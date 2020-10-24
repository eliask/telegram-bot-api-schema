import re
import lxml.html
from itertools import *
from collections import *
import json
import sys
import requests

url = 'https://core.telegram.org/bots/api'
requests.get(url).text
root = lxml.html.fromstring(requests.get(url).text)


def _rec_text(el):
    if el.text: yield el.text
    if el.tag == 'img' and el.attrib.get('alt'): yield el.attrib.get('alt')
    for c in el:
        yield from _rec_text(c)
def rec_text(el):
    return ''.join(chain(*(x.strip().split() for x in filter(None, _rec_text(el)))))

content = root.cssselect('#dev_page_content')

section_fields_raw=[]
section_params_raw=[]

section = None
for i, el in enumerate(content[0]):
    try:
        text = ''.join(x.strip() for x in el.itertext())
    except:
        continue

    if el.tag == 'h4': section = text
    if not section: continue

    if el.tag == 'table':
        thead = el.cssselect('thead')[0]
        tbody = el.cssselect('tbody')[0]

        head=None
        for tr in thead:
            head = [' '.join(x.strip() for x in td.itertext()) for td in tr]

        for tr in tbody:
            row = [' '.join(x.strip() for x in td.itertext()) for td in tr]
            assert len(row) == len(head)
            row = dict(zip(head, row))

            if 'Field' in row:
                section_fields_raw += [(section, row)]
            if 'Parameter' in row:
                section_params_raw += [(section, row)]


def group_by_section(xxx):
    prev=None
    g=[]
    for section, row in xxx:
        if section != prev and prev != None:
            yield prev, g
            g=[]
        prev=section
        g += [row]
    if g and prev:
        yield prev, g

section_fields = dict(group_by_section(section_fields_raw))
section_params = dict(group_by_section(section_params_raw))


def output_python(fh):
    type_map = {
        'String': 'str',
        'Integer': 'int',
        'Boolean': 'bool',
        'True': 'bool',
        'False': 'bool',
        'Float number': 'float',
        'Float': 'float',
    }

    print('''
from typing import List, Optional, Union
from dataclasses import dataclass

@dataclass
class CallbackGame: pass # Placeholder - zero fields in API doc

InputMessageContent = Union[
    'InputTextMessageContent',
    'InputLocationMessageContent',
    'InputVenueMessageContent',
    'InputContactMessageContent',
]

InputFile = str # TODO what type is this?

InlineQueryResult = Union[
    'InlineQueryResultCachedAudio',
    'InlineQueryResultCachedDocument',
    'InlineQueryResultCachedGif',
    'InlineQueryResultCachedMpeg4Gif',
    'InlineQueryResultCachedPhoto',
    'InlineQueryResultCachedSticker',
    'InlineQueryResultCachedVideo',
    'InlineQueryResultCachedVoice',
    'InlineQueryResultArticle',
    'InlineQueryResultAudio',
    'InlineQueryResultContact',
    'InlineQueryResultGame',
    'InlineQueryResultDocument',
    'InlineQueryResultGif',
    'InlineQueryResultLocation',
    'InlineQueryResultMpeg4Gif',
    'InlineQueryResultPhoto',
    'InlineQueryResultVenue',
    'InlineQueryResultVideo',
    'InlineQueryResultVoice',
]

InputMedia = Union[
    'InputMediaAnimation',
    'InputMediaDocument',
    'InputMediaAudio',
    'InputMediaPhoto',
    'InputMediaVideo',
]

PassportElementError = Union[
    'PassportElementErrorDataField',
    'PassportElementErrorFrontSide',
    'PassportElementErrorReverseSide',
    'PassportElementErrorSelfie',
    'PassportElementErrorFile',
    'PassportElementErrorFiles',
    'PassportElementErrorTranslationFile',
    'PassportElementErrorTranslationFiles',
    'PassportElementErrorUnspecified',
]
    ''', file=fh
    )

    seen_types=set(type_map.values()) | {'List', 'Optional', 'Union', 'InputFile', 'InputMessageContent', 'InlineQueryResult', 'InputMedia', 'PassportElementError'}
    for s,v in chain(section_fields.items(), section_params.items()):
        print(f'''
@dataclass
class {s}:
    '''.rstrip(), file=fh)

        for vv in v:
            type_ = vv['Type']
            array_of = 'Array of '
            while array_of in type_:
                last_index = type_.rfind(array_of)
                inner = type_[last_index+len(array_of):]
                inner = type_map.get(inner, inner)
                type_ = f'''{type_[:last_index]}List[{inner}]'''
            type_ = type_map.get(type_, type_)

            optional = False
            if 'Required' in vv:
                assert vv['Required'] in ('Optional', 'Yes')
                if vv['Required'] == 'Optional':
                    optional = True

            if vv['Description'].startswith('Optional'):
                optional = True

            if optional:
                type_ = f'''Optional[{type_}]'''

            inner_types = re.findall('(.*\[)([^\]]+)(\].*)', type_)
            if inner_types:
                _, inner_type, _ = inner_types[0]
                if inner_type not in seen_types:
                    type_ = re.sub('(.*\[)([^\]]+)(\].*)', "\\1'\\2'\\3", type_)
            elif type_ not in seen_types:
                type_ = f"'{type_}'"

            field = vv.get('Field') or vv.get('Parameter')

            # The only reserved keyword:
            if field == 'from': field = 'from_user'

            # There are few enough of these to enumerate them:
            type_ = type_.replace("'InputFile or String'", 'Union[InputFile, str]')
            type_ = type_.replace("'Integer or String'", 'Union[int, str]')
            type_ = type_.replace(
                "'InlineKeyboardMarkup or ReplyKeyboardMarkup or ReplyKeyboardRemove or ForceReply'",
                'Union[InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply]',
            )
            type_ = type_.replace(
                "'InputMediaPhoto and InputMediaVideo'",
                'Union[InputMediaPhoto, InputMediaVideo]',
            )

            assert ' or ' not in type_, type_
            assert ' and ' not in type_, type_

            description = vv['Description'].replace('Optional .', '').replace(' , ', ', ').strip()
            if description.endswith("'"): description += ' '

            comment = ''
            if vv['Type'] in ('True', 'False'):
                comment = f''' # Always {vv['Type']}'''

            print(f"""    '''{field}: {description}'''""", file=fh)
            print(f'''    {field}: {type_}{comment}''', file=fh)

        seen_types.add(s)


def output_json_schema(fh):
    type_map = {
        'String': 'string',
        'Integer': 'integer',
        'Boolean': 'boolean',
        'True': 'boolean',
        'False': 'boolean',
        'Float number': 'number',
        'Float': 'number',
    }

    # Use replacements instead of custom schema definitions to attempt to eliminate flat unions.
    # NB: This fails with quicktype until #493 is solved:
    # https://github.com/quicktype/quicktype/issues/493
    replacements = {}
    replacements['InputMessageContent'] = {
        "oneOf": [ { "$ref": f"#/definitions/{s}" } for s in [
        'InputTextMessageContent',
        'InputLocationMessageContent',
        'InputVenueMessageContent',
        'InputContactMessageContent',
    ]]
    }

    replacements['InlineQueryResult'] = {
        "oneOf": [ { "$ref": f"#/definitions/{s}" } for s in [
        'InlineQueryResultCachedAudio',
        'InlineQueryResultCachedDocument',
        'InlineQueryResultCachedGif',
        'InlineQueryResultCachedMpeg4Gif',
        'InlineQueryResultCachedPhoto',
        'InlineQueryResultCachedSticker',
        'InlineQueryResultCachedVideo',
        'InlineQueryResultCachedVoice',
        'InlineQueryResultArticle',
        'InlineQueryResultAudio',
        'InlineQueryResultContact',
        'InlineQueryResultGame',
        'InlineQueryResultDocument',
        'InlineQueryResultGif',
        'InlineQueryResultLocation',
        'InlineQueryResultMpeg4Gif',
        'InlineQueryResultPhoto',
        'InlineQueryResultVenue',
        'InlineQueryResultVideo',
        'InlineQueryResultVoice',
    ]]
    }

    replacements['InputMedia'] = {
        "oneOf": [ { "$ref": f"#/definitions/{s}" } for s in [
        'InputMediaAnimation',
        'InputMediaDocument',
        'InputMediaAudio',
        'InputMediaPhoto',
        'InputMediaVideo',
    ]]
    }

    replacements['PassportElementError'] = {
        "oneOf": [ { "$ref": f"#/definitions/{s}" } for s in [
        'PassportElementErrorDataField',
        'PassportElementErrorFrontSide',
        'PassportElementErrorReverseSide',
        'PassportElementErrorSelfie',
        'PassportElementErrorFile',
        'PassportElementErrorFiles',
        'PassportElementErrorTranslationFile',
        'PassportElementErrorTranslationFiles',
        'PassportElementErrorUnspecified',
    ]]
    }

    schema = {
        "$schema": "http://json-schema.org/draft-07/schema#",
        "$id": "",
        "title": "Telegram Bot API",
        "description": "Telegram Bot API. The root schema contains pseudo-attributes from ALL types to ensure quicktype generates all of them.",
        "definitions": {},
        "type": "object",
        "properties": {}
    }


    # empty definitions:
    schema['definitions']['InputFile'] = {
        "type": "object",
        "properties": {},
    }

    schema['definitions']['CallbackGame'] = {
        "type": "object",
        "properties": {},
    }

    for s,v in chain(section_fields.items(), section_params.items()):

        properties = {}
        required = {}
        for vv in v:
            field = vv.get('Field') or vv.get('Parameter')

            type_ = vv['Type']
            array_of = 'Array of '
            array_level = 0
            while array_of in type_:
                last_index = type_.rfind(array_of)
                inner = type_[last_index+len(array_of):]
                type_ = f'''{type_[:last_index]}{inner}'''
                array_level += 1

            optional = False
            if 'Required' in vv:
                assert vv['Required'] in ('Optional', 'Yes')
                if vv['Required'] == 'Optional':
                    optional = True

            if vv['Description'].startswith('Optional'):
                optional = True

            required[field] = not optional

            if ' or ' in type_:
                schema_type = type_.split(' or ')
            elif ' and ' in type_:
                schema_type = type_.split(' and ')
            else:
                schema_type = [type_]

            assert schema_type
            ss = []
            for z in schema_type:
                if z in type_map:
                    ss += [ { "type": type_map[z] }]
                elif z in replacements:
                    ss += [ replacements[z] ]
                else:
                    ss += [{ "$ref": f"#/definitions/{z}" }]

            properties[field] = ss[0] if len(ss) == 1 else {"oneOf": ss}

            description = vv['Description'].replace('Optional .', '').replace(' , ', ', ').strip()
            properties[field]['description'] = description

            for _ in range(array_level):
                properties[field] = {
                    "type": "array",
                    "items": properties[field],
                }

        schema2 = {
            "type": "object",
            "properties": properties,
            "required": [k for k,v in required.items() if v],
        }
        schema['definitions'][s] = schema2

        schema['properties'][s] = { "$ref": f"#/definitions/{s}" }


    json.dump(schema, fh, indent=2)


args = sys.argv[1:]
if 'python' in args:
    output_python(sys.stdout)
elif 'jsonschema' in args:
    output_json_schema(sys.stdout)
else:
    print(f'Usage: {sys.argv[0]} <jsonschema|python>', file=sys.stderr)
    sys.exit(1)
