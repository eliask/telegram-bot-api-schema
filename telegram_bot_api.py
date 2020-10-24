
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
    

@dataclass
class Update:
    '''update_id: The update's unique identifier. Update identifiers start from a certain positive number and increase sequentially. This ID becomes especially handy if you're using Webhooks, since it allows you to ignore repeated updates or to restore the correct update sequence, should they get out of order. If there are no new updates for at least a week, then identifier of the next update will be chosen randomly instead of sequentially.'''
    update_id: int
    '''message: New incoming message of any kind — text, photo, sticker, etc.'''
    message: Optional['Message']
    '''edited_message: New version of a message that is known to the bot and was edited'''
    edited_message: Optional['Message']
    '''channel_post: New incoming channel post of any kind — text, photo, sticker, etc.'''
    channel_post: Optional['Message']
    '''edited_channel_post: New version of a channel post that is known to the bot and was edited'''
    edited_channel_post: Optional['Message']
    '''inline_query: New incoming inline query'''
    inline_query: Optional['InlineQuery']
    '''chosen_inline_result: The result of an inline query that was chosen by a user and sent to their chat partner. Please see our documentation on the feedback collecting for details on how to enable these updates for your bot.'''
    chosen_inline_result: Optional['ChosenInlineResult']
    '''callback_query: New incoming callback query'''
    callback_query: Optional['CallbackQuery']
    '''shipping_query: New incoming shipping query. Only for invoices with flexible price'''
    shipping_query: Optional['ShippingQuery']
    '''pre_checkout_query: New incoming pre-checkout query. Contains full information about checkout'''
    pre_checkout_query: Optional['PreCheckoutQuery']
    '''poll: New poll state. Bots receive only updates about stopped polls and polls, which are sent by the bot'''
    poll: Optional['Poll']
    '''poll_answer: A user changed their answer in a non-anonymous poll. Bots receive new votes only in polls that were sent by the bot itself.'''
    poll_answer: Optional['PollAnswer']

@dataclass
class WebhookInfo:
    '''url: Webhook URL, may be empty if webhook is not set up'''
    url: str
    '''has_custom_certificate: True, if a custom certificate was provided for webhook certificate checks'''
    has_custom_certificate: bool
    '''pending_update_count: Number of updates awaiting delivery'''
    pending_update_count: int
    '''last_error_date: Unix time for the most recent error that happened when trying to deliver an update via webhook'''
    last_error_date: Optional[int]
    '''last_error_message: Error message in human-readable format for the most recent error that happened when trying to deliver an update via webhook'''
    last_error_message: Optional[str]
    '''max_connections: Maximum allowed number of simultaneous HTTPS connections to the webhook for update delivery'''
    max_connections: Optional[int]
    '''allowed_updates: A list of update types the bot is subscribed to. Defaults to all update types'''
    allowed_updates: Optional[List[str]]

@dataclass
class User:
    '''id: Unique identifier for this user or bot'''
    id: int
    '''is_bot: True, if this user is a bot'''
    is_bot: bool
    '''first_name: User's or bot's first name'''
    first_name: str
    '''last_name: User's or bot's last name'''
    last_name: Optional[str]
    '''username: User's or bot's username'''
    username: Optional[str]
    '''language_code: IETF language tag of the user's language'''
    language_code: Optional[str]
    '''can_join_groups: True, if the bot can be invited to groups. Returned only in getMe .'''
    can_join_groups: Optional[bool]
    '''can_read_all_group_messages: True, if privacy mode is disabled for the bot. Returned only in getMe .'''
    can_read_all_group_messages: Optional[bool]
    '''supports_inline_queries: True, if the bot supports inline queries. Returned only in getMe .'''
    supports_inline_queries: Optional[bool]

@dataclass
class Chat:
    '''id: Unique identifier for this chat. This number may be greater than 32 bits and some programming languages may have difficulty/silent defects in interpreting it. But it is smaller than 52 bits, so a signed 64 bit integer or double-precision float type are safe for storing this identifier.'''
    id: int
    '''type: Type of chat, can be either “private”, “group”, “supergroup” or “channel”'''
    type: str
    '''title: Title, for supergroups, channels and group chats'''
    title: Optional[str]
    '''username: Username, for private chats, supergroups and channels if available'''
    username: Optional[str]
    '''first_name: First name of the other party in a private chat'''
    first_name: Optional[str]
    '''last_name: Last name of the other party in a private chat'''
    last_name: Optional[str]
    '''photo: Chat photo. Returned only in getChat .'''
    photo: Optional['ChatPhoto']
    '''description: Description, for groups, supergroups and channel chats. Returned only in getChat .'''
    description: Optional[str]
    '''invite_link: Chat invite link, for groups, supergroups and channel chats. Each administrator in a chat generates their own invite links, so the bot must first generate the link using exportChatInviteLink . Returned only in getChat .'''
    invite_link: Optional[str]
    '''pinned_message: Pinned message, for groups, supergroups and channels. Returned only in getChat .'''
    pinned_message: Optional['Message']
    '''permissions: Default chat member permissions, for groups and supergroups. Returned only in getChat .'''
    permissions: Optional['ChatPermissions']
    '''slow_mode_delay: For supergroups, the minimum allowed delay between consecutive messages sent by each unpriviledged user. Returned only in getChat .'''
    slow_mode_delay: Optional[int]
    '''sticker_set_name: For supergroups, name of group sticker set. Returned only in getChat .'''
    sticker_set_name: Optional[str]
    '''can_set_sticker_set: True, if the bot can change the group sticker set. Returned only in getChat .'''
    can_set_sticker_set: Optional[bool]

@dataclass
class Message:
    '''message_id: Unique message identifier inside this chat'''
    message_id: int
    '''from_user: Sender, empty for messages sent to channels'''
    from_user: Optional[User]
    '''date: Date the message was sent in Unix time'''
    date: int
    '''chat: Conversation the message belongs to'''
    chat: Chat
    '''forward_from: For forwarded messages, sender of the original message'''
    forward_from: Optional[User]
    '''forward_from_chat: For messages forwarded from channels, information about the original channel'''
    forward_from_chat: Optional[Chat]
    '''forward_from_message_id: For messages forwarded from channels, identifier of the original message in the channel'''
    forward_from_message_id: Optional[int]
    '''forward_signature: For messages forwarded from channels, signature of the post author if present'''
    forward_signature: Optional[str]
    '''forward_sender_name: Sender's name for messages forwarded from users who disallow adding a link to their account in forwarded messages'''
    forward_sender_name: Optional[str]
    '''forward_date: For forwarded messages, date the original message was sent in Unix time'''
    forward_date: Optional[int]
    '''reply_to_message: For replies, the original message. Note that the Message object in this field will not contain further reply_to_message fields even if it itself is a reply.'''
    reply_to_message: Optional['Message']
    '''via_bot: Bot through which the message was sent'''
    via_bot: Optional[User]
    '''edit_date: Date the message was last edited in Unix time'''
    edit_date: Optional[int]
    '''media_group_id: The unique identifier of a media message group this message belongs to'''
    media_group_id: Optional[str]
    '''author_signature: Signature of the post author for messages in channels'''
    author_signature: Optional[str]
    '''text: For text messages, the actual UTF-8 text of the message, 0-4096 characters'''
    text: Optional[str]
    '''entities: For text messages, special entities like usernames, URLs, bot commands, etc. that appear in the text'''
    entities: Optional[List['MessageEntity']]
    '''animation: Message is an animation, information about the animation. For backward compatibility, when this field is set, the document field will also be set'''
    animation: Optional['Animation']
    '''audio: Message is an audio file, information about the file'''
    audio: Optional['Audio']
    '''document: Message is a general file, information about the file'''
    document: Optional['Document']
    '''photo: Message is a photo, available sizes of the photo'''
    photo: Optional[List['PhotoSize']]
    '''sticker: Message is a sticker, information about the sticker'''
    sticker: Optional['Sticker']
    '''video: Message is a video, information about the video'''
    video: Optional['Video']
    '''video_note: Message is a video note, information about the video message'''
    video_note: Optional['VideoNote']
    '''voice: Message is a voice message, information about the file'''
    voice: Optional['Voice']
    '''caption: Caption for the animation, audio, document, photo, video or voice, 0-1024 characters'''
    caption: Optional[str]
    '''caption_entities: For messages with a caption, special entities like usernames, URLs, bot commands, etc. that appear in the caption'''
    caption_entities: Optional[List['MessageEntity']]
    '''contact: Message is a shared contact, information about the contact'''
    contact: Optional['Contact']
    '''dice: Message is a dice with random value from 1 to 6'''
    dice: Optional['Dice']
    '''game: Message is a game, information about the game. More about games »'''
    game: Optional['Game']
    '''poll: Message is a native poll, information about the poll'''
    poll: Optional['Poll']
    '''venue: Message is a venue, information about the venue. For backward compatibility, when this field is set, the location field will also be set'''
    venue: Optional['Venue']
    '''location: Message is a shared location, information about the location'''
    location: Optional['Location']
    '''new_chat_members: New members that were added to the group or supergroup and information about them (the bot itself may be one of these members)'''
    new_chat_members: Optional[List[User]]
    '''left_chat_member: A member was removed from the group, information about them (this member may be the bot itself)'''
    left_chat_member: Optional[User]
    '''new_chat_title: A chat title was changed to this value'''
    new_chat_title: Optional[str]
    '''new_chat_photo: A chat photo was change to this value'''
    new_chat_photo: Optional[List['PhotoSize']]
    '''delete_chat_photo: Service message: the chat photo was deleted'''
    delete_chat_photo: Optional[bool] # Always True
    '''group_chat_created: Service message: the group has been created'''
    group_chat_created: Optional[bool] # Always True
    '''supergroup_chat_created: Service message: the supergroup has been created. This field can't be received in a message coming through updates, because bot can't be a member of a supergroup when it is created. It can only be found in reply_to_message if someone replies to a very first message in a directly created supergroup.'''
    supergroup_chat_created: Optional[bool] # Always True
    '''channel_chat_created: Service message: the channel has been created. This field can't be received in a message coming through updates, because bot can't be a member of a channel when it is created. It can only be found in reply_to_message if someone replies to a very first message in a channel.'''
    channel_chat_created: Optional[bool] # Always True
    '''migrate_to_chat_id: The group has been migrated to a supergroup with the specified identifier. This number may be greater than 32 bits and some programming languages may have difficulty/silent defects in interpreting it. But it is smaller than 52 bits, so a signed 64 bit integer or double-precision float type are safe for storing this identifier.'''
    migrate_to_chat_id: Optional[int]
    '''migrate_from_chat_id: The supergroup has been migrated from a group with the specified identifier. This number may be greater than 32 bits and some programming languages may have difficulty/silent defects in interpreting it. But it is smaller than 52 bits, so a signed 64 bit integer or double-precision float type are safe for storing this identifier.'''
    migrate_from_chat_id: Optional[int]
    '''pinned_message: Specified message was pinned. Note that the Message object in this field will not contain further reply_to_message fields even if it is itself a reply.'''
    pinned_message: Optional['Message']
    '''invoice: Message is an invoice for a payment, information about the invoice. More about payments »'''
    invoice: Optional['Invoice']
    '''successful_payment: Message is a service message about a successful payment, information about the payment. More about payments »'''
    successful_payment: Optional['SuccessfulPayment']
    '''connected_website: The domain name of the website on which the user has logged in. More about Telegram Login »'''
    connected_website: Optional[str]
    '''passport_data: Telegram Passport data'''
    passport_data: Optional['PassportData']
    '''reply_markup: Inline keyboard attached to the message. login_url buttons are represented as ordinary url buttons.'''
    reply_markup: Optional['InlineKeyboardMarkup']

@dataclass
class MessageEntity:
    '''type: Type of the entity. Can be “mention” ( @username ), “hashtag” ( #hashtag ), “cashtag” ( $USD ), “bot_command” ( /start@jobs_bot ), “url” ( https://telegram.org ), “email” ( do-not-reply@telegram.org ), “phone_number” ( +1-212-555-0123 ), “bold” ( bold text ), “italic” ( italic text ), “underline” (underlined text), “strikethrough” (strikethrough text), “code” (monowidth string), “pre” (monowidth block), “text_link” (for clickable text URLs), “text_mention” (for users without usernames )'''
    type: str
    '''offset: Offset in UTF-16 code units to the start of the entity'''
    offset: int
    '''length: Length of the entity in UTF-16 code units'''
    length: int
    '''url: For “text_link” only, url that will be opened after user taps on the text'''
    url: Optional[str]
    '''user: For “text_mention” only, the mentioned user'''
    user: Optional[User]
    '''language: For “pre” only, the programming language of the entity text'''
    language: Optional[str]

@dataclass
class PhotoSize:
    '''file_id: Identifier for this file, which can be used to download or reuse the file'''
    file_id: str
    '''file_unique_id: Unique identifier for this file, which is supposed to be the same over time and for different bots. Can't be used to download or reuse the file.'''
    file_unique_id: str
    '''width: Photo width'''
    width: int
    '''height: Photo height'''
    height: int
    '''file_size: File size'''
    file_size: Optional[int]

@dataclass
class Animation:
    '''file_id: Identifier for this file, which can be used to download or reuse the file'''
    file_id: str
    '''file_unique_id: Unique identifier for this file, which is supposed to be the same over time and for different bots. Can't be used to download or reuse the file.'''
    file_unique_id: str
    '''width: Video width as defined by sender'''
    width: int
    '''height: Video height as defined by sender'''
    height: int
    '''duration: Duration of the video in seconds as defined by sender'''
    duration: int
    '''thumb: Animation thumbnail as defined by sender'''
    thumb: Optional[PhotoSize]
    '''file_name: Original animation filename as defined by sender'''
    file_name: Optional[str]
    '''mime_type: MIME type of the file as defined by sender'''
    mime_type: Optional[str]
    '''file_size: File size'''
    file_size: Optional[int]

@dataclass
class Audio:
    '''file_id: Identifier for this file, which can be used to download or reuse the file'''
    file_id: str
    '''file_unique_id: Unique identifier for this file, which is supposed to be the same over time and for different bots. Can't be used to download or reuse the file.'''
    file_unique_id: str
    '''duration: Duration of the audio in seconds as defined by sender'''
    duration: int
    '''performer: Performer of the audio as defined by sender or by audio tags'''
    performer: Optional[str]
    '''title: Title of the audio as defined by sender or by audio tags'''
    title: Optional[str]
    '''mime_type: MIME type of the file as defined by sender'''
    mime_type: Optional[str]
    '''file_size: File size'''
    file_size: Optional[int]
    '''thumb: Thumbnail of the album cover to which the music file belongs'''
    thumb: Optional[PhotoSize]

@dataclass
class Document:
    '''file_id: Identifier for this file, which can be used to download or reuse the file'''
    file_id: str
    '''file_unique_id: Unique identifier for this file, which is supposed to be the same over time and for different bots. Can't be used to download or reuse the file.'''
    file_unique_id: str
    '''thumb: Document thumbnail as defined by sender'''
    thumb: Optional[PhotoSize]
    '''file_name: Original filename as defined by sender'''
    file_name: Optional[str]
    '''mime_type: MIME type of the file as defined by sender'''
    mime_type: Optional[str]
    '''file_size: File size'''
    file_size: Optional[int]

@dataclass
class Video:
    '''file_id: Identifier for this file, which can be used to download or reuse the file'''
    file_id: str
    '''file_unique_id: Unique identifier for this file, which is supposed to be the same over time and for different bots. Can't be used to download or reuse the file.'''
    file_unique_id: str
    '''width: Video width as defined by sender'''
    width: int
    '''height: Video height as defined by sender'''
    height: int
    '''duration: Duration of the video in seconds as defined by sender'''
    duration: int
    '''thumb: Video thumbnail'''
    thumb: Optional[PhotoSize]
    '''mime_type: Mime type of a file as defined by sender'''
    mime_type: Optional[str]
    '''file_size: File size'''
    file_size: Optional[int]

@dataclass
class VideoNote:
    '''file_id: Identifier for this file, which can be used to download or reuse the file'''
    file_id: str
    '''file_unique_id: Unique identifier for this file, which is supposed to be the same over time and for different bots. Can't be used to download or reuse the file.'''
    file_unique_id: str
    '''length: Video width and height (diameter of the video message) as defined by sender'''
    length: int
    '''duration: Duration of the video in seconds as defined by sender'''
    duration: int
    '''thumb: Video thumbnail'''
    thumb: Optional[PhotoSize]
    '''file_size: File size'''
    file_size: Optional[int]

@dataclass
class Voice:
    '''file_id: Identifier for this file, which can be used to download or reuse the file'''
    file_id: str
    '''file_unique_id: Unique identifier for this file, which is supposed to be the same over time and for different bots. Can't be used to download or reuse the file.'''
    file_unique_id: str
    '''duration: Duration of the audio in seconds as defined by sender'''
    duration: int
    '''mime_type: MIME type of the file as defined by sender'''
    mime_type: Optional[str]
    '''file_size: File size'''
    file_size: Optional[int]

@dataclass
class Contact:
    '''phone_number: Contact's phone number'''
    phone_number: str
    '''first_name: Contact's first name'''
    first_name: str
    '''last_name: Contact's last name'''
    last_name: Optional[str]
    '''user_id: Contact's user identifier in Telegram'''
    user_id: Optional[int]
    '''vcard: Additional data about the contact in the form of a vCard'''
    vcard: Optional[str]

@dataclass
class Dice:
    '''emoji: Emoji on which the dice throw animation is based'''
    emoji: str
    '''value: Value of the dice, 1-6 for “ ” and “ ” base emoji, 1-5 for “ ” base emoji'''
    value: int

@dataclass
class PollOption:
    '''text: Option text, 1-100 characters'''
    text: str
    '''voter_count: Number of users that voted for this option'''
    voter_count: int

@dataclass
class PollAnswer:
    '''poll_id: Unique poll identifier'''
    poll_id: str
    '''user: The user, who changed the answer to the poll'''
    user: User
    '''option_ids: 0-based identifiers of answer options, chosen by the user. May be empty if the user retracted their vote.'''
    option_ids: List[int]

@dataclass
class Poll:
    '''id: Unique poll identifier'''
    id: str
    '''question: Poll question, 1-255 characters'''
    question: str
    '''options: List of poll options'''
    options: List[PollOption]
    '''total_voter_count: Total number of users that voted in the poll'''
    total_voter_count: int
    '''is_closed: True, if the poll is closed'''
    is_closed: bool
    '''is_anonymous: True, if the poll is anonymous'''
    is_anonymous: bool
    '''type: Poll type, currently can be “regular” or “quiz”'''
    type: str
    '''allows_multiple_answers: True, if the poll allows multiple answers'''
    allows_multiple_answers: bool
    '''correct_option_id: 0-based identifier of the correct answer option. Available only for polls in the quiz mode, which are closed, or was sent (not forwarded) by the bot or to the private chat with the bot.'''
    correct_option_id: Optional[int]
    '''explanation: Text that is shown when a user chooses an incorrect answer or taps on the lamp icon in a quiz-style poll, 0-200 characters'''
    explanation: Optional[str]
    '''explanation_entities: Special entities like usernames, URLs, bot commands, etc. that appear in the explanation'''
    explanation_entities: Optional[List[MessageEntity]]
    '''open_period: Amount of time in seconds the poll will be active after creation'''
    open_period: Optional[int]
    '''close_date: Point in time (Unix timestamp) when the poll will be automatically closed'''
    close_date: Optional[int]

@dataclass
class Location:
    '''longitude: Longitude as defined by sender'''
    longitude: float
    '''latitude: Latitude as defined by sender'''
    latitude: float

@dataclass
class Venue:
    '''location: Venue location'''
    location: Location
    '''title: Name of the venue'''
    title: str
    '''address: Address of the venue'''
    address: str
    '''foursquare_id: Foursquare identifier of the venue'''
    foursquare_id: Optional[str]
    '''foursquare_type: Foursquare type of the venue. (For example, “arts_entertainment/default”, “arts_entertainment/aquarium” or “food/icecream”.)'''
    foursquare_type: Optional[str]

@dataclass
class UserProfilePhotos:
    '''total_count: Total number of profile pictures the target user has'''
    total_count: int
    '''photos: Requested profile pictures (in up to 4 sizes each)'''
    photos: List[List[PhotoSize]]

@dataclass
class File:
    '''file_id: Identifier for this file, which can be used to download or reuse the file'''
    file_id: str
    '''file_unique_id: Unique identifier for this file, which is supposed to be the same over time and for different bots. Can't be used to download or reuse the file.'''
    file_unique_id: str
    '''file_size: File size, if known'''
    file_size: Optional[int]
    '''file_path: File path. Use https://api.telegram.org/file/bot<token>/<file_path> to get the file.'''
    file_path: Optional[str]

@dataclass
class ReplyKeyboardMarkup:
    '''keyboard: Array of button rows, each represented by an Array of KeyboardButton objects'''
    keyboard: List[List['KeyboardButton']]
    '''resize_keyboard: Requests clients to resize the keyboard vertically for optimal fit (e.g., make the keyboard smaller if there are just two rows of buttons). Defaults to false, in which case the custom keyboard is always of the same height as the app's standard keyboard.'''
    resize_keyboard: Optional[bool]
    '''one_time_keyboard: Requests clients to hide the keyboard as soon as it's been used. The keyboard will still be available, but clients will automatically display the usual letter-keyboard in the chat – the user can press a special button in the input field to see the custom keyboard again. Defaults to false .'''
    one_time_keyboard: Optional[bool]
    '''selective: Use this parameter if you want to show the keyboard to specific users only. Targets: 1) users that are @mentioned in the text of the Message object; 2) if the bot's message is a reply (has reply_to_message_id ), sender of the original message. Example: A user requests to change the bot's language, bot replies to the request with a keyboard to select the new language. Other users in the group don't see the keyboard.'''
    selective: Optional[bool]

@dataclass
class KeyboardButton:
    '''text: Text of the button. If none of the optional fields are used, it will be sent as a message when the button is pressed'''
    text: str
    '''request_contact: If True, the user's phone number will be sent as a contact when the button is pressed. Available in private chats only'''
    request_contact: Optional[bool]
    '''request_location: If True, the user's current location will be sent when the button is pressed. Available in private chats only'''
    request_location: Optional[bool]
    '''request_poll: If specified, the user will be asked to create a poll and send it to the bot when the button is pressed. Available in private chats only'''
    request_poll: Optional['KeyboardButtonPollType']

@dataclass
class KeyboardButtonPollType:
    '''type: If quiz is passed, the user will be allowed to create only polls in the quiz mode. If regular is passed, only regular polls will be allowed. Otherwise, the user will be allowed to create a poll of any type.'''
    type: Optional[str]

@dataclass
class ReplyKeyboardRemove:
    '''remove_keyboard: Requests clients to remove the custom keyboard (user will not be able to summon this keyboard; if you want to hide the keyboard from sight but keep it accessible, use one_time_keyboard in ReplyKeyboardMarkup )'''
    remove_keyboard: bool # Always True
    '''selective: Use this parameter if you want to remove the keyboard for specific users only. Targets: 1) users that are @mentioned in the text of the Message object; 2) if the bot's message is a reply (has reply_to_message_id ), sender of the original message. Example: A user votes in a poll, bot returns confirmation message in reply to the vote and removes the keyboard for that user, while still showing the keyboard with poll options to users who haven't voted yet.'''
    selective: Optional[bool]

@dataclass
class InlineKeyboardMarkup:
    '''inline_keyboard: Array of button rows, each represented by an Array of InlineKeyboardButton objects'''
    inline_keyboard: List[List['InlineKeyboardButton']]

@dataclass
class InlineKeyboardButton:
    '''text: Label text on the button'''
    text: str
    '''url: HTTP or tg:// url to be opened when button is pressed'''
    url: Optional[str]
    '''login_url: An HTTP URL used to automatically authorize the user. Can be used as a replacement for the Telegram Login Widget .'''
    login_url: Optional['LoginUrl']
    '''callback_data: Data to be sent in a callback query to the bot when button is pressed, 1-64 bytes'''
    callback_data: Optional[str]
    '''switch_inline_query: If set, pressing the button will prompt the user to select one of their chats, open that chat and insert the bot's username and the specified inline query in the input field. Can be empty, in which case just the bot's username will be inserted. Note: This offers an easy way for users to start using your bot in inline mode when they are currently in a private chat with it. Especially useful when combined with switch_pm… actions – in this case the user will be automatically returned to the chat they switched from, skipping the chat selection screen.'''
    switch_inline_query: Optional[str]
    '''switch_inline_query_current_chat: If set, pressing the button will insert the bot's username and the specified inline query in the current chat's input field. Can be empty, in which case only the bot's username will be inserted. This offers a quick way for the user to open your bot in inline mode in the same chat – good for selecting something from multiple options.'''
    switch_inline_query_current_chat: Optional[str]
    '''callback_game: Description of the game that will be launched when the user presses the button. NOTE: This type of button must always be the first button in the first row.'''
    callback_game: Optional['CallbackGame']
    '''pay: Specify True, to send a Pay button . NOTE: This type of button must always be the first button in the first row.'''
    pay: Optional[bool]

@dataclass
class LoginUrl:
    '''url: An HTTP URL to be opened with user authorization data added to the query string when the button is pressed. If the user refuses to provide authorization data, the original URL without information about the user will be opened. The data added is the same as described in Receiving authorization data . NOTE: You must always check the hash of the received data to verify the authentication and the integrity of the data as described in Checking authorization .'''
    url: str
    '''forward_text: New text of the button in forwarded messages.'''
    forward_text: Optional[str]
    '''bot_username: Username of a bot, which will be used for user authorization. See Setting up a bot for more details. If not specified, the current bot's username will be assumed. The url 's domain must be the same as the domain linked with the bot. See Linking your domain to the bot for more details.'''
    bot_username: Optional[str]
    '''request_write_access: Pass True to request the permission for your bot to send messages to the user.'''
    request_write_access: Optional[bool]

@dataclass
class CallbackQuery:
    '''id: Unique identifier for this query'''
    id: str
    '''from_user: Sender'''
    from_user: User
    '''message: Message with the callback button that originated the query. Note that message content and message date will not be available if the message is too old'''
    message: Optional[Message]
    '''inline_message_id: Identifier of the message sent via the bot in inline mode, that originated the query.'''
    inline_message_id: Optional[str]
    '''chat_instance: Global identifier, uniquely corresponding to the chat to which the message with the callback button was sent. Useful for high scores in games .'''
    chat_instance: str
    '''data: Data associated with the callback button. Be aware that a bad client can send arbitrary data in this field.'''
    data: Optional[str]
    '''game_short_name: Short name of a Game to be returned, serves as the unique identifier for the game'''
    game_short_name: Optional[str]

@dataclass
class ForceReply:
    '''force_reply: Shows reply interface to the user, as if they manually selected the bot's message and tapped 'Reply' '''
    force_reply: bool # Always True
    '''selective: Use this parameter if you want to force reply from specific users only. Targets: 1) users that are @mentioned in the text of the Message object; 2) if the bot's message is a reply (has reply_to_message_id ), sender of the original message.'''
    selective: Optional[bool]

@dataclass
class ChatPhoto:
    '''small_file_id: File identifier of small (160x160) chat photo. This file_id can be used only for photo download and only for as long as the photo is not changed.'''
    small_file_id: str
    '''small_file_unique_id: Unique file identifier of small (160x160) chat photo, which is supposed to be the same over time and for different bots. Can't be used to download or reuse the file.'''
    small_file_unique_id: str
    '''big_file_id: File identifier of big (640x640) chat photo. This file_id can be used only for photo download and only for as long as the photo is not changed.'''
    big_file_id: str
    '''big_file_unique_id: Unique file identifier of big (640x640) chat photo, which is supposed to be the same over time and for different bots. Can't be used to download or reuse the file.'''
    big_file_unique_id: str

@dataclass
class ChatMember:
    '''user: Information about the user'''
    user: User
    '''status: The member's status in the chat. Can be “creator”, “administrator”, “member”, “restricted”, “left” or “kicked”'''
    status: str
    '''custom_title: Owner and administrators only. Custom title for this user'''
    custom_title: Optional[str]
    '''until_date: Restricted and kicked only. Date when restrictions will be lifted for this user; unix time'''
    until_date: Optional[int]
    '''can_be_edited: Administrators only. True, if the bot is allowed to edit administrator privileges of that user'''
    can_be_edited: Optional[bool]
    '''can_post_messages: Administrators only. True, if the administrator can post in the channel; channels only'''
    can_post_messages: Optional[bool]
    '''can_edit_messages: Administrators only. True, if the administrator can edit messages of other users and can pin messages; channels only'''
    can_edit_messages: Optional[bool]
    '''can_delete_messages: Administrators only. True, if the administrator can delete messages of other users'''
    can_delete_messages: Optional[bool]
    '''can_restrict_members: Administrators only. True, if the administrator can restrict, ban or unban chat members'''
    can_restrict_members: Optional[bool]
    '''can_promote_members: Administrators only. True, if the administrator can add new administrators with a subset of their own privileges or demote administrators that he has promoted, directly or indirectly (promoted by administrators that were appointed by the user)'''
    can_promote_members: Optional[bool]
    '''can_change_info: Administrators and restricted only. True, if the user is allowed to change the chat title, photo and other settings'''
    can_change_info: Optional[bool]
    '''can_invite_users: Administrators and restricted only. True, if the user is allowed to invite new users to the chat'''
    can_invite_users: Optional[bool]
    '''can_pin_messages: Administrators and restricted only. True, if the user is allowed to pin messages; groups and supergroups only'''
    can_pin_messages: Optional[bool]
    '''is_member: Restricted only. True, if the user is a member of the chat at the moment of the request'''
    is_member: Optional[bool]
    '''can_send_messages: Restricted only. True, if the user is allowed to send text messages, contacts, locations and venues'''
    can_send_messages: Optional[bool]
    '''can_send_media_messages: Restricted only. True, if the user is allowed to send audios, documents, photos, videos, video notes and voice notes'''
    can_send_media_messages: Optional[bool]
    '''can_send_polls: Restricted only. True, if the user is allowed to send polls'''
    can_send_polls: Optional[bool]
    '''can_send_other_messages: Restricted only. True, if the user is allowed to send animations, games, stickers and use inline bots'''
    can_send_other_messages: Optional[bool]
    '''can_add_web_page_previews: Restricted only. True, if the user is allowed to add web page previews to their messages'''
    can_add_web_page_previews: Optional[bool]

@dataclass
class ChatPermissions:
    '''can_send_messages: True, if the user is allowed to send text messages, contacts, locations and venues'''
    can_send_messages: Optional[bool]
    '''can_send_media_messages: True, if the user is allowed to send audios, documents, photos, videos, video notes and voice notes, implies can_send_messages'''
    can_send_media_messages: Optional[bool]
    '''can_send_polls: True, if the user is allowed to send polls, implies can_send_messages'''
    can_send_polls: Optional[bool]
    '''can_send_other_messages: True, if the user is allowed to send animations, games, stickers and use inline bots, implies can_send_media_messages'''
    can_send_other_messages: Optional[bool]
    '''can_add_web_page_previews: True, if the user is allowed to add web page previews to their messages, implies can_send_media_messages'''
    can_add_web_page_previews: Optional[bool]
    '''can_change_info: True, if the user is allowed to change the chat title, photo and other settings. Ignored in public supergroups'''
    can_change_info: Optional[bool]
    '''can_invite_users: True, if the user is allowed to invite new users to the chat'''
    can_invite_users: Optional[bool]
    '''can_pin_messages: True, if the user is allowed to pin messages. Ignored in public supergroups'''
    can_pin_messages: Optional[bool]

@dataclass
class BotCommand:
    '''command: Text of the command, 1-32 characters. Can contain only lowercase English letters, digits and underscores.'''
    command: str
    '''description: Description of the command, 3-256 characters.'''
    description: str

@dataclass
class ResponseParameters:
    '''migrate_to_chat_id: The group has been migrated to a supergroup with the specified identifier. This number may be greater than 32 bits and some programming languages may have difficulty/silent defects in interpreting it. But it is smaller than 52 bits, so a signed 64 bit integer or double-precision float type are safe for storing this identifier.'''
    migrate_to_chat_id: Optional[int]
    '''retry_after: In case of exceeding flood control, the number of seconds left to wait before the request can be repeated'''
    retry_after: Optional[int]

@dataclass
class InputMediaPhoto:
    '''type: Type of the result, must be photo'''
    type: str
    '''media: File to send. Pass a file_id to send a file that exists on the Telegram servers (recommended), pass an HTTP URL for Telegram to get a file from the Internet, or pass “attach://<file_attach_name>” to upload a new one using multipart/form-data under <file_attach_name> name. More info on Sending Files »'''
    media: str
    '''caption: Caption of the photo to be sent, 0-1024 characters after entities parsing'''
    caption: Optional[str]
    '''parse_mode: Mode for parsing entities in the photo caption. See formatting options for more details.'''
    parse_mode: Optional[str]

@dataclass
class InputMediaVideo:
    '''type: Type of the result, must be video'''
    type: str
    '''media: File to send. Pass a file_id to send a file that exists on the Telegram servers (recommended), pass an HTTP URL for Telegram to get a file from the Internet, or pass “attach://<file_attach_name>” to upload a new one using multipart/form-data under <file_attach_name> name. More info on Sending Files »'''
    media: str
    '''thumb: Thumbnail of the file sent; can be ignored if thumbnail generation for the file is supported server-side. The thumbnail should be in JPEG format and less than 200 kB in size. A thumbnail's width and height should not exceed 320. Ignored if the file is not uploaded using multipart/form-data. Thumbnails can't be reused and can be only uploaded as a new file, so you can pass “attach://<file_attach_name>” if the thumbnail was uploaded using multipart/form-data under <file_attach_name>. More info on Sending Files »'''
    thumb: Optional[Union[InputFile, str]]
    '''caption: Caption of the video to be sent, 0-1024 characters after entities parsing'''
    caption: Optional[str]
    '''parse_mode: Mode for parsing entities in the video caption. See formatting options for more details.'''
    parse_mode: Optional[str]
    '''width: Video width'''
    width: Optional[int]
    '''height: Video height'''
    height: Optional[int]
    '''duration: Video duration'''
    duration: Optional[int]
    '''supports_streaming: Pass True, if the uploaded video is suitable for streaming'''
    supports_streaming: Optional[bool]

@dataclass
class InputMediaAnimation:
    '''type: Type of the result, must be animation'''
    type: str
    '''media: File to send. Pass a file_id to send a file that exists on the Telegram servers (recommended), pass an HTTP URL for Telegram to get a file from the Internet, or pass “attach://<file_attach_name>” to upload a new one using multipart/form-data under <file_attach_name> name. More info on Sending Files »'''
    media: str
    '''thumb: Thumbnail of the file sent; can be ignored if thumbnail generation for the file is supported server-side. The thumbnail should be in JPEG format and less than 200 kB in size. A thumbnail's width and height should not exceed 320. Ignored if the file is not uploaded using multipart/form-data. Thumbnails can't be reused and can be only uploaded as a new file, so you can pass “attach://<file_attach_name>” if the thumbnail was uploaded using multipart/form-data under <file_attach_name>. More info on Sending Files »'''
    thumb: Optional[Union[InputFile, str]]
    '''caption: Caption of the animation to be sent, 0-1024 characters after entities parsing'''
    caption: Optional[str]
    '''parse_mode: Mode for parsing entities in the animation caption. See formatting options for more details.'''
    parse_mode: Optional[str]
    '''width: Animation width'''
    width: Optional[int]
    '''height: Animation height'''
    height: Optional[int]
    '''duration: Animation duration'''
    duration: Optional[int]

@dataclass
class InputMediaAudio:
    '''type: Type of the result, must be audio'''
    type: str
    '''media: File to send. Pass a file_id to send a file that exists on the Telegram servers (recommended), pass an HTTP URL for Telegram to get a file from the Internet, or pass “attach://<file_attach_name>” to upload a new one using multipart/form-data under <file_attach_name> name. More info on Sending Files »'''
    media: str
    '''thumb: Thumbnail of the file sent; can be ignored if thumbnail generation for the file is supported server-side. The thumbnail should be in JPEG format and less than 200 kB in size. A thumbnail's width and height should not exceed 320. Ignored if the file is not uploaded using multipart/form-data. Thumbnails can't be reused and can be only uploaded as a new file, so you can pass “attach://<file_attach_name>” if the thumbnail was uploaded using multipart/form-data under <file_attach_name>. More info on Sending Files »'''
    thumb: Optional[Union[InputFile, str]]
    '''caption: Caption of the audio to be sent, 0-1024 characters after entities parsing'''
    caption: Optional[str]
    '''parse_mode: Mode for parsing entities in the audio caption. See formatting options for more details.'''
    parse_mode: Optional[str]
    '''duration: Duration of the audio in seconds'''
    duration: Optional[int]
    '''performer: Performer of the audio'''
    performer: Optional[str]
    '''title: Title of the audio'''
    title: Optional[str]

@dataclass
class InputMediaDocument:
    '''type: Type of the result, must be document'''
    type: str
    '''media: File to send. Pass a file_id to send a file that exists on the Telegram servers (recommended), pass an HTTP URL for Telegram to get a file from the Internet, or pass “attach://<file_attach_name>” to upload a new one using multipart/form-data under <file_attach_name> name. More info on Sending Files »'''
    media: str
    '''thumb: Thumbnail of the file sent; can be ignored if thumbnail generation for the file is supported server-side. The thumbnail should be in JPEG format and less than 200 kB in size. A thumbnail's width and height should not exceed 320. Ignored if the file is not uploaded using multipart/form-data. Thumbnails can't be reused and can be only uploaded as a new file, so you can pass “attach://<file_attach_name>” if the thumbnail was uploaded using multipart/form-data under <file_attach_name>. More info on Sending Files »'''
    thumb: Optional[Union[InputFile, str]]
    '''caption: Caption of the document to be sent, 0-1024 characters after entities parsing'''
    caption: Optional[str]
    '''parse_mode: Mode for parsing entities in the document caption. See formatting options for more details.'''
    parse_mode: Optional[str]

@dataclass
class Sticker:
    '''file_id: Identifier for this file, which can be used to download or reuse the file'''
    file_id: str
    '''file_unique_id: Unique identifier for this file, which is supposed to be the same over time and for different bots. Can't be used to download or reuse the file.'''
    file_unique_id: str
    '''width: Sticker width'''
    width: int
    '''height: Sticker height'''
    height: int
    '''is_animated: True, if the sticker is animated'''
    is_animated: bool
    '''thumb: Sticker thumbnail in the .WEBP or .JPG format'''
    thumb: Optional[PhotoSize]
    '''emoji: Emoji associated with the sticker'''
    emoji: Optional[str]
    '''set_name: Name of the sticker set to which the sticker belongs'''
    set_name: Optional[str]
    '''mask_position: For mask stickers, the position where the mask should be placed'''
    mask_position: Optional['MaskPosition']
    '''file_size: File size'''
    file_size: Optional[int]

@dataclass
class StickerSet:
    '''name: Sticker set name'''
    name: str
    '''title: Sticker set title'''
    title: str
    '''is_animated: True, if the sticker set contains animated stickers'''
    is_animated: bool
    '''contains_masks: True, if the sticker set contains masks'''
    contains_masks: bool
    '''stickers: List of all set stickers'''
    stickers: List[Sticker]
    '''thumb: Sticker set thumbnail in the .WEBP or .TGS format'''
    thumb: Optional[PhotoSize]

@dataclass
class MaskPosition:
    '''point: The part of the face relative to which the mask should be placed. One of “forehead”, “eyes”, “mouth”, or “chin”.'''
    point: str
    '''x_shift: Shift by X-axis measured in widths of the mask scaled to the face size, from left to right. For example, choosing -1.0 will place mask just to the left of the default mask position.'''
    x_shift: float
    '''y_shift: Shift by Y-axis measured in heights of the mask scaled to the face size, from top to bottom. For example, 1.0 will place the mask just below the default mask position.'''
    y_shift: float
    '''scale: Mask scaling coefficient. For example, 2.0 means double size.'''
    scale: float

@dataclass
class InlineQuery:
    '''id: Unique identifier for this query'''
    id: str
    '''from_user: Sender'''
    from_user: User
    '''location: Sender location, only for bots that request user location'''
    location: Optional[Location]
    '''query: Text of the query (up to 256 characters)'''
    query: str
    '''offset: Offset of the results to be returned, can be controlled by the bot'''
    offset: str

@dataclass
class InlineQueryResultArticle:
    '''type: Type of the result, must be article'''
    type: str
    '''id: Unique identifier for this result, 1-64 Bytes'''
    id: str
    '''title: Title of the result'''
    title: str
    '''input_message_content: Content of the message to be sent'''
    input_message_content: InputMessageContent
    '''reply_markup: Inline keyboard attached to the message'''
    reply_markup: Optional[InlineKeyboardMarkup]
    '''url: URL of the result'''
    url: Optional[str]
    '''hide_url: Pass True, if you don't want the URL to be shown in the message'''
    hide_url: Optional[bool]
    '''description: Short description of the result'''
    description: Optional[str]
    '''thumb_url: Url of the thumbnail for the result'''
    thumb_url: Optional[str]
    '''thumb_width: Thumbnail width'''
    thumb_width: Optional[int]
    '''thumb_height: Thumbnail height'''
    thumb_height: Optional[int]

@dataclass
class InlineQueryResultPhoto:
    '''type: Type of the result, must be photo'''
    type: str
    '''id: Unique identifier for this result, 1-64 bytes'''
    id: str
    '''photo_url: A valid URL of the photo. Photo must be in jpeg format. Photo size must not exceed 5MB'''
    photo_url: str
    '''thumb_url: URL of the thumbnail for the photo'''
    thumb_url: str
    '''photo_width: Width of the photo'''
    photo_width: Optional[int]
    '''photo_height: Height of the photo'''
    photo_height: Optional[int]
    '''title: Title for the result'''
    title: Optional[str]
    '''description: Short description of the result'''
    description: Optional[str]
    '''caption: Caption of the photo to be sent, 0-1024 characters after entities parsing'''
    caption: Optional[str]
    '''parse_mode: Mode for parsing entities in the photo caption. See formatting options for more details.'''
    parse_mode: Optional[str]
    '''reply_markup: Inline keyboard attached to the message'''
    reply_markup: Optional[InlineKeyboardMarkup]
    '''input_message_content: Content of the message to be sent instead of the photo'''
    input_message_content: Optional[InputMessageContent]

@dataclass
class InlineQueryResultGif:
    '''type: Type of the result, must be gif'''
    type: str
    '''id: Unique identifier for this result, 1-64 bytes'''
    id: str
    '''gif_url: A valid URL for the GIF file. File size must not exceed 1MB'''
    gif_url: str
    '''gif_width: Width of the GIF'''
    gif_width: Optional[int]
    '''gif_height: Height of the GIF'''
    gif_height: Optional[int]
    '''gif_duration: Duration of the GIF'''
    gif_duration: Optional[int]
    '''thumb_url: URL of the static (JPEG or GIF) or animated (MPEG4) thumbnail for the result'''
    thumb_url: str
    '''thumb_mime_type: MIME type of the thumbnail, must be one of “image/jpeg”, “image/gif”, or “video/mp4”. Defaults to “image/jpeg”'''
    thumb_mime_type: Optional[str]
    '''title: Title for the result'''
    title: Optional[str]
    '''caption: Caption of the GIF file to be sent, 0-1024 characters after entities parsing'''
    caption: Optional[str]
    '''parse_mode: Mode for parsing entities in the caption. See formatting options for more details.'''
    parse_mode: Optional[str]
    '''reply_markup: Inline keyboard attached to the message'''
    reply_markup: Optional[InlineKeyboardMarkup]
    '''input_message_content: Content of the message to be sent instead of the GIF animation'''
    input_message_content: Optional[InputMessageContent]

@dataclass
class InlineQueryResultMpeg4Gif:
    '''type: Type of the result, must be mpeg4_gif'''
    type: str
    '''id: Unique identifier for this result, 1-64 bytes'''
    id: str
    '''mpeg4_url: A valid URL for the MP4 file. File size must not exceed 1MB'''
    mpeg4_url: str
    '''mpeg4_width: Video width'''
    mpeg4_width: Optional[int]
    '''mpeg4_height: Video height'''
    mpeg4_height: Optional[int]
    '''mpeg4_duration: Video duration'''
    mpeg4_duration: Optional[int]
    '''thumb_url: URL of the static (JPEG or GIF) or animated (MPEG4) thumbnail for the result'''
    thumb_url: str
    '''thumb_mime_type: MIME type of the thumbnail, must be one of “image/jpeg”, “image/gif”, or “video/mp4”. Defaults to “image/jpeg”'''
    thumb_mime_type: Optional[str]
    '''title: Title for the result'''
    title: Optional[str]
    '''caption: Caption of the MPEG-4 file to be sent, 0-1024 characters after entities parsing'''
    caption: Optional[str]
    '''parse_mode: Mode for parsing entities in the caption. See formatting options for more details.'''
    parse_mode: Optional[str]
    '''reply_markup: Inline keyboard attached to the message'''
    reply_markup: Optional[InlineKeyboardMarkup]
    '''input_message_content: Content of the message to be sent instead of the video animation'''
    input_message_content: Optional[InputMessageContent]

@dataclass
class InlineQueryResultVideo:
    '''type: Type of the result, must be video'''
    type: str
    '''id: Unique identifier for this result, 1-64 bytes'''
    id: str
    '''video_url: A valid URL for the embedded video player or video file'''
    video_url: str
    '''mime_type: Mime type of the content of video url, “text/html” or “video/mp4”'''
    mime_type: str
    '''thumb_url: URL of the thumbnail (jpeg only) for the video'''
    thumb_url: str
    '''title: Title for the result'''
    title: str
    '''caption: Caption of the video to be sent, 0-1024 characters after entities parsing'''
    caption: Optional[str]
    '''parse_mode: Mode for parsing entities in the video caption. See formatting options for more details.'''
    parse_mode: Optional[str]
    '''video_width: Video width'''
    video_width: Optional[int]
    '''video_height: Video height'''
    video_height: Optional[int]
    '''video_duration: Video duration in seconds'''
    video_duration: Optional[int]
    '''description: Short description of the result'''
    description: Optional[str]
    '''reply_markup: Inline keyboard attached to the message'''
    reply_markup: Optional[InlineKeyboardMarkup]
    '''input_message_content: Content of the message to be sent instead of the video. This field is required if InlineQueryResultVideo is used to send an HTML-page as a result (e.g., a YouTube video).'''
    input_message_content: Optional[InputMessageContent]

@dataclass
class InlineQueryResultAudio:
    '''type: Type of the result, must be audio'''
    type: str
    '''id: Unique identifier for this result, 1-64 bytes'''
    id: str
    '''audio_url: A valid URL for the audio file'''
    audio_url: str
    '''title: Title'''
    title: str
    '''caption: Caption, 0-1024 characters after entities parsing'''
    caption: Optional[str]
    '''parse_mode: Mode for parsing entities in the audio caption. See formatting options for more details.'''
    parse_mode: Optional[str]
    '''performer: Performer'''
    performer: Optional[str]
    '''audio_duration: Audio duration in seconds'''
    audio_duration: Optional[int]
    '''reply_markup: Inline keyboard attached to the message'''
    reply_markup: Optional[InlineKeyboardMarkup]
    '''input_message_content: Content of the message to be sent instead of the audio'''
    input_message_content: Optional[InputMessageContent]

@dataclass
class InlineQueryResultVoice:
    '''type: Type of the result, must be voice'''
    type: str
    '''id: Unique identifier for this result, 1-64 bytes'''
    id: str
    '''voice_url: A valid URL for the voice recording'''
    voice_url: str
    '''title: Recording title'''
    title: str
    '''caption: Caption, 0-1024 characters after entities parsing'''
    caption: Optional[str]
    '''parse_mode: Mode for parsing entities in the voice message caption. See formatting options for more details.'''
    parse_mode: Optional[str]
    '''voice_duration: Recording duration in seconds'''
    voice_duration: Optional[int]
    '''reply_markup: Inline keyboard attached to the message'''
    reply_markup: Optional[InlineKeyboardMarkup]
    '''input_message_content: Content of the message to be sent instead of the voice recording'''
    input_message_content: Optional[InputMessageContent]

@dataclass
class InlineQueryResultDocument:
    '''type: Type of the result, must be document'''
    type: str
    '''id: Unique identifier for this result, 1-64 bytes'''
    id: str
    '''title: Title for the result'''
    title: str
    '''caption: Caption of the document to be sent, 0-1024 characters after entities parsing'''
    caption: Optional[str]
    '''parse_mode: Mode for parsing entities in the document caption. See formatting options for more details.'''
    parse_mode: Optional[str]
    '''document_url: A valid URL for the file'''
    document_url: str
    '''mime_type: Mime type of the content of the file, either “application/pdf” or “application/zip”'''
    mime_type: str
    '''description: Short description of the result'''
    description: Optional[str]
    '''reply_markup: Inline keyboard attached to the message'''
    reply_markup: Optional[InlineKeyboardMarkup]
    '''input_message_content: Content of the message to be sent instead of the file'''
    input_message_content: Optional[InputMessageContent]
    '''thumb_url: URL of the thumbnail (jpeg only) for the file'''
    thumb_url: Optional[str]
    '''thumb_width: Thumbnail width'''
    thumb_width: Optional[int]
    '''thumb_height: Thumbnail height'''
    thumb_height: Optional[int]

@dataclass
class InlineQueryResultLocation:
    '''type: Type of the result, must be location'''
    type: str
    '''id: Unique identifier for this result, 1-64 Bytes'''
    id: str
    '''latitude: Location latitude in degrees'''
    latitude: float
    '''longitude: Location longitude in degrees'''
    longitude: float
    '''title: Location title'''
    title: str
    '''live_period: Period in seconds for which the location can be updated, should be between 60 and 86400.'''
    live_period: Optional[int]
    '''reply_markup: Inline keyboard attached to the message'''
    reply_markup: Optional[InlineKeyboardMarkup]
    '''input_message_content: Content of the message to be sent instead of the location'''
    input_message_content: Optional[InputMessageContent]
    '''thumb_url: Url of the thumbnail for the result'''
    thumb_url: Optional[str]
    '''thumb_width: Thumbnail width'''
    thumb_width: Optional[int]
    '''thumb_height: Thumbnail height'''
    thumb_height: Optional[int]

@dataclass
class InlineQueryResultVenue:
    '''type: Type of the result, must be venue'''
    type: str
    '''id: Unique identifier for this result, 1-64 Bytes'''
    id: str
    '''latitude: Latitude of the venue location in degrees'''
    latitude: float
    '''longitude: Longitude of the venue location in degrees'''
    longitude: float
    '''title: Title of the venue'''
    title: str
    '''address: Address of the venue'''
    address: str
    '''foursquare_id: Foursquare identifier of the venue if known'''
    foursquare_id: Optional[str]
    '''foursquare_type: Foursquare type of the venue, if known. (For example, “arts_entertainment/default”, “arts_entertainment/aquarium” or “food/icecream”.)'''
    foursquare_type: Optional[str]
    '''reply_markup: Inline keyboard attached to the message'''
    reply_markup: Optional[InlineKeyboardMarkup]
    '''input_message_content: Content of the message to be sent instead of the venue'''
    input_message_content: Optional[InputMessageContent]
    '''thumb_url: Url of the thumbnail for the result'''
    thumb_url: Optional[str]
    '''thumb_width: Thumbnail width'''
    thumb_width: Optional[int]
    '''thumb_height: Thumbnail height'''
    thumb_height: Optional[int]

@dataclass
class InlineQueryResultContact:
    '''type: Type of the result, must be contact'''
    type: str
    '''id: Unique identifier for this result, 1-64 Bytes'''
    id: str
    '''phone_number: Contact's phone number'''
    phone_number: str
    '''first_name: Contact's first name'''
    first_name: str
    '''last_name: Contact's last name'''
    last_name: Optional[str]
    '''vcard: Additional data about the contact in the form of a vCard, 0-2048 bytes'''
    vcard: Optional[str]
    '''reply_markup: Inline keyboard attached to the message'''
    reply_markup: Optional[InlineKeyboardMarkup]
    '''input_message_content: Content of the message to be sent instead of the contact'''
    input_message_content: Optional[InputMessageContent]
    '''thumb_url: Url of the thumbnail for the result'''
    thumb_url: Optional[str]
    '''thumb_width: Thumbnail width'''
    thumb_width: Optional[int]
    '''thumb_height: Thumbnail height'''
    thumb_height: Optional[int]

@dataclass
class InlineQueryResultGame:
    '''type: Type of the result, must be game'''
    type: str
    '''id: Unique identifier for this result, 1-64 bytes'''
    id: str
    '''game_short_name: Short name of the game'''
    game_short_name: str
    '''reply_markup: Inline keyboard attached to the message'''
    reply_markup: Optional[InlineKeyboardMarkup]

@dataclass
class InlineQueryResultCachedPhoto:
    '''type: Type of the result, must be photo'''
    type: str
    '''id: Unique identifier for this result, 1-64 bytes'''
    id: str
    '''photo_file_id: A valid file identifier of the photo'''
    photo_file_id: str
    '''title: Title for the result'''
    title: Optional[str]
    '''description: Short description of the result'''
    description: Optional[str]
    '''caption: Caption of the photo to be sent, 0-1024 characters after entities parsing'''
    caption: Optional[str]
    '''parse_mode: Mode for parsing entities in the photo caption. See formatting options for more details.'''
    parse_mode: Optional[str]
    '''reply_markup: Inline keyboard attached to the message'''
    reply_markup: Optional[InlineKeyboardMarkup]
    '''input_message_content: Content of the message to be sent instead of the photo'''
    input_message_content: Optional[InputMessageContent]

@dataclass
class InlineQueryResultCachedGif:
    '''type: Type of the result, must be gif'''
    type: str
    '''id: Unique identifier for this result, 1-64 bytes'''
    id: str
    '''gif_file_id: A valid file identifier for the GIF file'''
    gif_file_id: str
    '''title: Title for the result'''
    title: Optional[str]
    '''caption: Caption of the GIF file to be sent, 0-1024 characters after entities parsing'''
    caption: Optional[str]
    '''parse_mode: Mode for parsing entities in the caption. See formatting options for more details.'''
    parse_mode: Optional[str]
    '''reply_markup: Inline keyboard attached to the message'''
    reply_markup: Optional[InlineKeyboardMarkup]
    '''input_message_content: Content of the message to be sent instead of the GIF animation'''
    input_message_content: Optional[InputMessageContent]

@dataclass
class InlineQueryResultCachedMpeg4Gif:
    '''type: Type of the result, must be mpeg4_gif'''
    type: str
    '''id: Unique identifier for this result, 1-64 bytes'''
    id: str
    '''mpeg4_file_id: A valid file identifier for the MP4 file'''
    mpeg4_file_id: str
    '''title: Title for the result'''
    title: Optional[str]
    '''caption: Caption of the MPEG-4 file to be sent, 0-1024 characters after entities parsing'''
    caption: Optional[str]
    '''parse_mode: Mode for parsing entities in the caption. See formatting options for more details.'''
    parse_mode: Optional[str]
    '''reply_markup: Inline keyboard attached to the message'''
    reply_markup: Optional[InlineKeyboardMarkup]
    '''input_message_content: Content of the message to be sent instead of the video animation'''
    input_message_content: Optional[InputMessageContent]

@dataclass
class InlineQueryResultCachedSticker:
    '''type: Type of the result, must be sticker'''
    type: str
    '''id: Unique identifier for this result, 1-64 bytes'''
    id: str
    '''sticker_file_id: A valid file identifier of the sticker'''
    sticker_file_id: str
    '''reply_markup: Inline keyboard attached to the message'''
    reply_markup: Optional[InlineKeyboardMarkup]
    '''input_message_content: Content of the message to be sent instead of the sticker'''
    input_message_content: Optional[InputMessageContent]

@dataclass
class InlineQueryResultCachedDocument:
    '''type: Type of the result, must be document'''
    type: str
    '''id: Unique identifier for this result, 1-64 bytes'''
    id: str
    '''title: Title for the result'''
    title: str
    '''document_file_id: A valid file identifier for the file'''
    document_file_id: str
    '''description: Short description of the result'''
    description: Optional[str]
    '''caption: Caption of the document to be sent, 0-1024 characters after entities parsing'''
    caption: Optional[str]
    '''parse_mode: Mode for parsing entities in the document caption. See formatting options for more details.'''
    parse_mode: Optional[str]
    '''reply_markup: Inline keyboard attached to the message'''
    reply_markup: Optional[InlineKeyboardMarkup]
    '''input_message_content: Content of the message to be sent instead of the file'''
    input_message_content: Optional[InputMessageContent]

@dataclass
class InlineQueryResultCachedVideo:
    '''type: Type of the result, must be video'''
    type: str
    '''id: Unique identifier for this result, 1-64 bytes'''
    id: str
    '''video_file_id: A valid file identifier for the video file'''
    video_file_id: str
    '''title: Title for the result'''
    title: str
    '''description: Short description of the result'''
    description: Optional[str]
    '''caption: Caption of the video to be sent, 0-1024 characters after entities parsing'''
    caption: Optional[str]
    '''parse_mode: Mode for parsing entities in the video caption. See formatting options for more details.'''
    parse_mode: Optional[str]
    '''reply_markup: Inline keyboard attached to the message'''
    reply_markup: Optional[InlineKeyboardMarkup]
    '''input_message_content: Content of the message to be sent instead of the video'''
    input_message_content: Optional[InputMessageContent]

@dataclass
class InlineQueryResultCachedVoice:
    '''type: Type of the result, must be voice'''
    type: str
    '''id: Unique identifier for this result, 1-64 bytes'''
    id: str
    '''voice_file_id: A valid file identifier for the voice message'''
    voice_file_id: str
    '''title: Voice message title'''
    title: str
    '''caption: Caption, 0-1024 characters after entities parsing'''
    caption: Optional[str]
    '''parse_mode: Mode for parsing entities in the voice message caption. See formatting options for more details.'''
    parse_mode: Optional[str]
    '''reply_markup: Inline keyboard attached to the message'''
    reply_markup: Optional[InlineKeyboardMarkup]
    '''input_message_content: Content of the message to be sent instead of the voice message'''
    input_message_content: Optional[InputMessageContent]

@dataclass
class InlineQueryResultCachedAudio:
    '''type: Type of the result, must be audio'''
    type: str
    '''id: Unique identifier for this result, 1-64 bytes'''
    id: str
    '''audio_file_id: A valid file identifier for the audio file'''
    audio_file_id: str
    '''caption: Caption, 0-1024 characters after entities parsing'''
    caption: Optional[str]
    '''parse_mode: Mode for parsing entities in the audio caption. See formatting options for more details.'''
    parse_mode: Optional[str]
    '''reply_markup: Inline keyboard attached to the message'''
    reply_markup: Optional[InlineKeyboardMarkup]
    '''input_message_content: Content of the message to be sent instead of the audio'''
    input_message_content: Optional[InputMessageContent]

@dataclass
class InputTextMessageContent:
    '''message_text: Text of the message to be sent, 1-4096 characters'''
    message_text: str
    '''parse_mode: Mode for parsing entities in the message text. See formatting options for more details.'''
    parse_mode: Optional[str]
    '''disable_web_page_preview: Disables link previews for links in the sent message'''
    disable_web_page_preview: Optional[bool]

@dataclass
class InputLocationMessageContent:
    '''latitude: Latitude of the location in degrees'''
    latitude: float
    '''longitude: Longitude of the location in degrees'''
    longitude: float
    '''live_period: Period in seconds for which the location can be updated, should be between 60 and 86400.'''
    live_period: Optional[int]

@dataclass
class InputVenueMessageContent:
    '''latitude: Latitude of the venue in degrees'''
    latitude: float
    '''longitude: Longitude of the venue in degrees'''
    longitude: float
    '''title: Name of the venue'''
    title: str
    '''address: Address of the venue'''
    address: str
    '''foursquare_id: Foursquare identifier of the venue, if known'''
    foursquare_id: Optional[str]
    '''foursquare_type: Foursquare type of the venue, if known. (For example, “arts_entertainment/default”, “arts_entertainment/aquarium” or “food/icecream”.)'''
    foursquare_type: Optional[str]

@dataclass
class InputContactMessageContent:
    '''phone_number: Contact's phone number'''
    phone_number: str
    '''first_name: Contact's first name'''
    first_name: str
    '''last_name: Contact's last name'''
    last_name: Optional[str]
    '''vcard: Additional data about the contact in the form of a vCard, 0-2048 bytes'''
    vcard: Optional[str]

@dataclass
class ChosenInlineResult:
    '''result_id: The unique identifier for the result that was chosen'''
    result_id: str
    '''from_user: The user that chose the result'''
    from_user: User
    '''location: Sender location, only for bots that require user location'''
    location: Optional[Location]
    '''inline_message_id: Identifier of the sent inline message. Available only if there is an inline keyboard attached to the message. Will be also received in callback queries and can be used to edit the message.'''
    inline_message_id: Optional[str]
    '''query: The query that was used to obtain the result'''
    query: str

@dataclass
class LabeledPrice:
    '''label: Portion label'''
    label: str
    '''amount: Price of the product in the smallest units of the currency (integer, not float/double). For example, for a price of US$ 1.45 pass amount = 145 . See the exp parameter in currencies.json, it shows the number of digits past the decimal point for each currency (2 for the majority of currencies).'''
    amount: int

@dataclass
class Invoice:
    '''title: Product name'''
    title: str
    '''description: Product description'''
    description: str
    '''start_parameter: Unique bot deep-linking parameter that can be used to generate this invoice'''
    start_parameter: str
    '''currency: Three-letter ISO 4217 currency code'''
    currency: str
    '''total_amount: Total price in the smallest units of the currency (integer, not float/double). For example, for a price of US$ 1.45 pass amount = 145 . See the exp parameter in currencies.json, it shows the number of digits past the decimal point for each currency (2 for the majority of currencies).'''
    total_amount: int

@dataclass
class ShippingAddress:
    '''country_code: ISO 3166-1 alpha-2 country code'''
    country_code: str
    '''state: State, if applicable'''
    state: str
    '''city: City'''
    city: str
    '''street_line1: First line for the address'''
    street_line1: str
    '''street_line2: Second line for the address'''
    street_line2: str
    '''post_code: Address post code'''
    post_code: str

@dataclass
class OrderInfo:
    '''name: User name'''
    name: Optional[str]
    '''phone_number: User's phone number'''
    phone_number: Optional[str]
    '''email: User email'''
    email: Optional[str]
    '''shipping_address: User shipping address'''
    shipping_address: Optional[ShippingAddress]

@dataclass
class ShippingOption:
    '''id: Shipping option identifier'''
    id: str
    '''title: Option title'''
    title: str
    '''prices: List of price portions'''
    prices: List[LabeledPrice]

@dataclass
class SuccessfulPayment:
    '''currency: Three-letter ISO 4217 currency code'''
    currency: str
    '''total_amount: Total price in the smallest units of the currency (integer, not float/double). For example, for a price of US$ 1.45 pass amount = 145 . See the exp parameter in currencies.json, it shows the number of digits past the decimal point for each currency (2 for the majority of currencies).'''
    total_amount: int
    '''invoice_payload: Bot specified invoice payload'''
    invoice_payload: str
    '''shipping_option_id: Identifier of the shipping option chosen by the user'''
    shipping_option_id: Optional[str]
    '''order_info: Order info provided by the user'''
    order_info: Optional[OrderInfo]
    '''telegram_payment_charge_id: Telegram payment identifier'''
    telegram_payment_charge_id: str
    '''provider_payment_charge_id: Provider payment identifier'''
    provider_payment_charge_id: str

@dataclass
class ShippingQuery:
    '''id: Unique query identifier'''
    id: str
    '''from_user: User who sent the query'''
    from_user: User
    '''invoice_payload: Bot specified invoice payload'''
    invoice_payload: str
    '''shipping_address: User specified shipping address'''
    shipping_address: ShippingAddress

@dataclass
class PreCheckoutQuery:
    '''id: Unique query identifier'''
    id: str
    '''from_user: User who sent the query'''
    from_user: User
    '''currency: Three-letter ISO 4217 currency code'''
    currency: str
    '''total_amount: Total price in the smallest units of the currency (integer, not float/double). For example, for a price of US$ 1.45 pass amount = 145 . See the exp parameter in currencies.json, it shows the number of digits past the decimal point for each currency (2 for the majority of currencies).'''
    total_amount: int
    '''invoice_payload: Bot specified invoice payload'''
    invoice_payload: str
    '''shipping_option_id: Identifier of the shipping option chosen by the user'''
    shipping_option_id: Optional[str]
    '''order_info: Order info provided by the user'''
    order_info: Optional[OrderInfo]

@dataclass
class PassportData:
    '''data: Array with information about documents and other Telegram Passport elements that was shared with the bot'''
    data: List['EncryptedPassportElement']
    '''credentials: Encrypted credentials required to decrypt the data'''
    credentials: 'EncryptedCredentials'

@dataclass
class PassportFile:
    '''file_id: Identifier for this file, which can be used to download or reuse the file'''
    file_id: str
    '''file_unique_id: Unique identifier for this file, which is supposed to be the same over time and for different bots. Can't be used to download or reuse the file.'''
    file_unique_id: str
    '''file_size: File size'''
    file_size: int
    '''file_date: Unix time when the file was uploaded'''
    file_date: int

@dataclass
class EncryptedPassportElement:
    '''type: Element type. One of “personal_details”, “passport”, “driver_license”, “identity_card”, “internal_passport”, “address”, “utility_bill”, “bank_statement”, “rental_agreement”, “passport_registration”, “temporary_registration”, “phone_number”, “email”.'''
    type: str
    '''data: Base64-encoded encrypted Telegram Passport element data provided by the user, available for “personal_details”, “passport”, “driver_license”, “identity_card”, “internal_passport” and “address” types. Can be decrypted and verified using the accompanying EncryptedCredentials .'''
    data: Optional[str]
    '''phone_number: User's verified phone number, available only for “phone_number” type'''
    phone_number: Optional[str]
    '''email: User's verified email address, available only for “email” type'''
    email: Optional[str]
    '''files: Array of encrypted files with documents provided by the user, available for “utility_bill”, “bank_statement”, “rental_agreement”, “passport_registration” and “temporary_registration” types. Files can be decrypted and verified using the accompanying EncryptedCredentials .'''
    files: Optional[List[PassportFile]]
    '''front_side: Encrypted file with the front side of the document, provided by the user. Available for “passport”, “driver_license”, “identity_card” and “internal_passport”. The file can be decrypted and verified using the accompanying EncryptedCredentials .'''
    front_side: Optional[PassportFile]
    '''reverse_side: Encrypted file with the reverse side of the document, provided by the user. Available for “driver_license” and “identity_card”. The file can be decrypted and verified using the accompanying EncryptedCredentials .'''
    reverse_side: Optional[PassportFile]
    '''selfie: Encrypted file with the selfie of the user holding a document, provided by the user; available for “passport”, “driver_license”, “identity_card” and “internal_passport”. The file can be decrypted and verified using the accompanying EncryptedCredentials .'''
    selfie: Optional[PassportFile]
    '''translation: Array of encrypted files with translated versions of documents provided by the user. Available if requested for “passport”, “driver_license”, “identity_card”, “internal_passport”, “utility_bill”, “bank_statement”, “rental_agreement”, “passport_registration” and “temporary_registration” types. Files can be decrypted and verified using the accompanying EncryptedCredentials .'''
    translation: Optional[List[PassportFile]]
    '''hash: Base64-encoded element hash for using in PassportElementErrorUnspecified'''
    hash: str

@dataclass
class EncryptedCredentials:
    '''data: Base64-encoded encrypted JSON-serialized data with unique user's payload, data hashes and secrets required for EncryptedPassportElement decryption and authentication'''
    data: str
    '''hash: Base64-encoded data hash for data authentication'''
    hash: str
    '''secret: Base64-encoded secret, encrypted with the bot's public RSA key, required for data decryption'''
    secret: str

@dataclass
class PassportElementErrorDataField:
    '''source: Error source, must be data'''
    source: str
    '''type: The section of the user's Telegram Passport which has the error, one of “personal_details”, “passport”, “driver_license”, “identity_card”, “internal_passport”, “address”'''
    type: str
    '''field_name: Name of the data field which has the error'''
    field_name: str
    '''data_hash: Base64-encoded data hash'''
    data_hash: str
    '''message: Error message'''
    message: str

@dataclass
class PassportElementErrorFrontSide:
    '''source: Error source, must be front_side'''
    source: str
    '''type: The section of the user's Telegram Passport which has the issue, one of “passport”, “driver_license”, “identity_card”, “internal_passport”'''
    type: str
    '''file_hash: Base64-encoded hash of the file with the front side of the document'''
    file_hash: str
    '''message: Error message'''
    message: str

@dataclass
class PassportElementErrorReverseSide:
    '''source: Error source, must be reverse_side'''
    source: str
    '''type: The section of the user's Telegram Passport which has the issue, one of “driver_license”, “identity_card”'''
    type: str
    '''file_hash: Base64-encoded hash of the file with the reverse side of the document'''
    file_hash: str
    '''message: Error message'''
    message: str

@dataclass
class PassportElementErrorSelfie:
    '''source: Error source, must be selfie'''
    source: str
    '''type: The section of the user's Telegram Passport which has the issue, one of “passport”, “driver_license”, “identity_card”, “internal_passport”'''
    type: str
    '''file_hash: Base64-encoded hash of the file with the selfie'''
    file_hash: str
    '''message: Error message'''
    message: str

@dataclass
class PassportElementErrorFile:
    '''source: Error source, must be file'''
    source: str
    '''type: The section of the user's Telegram Passport which has the issue, one of “utility_bill”, “bank_statement”, “rental_agreement”, “passport_registration”, “temporary_registration”'''
    type: str
    '''file_hash: Base64-encoded file hash'''
    file_hash: str
    '''message: Error message'''
    message: str

@dataclass
class PassportElementErrorFiles:
    '''source: Error source, must be files'''
    source: str
    '''type: The section of the user's Telegram Passport which has the issue, one of “utility_bill”, “bank_statement”, “rental_agreement”, “passport_registration”, “temporary_registration”'''
    type: str
    '''file_hashes: List of base64-encoded file hashes'''
    file_hashes: List[str]
    '''message: Error message'''
    message: str

@dataclass
class PassportElementErrorTranslationFile:
    '''source: Error source, must be translation_file'''
    source: str
    '''type: Type of element of the user's Telegram Passport which has the issue, one of “passport”, “driver_license”, “identity_card”, “internal_passport”, “utility_bill”, “bank_statement”, “rental_agreement”, “passport_registration”, “temporary_registration”'''
    type: str
    '''file_hash: Base64-encoded file hash'''
    file_hash: str
    '''message: Error message'''
    message: str

@dataclass
class PassportElementErrorTranslationFiles:
    '''source: Error source, must be translation_files'''
    source: str
    '''type: Type of element of the user's Telegram Passport which has the issue, one of “passport”, “driver_license”, “identity_card”, “internal_passport”, “utility_bill”, “bank_statement”, “rental_agreement”, “passport_registration”, “temporary_registration”'''
    type: str
    '''file_hashes: List of base64-encoded file hashes'''
    file_hashes: List[str]
    '''message: Error message'''
    message: str

@dataclass
class PassportElementErrorUnspecified:
    '''source: Error source, must be unspecified'''
    source: str
    '''type: Type of element of the user's Telegram Passport which has the issue'''
    type: str
    '''element_hash: Base64-encoded element hash'''
    element_hash: str
    '''message: Error message'''
    message: str

@dataclass
class Game:
    '''title: Title of the game'''
    title: str
    '''description: Description of the game'''
    description: str
    '''photo: Photo that will be displayed in the game message in chats.'''
    photo: List[PhotoSize]
    '''text: Brief description of the game or high scores included in the game message. Can be automatically edited to include current high scores for the game when the bot calls setGameScore, or manually edited using editMessageText . 0-4096 characters.'''
    text: Optional[str]
    '''text_entities: Special entities that appear in text, such as usernames, URLs, bot commands, etc.'''
    text_entities: Optional[List[MessageEntity]]
    '''animation: Animation that will be displayed in the game message in chats. Upload via BotFather'''
    animation: Optional[Animation]

@dataclass
class GameHighScore:
    '''position: Position in high score table for the game'''
    position: int
    '''user: User'''
    user: User
    '''score: Score'''
    score: int

@dataclass
class getUpdates:
    '''offset: Identifier of the first update to be returned. Must be greater by one than the highest among the identifiers of previously received updates. By default, updates starting with the earliest unconfirmed update are returned. An update is considered confirmed as soon as getUpdates is called with an offset higher than its update_id . The negative offset can be specified to retrieve updates starting from -offset update from the end of the updates queue. All previous updates will forgotten.'''
    offset: Optional[int]
    '''limit: Limits the number of updates to be retrieved. Values between 1-100 are accepted. Defaults to 100.'''
    limit: Optional[int]
    '''timeout: Timeout in seconds for long polling. Defaults to 0, i.e. usual short polling. Should be positive, short polling should be used for testing purposes only.'''
    timeout: Optional[int]
    '''allowed_updates: A JSON-serialized list of the update types you want your bot to receive. For example, specify [“message”, “edited_channel_post”, “callback_query”] to only receive updates of these types. See Update for a complete list of available update types. Specify an empty list to receive all updates regardless of type (default). If not specified, the previous setting will be used. Please note that this parameter doesn't affect updates created before the call to the getUpdates, so unwanted updates may be received for a short period of time.'''
    allowed_updates: Optional[List[str]]

@dataclass
class setWebhook:
    '''url: HTTPS url to send updates to. Use an empty string to remove webhook integration'''
    url: str
    '''certificate: Upload your public key certificate so that the root certificate in use can be checked. See our self-signed guide for details.'''
    certificate: Optional[InputFile]
    '''max_connections: Maximum allowed number of simultaneous HTTPS connections to the webhook for update delivery, 1-100. Defaults to 40 . Use lower values to limit the load on your bot's server, and higher values to increase your bot's throughput.'''
    max_connections: Optional[int]
    '''allowed_updates: A JSON-serialized list of the update types you want your bot to receive. For example, specify [“message”, “edited_channel_post”, “callback_query”] to only receive updates of these types. See Update for a complete list of available update types. Specify an empty list to receive all updates regardless of type (default). If not specified, the previous setting will be used. Please note that this parameter doesn't affect updates created before the call to the setWebhook, so unwanted updates may be received for a short period of time.'''
    allowed_updates: Optional[List[str]]

@dataclass
class sendMessage:
    '''chat_id: Unique identifier for the target chat or username of the target channel (in the format @channelusername )'''
    chat_id: Union[int, str]
    '''text: Text of the message to be sent, 1-4096 characters after entities parsing'''
    text: str
    '''parse_mode: Mode for parsing entities in the message text. See formatting options for more details.'''
    parse_mode: Optional[str]
    '''disable_web_page_preview: Disables link previews for links in this message'''
    disable_web_page_preview: Optional[bool]
    '''disable_notification: Sends the message silently . Users will receive a notification with no sound.'''
    disable_notification: Optional[bool]
    '''reply_to_message_id: If the message is a reply, ID of the original message'''
    reply_to_message_id: Optional[int]
    '''reply_markup: Additional interface options. A JSON-serialized object for an inline keyboard, custom reply keyboard, instructions to remove reply keyboard or to force a reply from the user.'''
    reply_markup: Optional[Union[InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply]]

@dataclass
class forwardMessage:
    '''chat_id: Unique identifier for the target chat or username of the target channel (in the format @channelusername )'''
    chat_id: Union[int, str]
    '''from_chat_id: Unique identifier for the chat where the original message was sent (or channel username in the format @channelusername )'''
    from_chat_id: Union[int, str]
    '''disable_notification: Sends the message silently . Users will receive a notification with no sound.'''
    disable_notification: Optional[bool]
    '''message_id: Message identifier in the chat specified in from_chat_id'''
    message_id: int

@dataclass
class sendPhoto:
    '''chat_id: Unique identifier for the target chat or username of the target channel (in the format @channelusername )'''
    chat_id: Union[int, str]
    '''photo: Photo to send. Pass a file_id as String to send a photo that exists on the Telegram servers (recommended), pass an HTTP URL as a String for Telegram to get a photo from the Internet, or upload a new photo using multipart/form-data. More info on Sending Files »'''
    photo: Union[InputFile, str]
    '''caption: Photo caption (may also be used when resending photos by file_id ), 0-1024 characters after entities parsing'''
    caption: Optional[str]
    '''parse_mode: Mode for parsing entities in the photo caption. See formatting options for more details.'''
    parse_mode: Optional[str]
    '''disable_notification: Sends the message silently . Users will receive a notification with no sound.'''
    disable_notification: Optional[bool]
    '''reply_to_message_id: If the message is a reply, ID of the original message'''
    reply_to_message_id: Optional[int]
    '''reply_markup: Additional interface options. A JSON-serialized object for an inline keyboard, custom reply keyboard, instructions to remove reply keyboard or to force a reply from the user.'''
    reply_markup: Optional[Union[InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply]]

@dataclass
class sendAudio:
    '''chat_id: Unique identifier for the target chat or username of the target channel (in the format @channelusername )'''
    chat_id: Union[int, str]
    '''audio: Audio file to send. Pass a file_id as String to send an audio file that exists on the Telegram servers (recommended), pass an HTTP URL as a String for Telegram to get an audio file from the Internet, or upload a new one using multipart/form-data. More info on Sending Files »'''
    audio: Union[InputFile, str]
    '''caption: Audio caption, 0-1024 characters after entities parsing'''
    caption: Optional[str]
    '''parse_mode: Mode for parsing entities in the audio caption. See formatting options for more details.'''
    parse_mode: Optional[str]
    '''duration: Duration of the audio in seconds'''
    duration: Optional[int]
    '''performer: Performer'''
    performer: Optional[str]
    '''title: Track name'''
    title: Optional[str]
    '''thumb: Thumbnail of the file sent; can be ignored if thumbnail generation for the file is supported server-side. The thumbnail should be in JPEG format and less than 200 kB in size. A thumbnail's width and height should not exceed 320. Ignored if the file is not uploaded using multipart/form-data. Thumbnails can't be reused and can be only uploaded as a new file, so you can pass “attach://<file_attach_name>” if the thumbnail was uploaded using multipart/form-data under <file_attach_name>. More info on Sending Files »'''
    thumb: Optional[Union[InputFile, str]]
    '''disable_notification: Sends the message silently . Users will receive a notification with no sound.'''
    disable_notification: Optional[bool]
    '''reply_to_message_id: If the message is a reply, ID of the original message'''
    reply_to_message_id: Optional[int]
    '''reply_markup: Additional interface options. A JSON-serialized object for an inline keyboard, custom reply keyboard, instructions to remove reply keyboard or to force a reply from the user.'''
    reply_markup: Optional[Union[InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply]]

@dataclass
class sendDocument:
    '''chat_id: Unique identifier for the target chat or username of the target channel (in the format @channelusername )'''
    chat_id: Union[int, str]
    '''document: File to send. Pass a file_id as String to send a file that exists on the Telegram servers (recommended), pass an HTTP URL as a String for Telegram to get a file from the Internet, or upload a new one using multipart/form-data. More info on Sending Files »'''
    document: Union[InputFile, str]
    '''thumb: Thumbnail of the file sent; can be ignored if thumbnail generation for the file is supported server-side. The thumbnail should be in JPEG format and less than 200 kB in size. A thumbnail's width and height should not exceed 320. Ignored if the file is not uploaded using multipart/form-data. Thumbnails can't be reused and can be only uploaded as a new file, so you can pass “attach://<file_attach_name>” if the thumbnail was uploaded using multipart/form-data under <file_attach_name>. More info on Sending Files »'''
    thumb: Optional[Union[InputFile, str]]
    '''caption: Document caption (may also be used when resending documents by file_id ), 0-1024 characters after entities parsing'''
    caption: Optional[str]
    '''parse_mode: Mode for parsing entities in the document caption. See formatting options for more details.'''
    parse_mode: Optional[str]
    '''disable_notification: Sends the message silently . Users will receive a notification with no sound.'''
    disable_notification: Optional[bool]
    '''reply_to_message_id: If the message is a reply, ID of the original message'''
    reply_to_message_id: Optional[int]
    '''reply_markup: Additional interface options. A JSON-serialized object for an inline keyboard, custom reply keyboard, instructions to remove reply keyboard or to force a reply from the user.'''
    reply_markup: Optional[Union[InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply]]

@dataclass
class sendVideo:
    '''chat_id: Unique identifier for the target chat or username of the target channel (in the format @channelusername )'''
    chat_id: Union[int, str]
    '''video: Video to send. Pass a file_id as String to send a video that exists on the Telegram servers (recommended), pass an HTTP URL as a String for Telegram to get a video from the Internet, or upload a new video using multipart/form-data. More info on Sending Files »'''
    video: Union[InputFile, str]
    '''duration: Duration of sent video in seconds'''
    duration: Optional[int]
    '''width: Video width'''
    width: Optional[int]
    '''height: Video height'''
    height: Optional[int]
    '''thumb: Thumbnail of the file sent; can be ignored if thumbnail generation for the file is supported server-side. The thumbnail should be in JPEG format and less than 200 kB in size. A thumbnail's width and height should not exceed 320. Ignored if the file is not uploaded using multipart/form-data. Thumbnails can't be reused and can be only uploaded as a new file, so you can pass “attach://<file_attach_name>” if the thumbnail was uploaded using multipart/form-data under <file_attach_name>. More info on Sending Files »'''
    thumb: Optional[Union[InputFile, str]]
    '''caption: Video caption (may also be used when resending videos by file_id ), 0-1024 characters after entities parsing'''
    caption: Optional[str]
    '''parse_mode: Mode for parsing entities in the video caption. See formatting options for more details.'''
    parse_mode: Optional[str]
    '''supports_streaming: Pass True, if the uploaded video is suitable for streaming'''
    supports_streaming: Optional[bool]
    '''disable_notification: Sends the message silently . Users will receive a notification with no sound.'''
    disable_notification: Optional[bool]
    '''reply_to_message_id: If the message is a reply, ID of the original message'''
    reply_to_message_id: Optional[int]
    '''reply_markup: Additional interface options. A JSON-serialized object for an inline keyboard, custom reply keyboard, instructions to remove reply keyboard or to force a reply from the user.'''
    reply_markup: Optional[Union[InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply]]

@dataclass
class sendAnimation:
    '''chat_id: Unique identifier for the target chat or username of the target channel (in the format @channelusername )'''
    chat_id: Union[int, str]
    '''animation: Animation to send. Pass a file_id as String to send an animation that exists on the Telegram servers (recommended), pass an HTTP URL as a String for Telegram to get an animation from the Internet, or upload a new animation using multipart/form-data. More info on Sending Files »'''
    animation: Union[InputFile, str]
    '''duration: Duration of sent animation in seconds'''
    duration: Optional[int]
    '''width: Animation width'''
    width: Optional[int]
    '''height: Animation height'''
    height: Optional[int]
    '''thumb: Thumbnail of the file sent; can be ignored if thumbnail generation for the file is supported server-side. The thumbnail should be in JPEG format and less than 200 kB in size. A thumbnail's width and height should not exceed 320. Ignored if the file is not uploaded using multipart/form-data. Thumbnails can't be reused and can be only uploaded as a new file, so you can pass “attach://<file_attach_name>” if the thumbnail was uploaded using multipart/form-data under <file_attach_name>. More info on Sending Files »'''
    thumb: Optional[Union[InputFile, str]]
    '''caption: Animation caption (may also be used when resending animation by file_id ), 0-1024 characters after entities parsing'''
    caption: Optional[str]
    '''parse_mode: Mode for parsing entities in the animation caption. See formatting options for more details.'''
    parse_mode: Optional[str]
    '''disable_notification: Sends the message silently . Users will receive a notification with no sound.'''
    disable_notification: Optional[bool]
    '''reply_to_message_id: If the message is a reply, ID of the original message'''
    reply_to_message_id: Optional[int]
    '''reply_markup: Additional interface options. A JSON-serialized object for an inline keyboard, custom reply keyboard, instructions to remove reply keyboard or to force a reply from the user.'''
    reply_markup: Optional[Union[InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply]]

@dataclass
class sendVoice:
    '''chat_id: Unique identifier for the target chat or username of the target channel (in the format @channelusername )'''
    chat_id: Union[int, str]
    '''voice: Audio file to send. Pass a file_id as String to send a file that exists on the Telegram servers (recommended), pass an HTTP URL as a String for Telegram to get a file from the Internet, or upload a new one using multipart/form-data. More info on Sending Files »'''
    voice: Union[InputFile, str]
    '''caption: Voice message caption, 0-1024 characters after entities parsing'''
    caption: Optional[str]
    '''parse_mode: Mode for parsing entities in the voice message caption. See formatting options for more details.'''
    parse_mode: Optional[str]
    '''duration: Duration of the voice message in seconds'''
    duration: Optional[int]
    '''disable_notification: Sends the message silently . Users will receive a notification with no sound.'''
    disable_notification: Optional[bool]
    '''reply_to_message_id: If the message is a reply, ID of the original message'''
    reply_to_message_id: Optional[int]
    '''reply_markup: Additional interface options. A JSON-serialized object for an inline keyboard, custom reply keyboard, instructions to remove reply keyboard or to force a reply from the user.'''
    reply_markup: Optional[Union[InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply]]

@dataclass
class sendVideoNote:
    '''chat_id: Unique identifier for the target chat or username of the target channel (in the format @channelusername )'''
    chat_id: Union[int, str]
    '''video_note: Video note to send. Pass a file_id as String to send a video note that exists on the Telegram servers (recommended) or upload a new video using multipart/form-data. More info on Sending Files » . Sending video notes by a URL is currently unsupported'''
    video_note: Union[InputFile, str]
    '''duration: Duration of sent video in seconds'''
    duration: Optional[int]
    '''length: Video width and height, i.e. diameter of the video message'''
    length: Optional[int]
    '''thumb: Thumbnail of the file sent; can be ignored if thumbnail generation for the file is supported server-side. The thumbnail should be in JPEG format and less than 200 kB in size. A thumbnail's width and height should not exceed 320. Ignored if the file is not uploaded using multipart/form-data. Thumbnails can't be reused and can be only uploaded as a new file, so you can pass “attach://<file_attach_name>” if the thumbnail was uploaded using multipart/form-data under <file_attach_name>. More info on Sending Files »'''
    thumb: Optional[Union[InputFile, str]]
    '''disable_notification: Sends the message silently . Users will receive a notification with no sound.'''
    disable_notification: Optional[bool]
    '''reply_to_message_id: If the message is a reply, ID of the original message'''
    reply_to_message_id: Optional[int]
    '''reply_markup: Additional interface options. A JSON-serialized object for an inline keyboard, custom reply keyboard, instructions to remove reply keyboard or to force a reply from the user.'''
    reply_markup: Optional[Union[InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply]]

@dataclass
class sendMediaGroup:
    '''chat_id: Unique identifier for the target chat or username of the target channel (in the format @channelusername )'''
    chat_id: Union[int, str]
    '''media: A JSON-serialized array describing photos and videos to be sent, must include 2-10 items'''
    media: List[Union[InputMediaPhoto, InputMediaVideo]]
    '''disable_notification: Sends the messages silently . Users will receive a notification with no sound.'''
    disable_notification: Optional[bool]
    '''reply_to_message_id: If the messages are a reply, ID of the original message'''
    reply_to_message_id: Optional[int]

@dataclass
class sendLocation:
    '''chat_id: Unique identifier for the target chat or username of the target channel (in the format @channelusername )'''
    chat_id: Union[int, str]
    '''latitude: Latitude of the location'''
    latitude: float
    '''longitude: Longitude of the location'''
    longitude: float
    '''live_period: Period in seconds for which the location will be updated (see Live Locations, should be between 60 and 86400.'''
    live_period: Optional[int]
    '''disable_notification: Sends the message silently . Users will receive a notification with no sound.'''
    disable_notification: Optional[bool]
    '''reply_to_message_id: If the message is a reply, ID of the original message'''
    reply_to_message_id: Optional[int]
    '''reply_markup: Additional interface options. A JSON-serialized object for an inline keyboard, custom reply keyboard, instructions to remove reply keyboard or to force a reply from the user.'''
    reply_markup: Optional[Union[InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply]]

@dataclass
class editMessageLiveLocation:
    '''chat_id: Required if inline_message_id is not specified. Unique identifier for the target chat or username of the target channel (in the format @channelusername )'''
    chat_id: Optional[Union[int, str]]
    '''message_id: Required if inline_message_id is not specified. Identifier of the message to edit'''
    message_id: Optional[int]
    '''inline_message_id: Required if chat_id and message_id are not specified. Identifier of the inline message'''
    inline_message_id: Optional[str]
    '''latitude: Latitude of new location'''
    latitude: float
    '''longitude: Longitude of new location'''
    longitude: float
    '''reply_markup: A JSON-serialized object for a new inline keyboard .'''
    reply_markup: Optional[InlineKeyboardMarkup]

@dataclass
class stopMessageLiveLocation:
    '''chat_id: Required if inline_message_id is not specified. Unique identifier for the target chat or username of the target channel (in the format @channelusername )'''
    chat_id: Optional[Union[int, str]]
    '''message_id: Required if inline_message_id is not specified. Identifier of the message with live location to stop'''
    message_id: Optional[int]
    '''inline_message_id: Required if chat_id and message_id are not specified. Identifier of the inline message'''
    inline_message_id: Optional[str]
    '''reply_markup: A JSON-serialized object for a new inline keyboard .'''
    reply_markup: Optional[InlineKeyboardMarkup]

@dataclass
class sendVenue:
    '''chat_id: Unique identifier for the target chat or username of the target channel (in the format @channelusername )'''
    chat_id: Union[int, str]
    '''latitude: Latitude of the venue'''
    latitude: float
    '''longitude: Longitude of the venue'''
    longitude: float
    '''title: Name of the venue'''
    title: str
    '''address: Address of the venue'''
    address: str
    '''foursquare_id: Foursquare identifier of the venue'''
    foursquare_id: Optional[str]
    '''foursquare_type: Foursquare type of the venue, if known. (For example, “arts_entertainment/default”, “arts_entertainment/aquarium” or “food/icecream”.)'''
    foursquare_type: Optional[str]
    '''disable_notification: Sends the message silently . Users will receive a notification with no sound.'''
    disable_notification: Optional[bool]
    '''reply_to_message_id: If the message is a reply, ID of the original message'''
    reply_to_message_id: Optional[int]
    '''reply_markup: Additional interface options. A JSON-serialized object for an inline keyboard, custom reply keyboard, instructions to remove reply keyboard or to force a reply from the user.'''
    reply_markup: Optional[Union[InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply]]

@dataclass
class sendContact:
    '''chat_id: Unique identifier for the target chat or username of the target channel (in the format @channelusername )'''
    chat_id: Union[int, str]
    '''phone_number: Contact's phone number'''
    phone_number: str
    '''first_name: Contact's first name'''
    first_name: str
    '''last_name: Contact's last name'''
    last_name: Optional[str]
    '''vcard: Additional data about the contact in the form of a vCard, 0-2048 bytes'''
    vcard: Optional[str]
    '''disable_notification: Sends the message silently . Users will receive a notification with no sound.'''
    disable_notification: Optional[bool]
    '''reply_to_message_id: If the message is a reply, ID of the original message'''
    reply_to_message_id: Optional[int]
    '''reply_markup: Additional interface options. A JSON-serialized object for an inline keyboard, custom reply keyboard, instructions to remove keyboard or to force a reply from the user.'''
    reply_markup: Optional[Union[InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply]]

@dataclass
class sendPoll:
    '''chat_id: Unique identifier for the target chat or username of the target channel (in the format @channelusername )'''
    chat_id: Union[int, str]
    '''question: Poll question, 1-255 characters'''
    question: str
    '''options: A JSON-serialized list of answer options, 2-10 strings 1-100 characters each'''
    options: List[str]
    '''is_anonymous: True, if the poll needs to be anonymous, defaults to True'''
    is_anonymous: Optional[bool]
    '''type: Poll type, “quiz” or “regular”, defaults to “regular”'''
    type: Optional[str]
    '''allows_multiple_answers: True, if the poll allows multiple answers, ignored for polls in quiz mode, defaults to False'''
    allows_multiple_answers: Optional[bool]
    '''correct_option_id: 0-based identifier of the correct answer option, required for polls in quiz mode'''
    correct_option_id: Optional[int]
    '''explanation: Text that is shown when a user chooses an incorrect answer or taps on the lamp icon in a quiz-style poll, 0-200 characters with at most 2 line feeds after entities parsing'''
    explanation: Optional[str]
    '''explanation_parse_mode: Mode for parsing entities in the explanation. See formatting options for more details.'''
    explanation_parse_mode: Optional[str]
    '''open_period: Amount of time in seconds the poll will be active after creation, 5-600. Can't be used together with close_date .'''
    open_period: Optional[int]
    '''close_date: Point in time (Unix timestamp) when the poll will be automatically closed. Must be at least 5 and no more than 600 seconds in the future. Can't be used together with open_period .'''
    close_date: Optional[int]
    '''is_closed: Pass True, if the poll needs to be immediately closed. This can be useful for poll preview.'''
    is_closed: Optional[bool]
    '''disable_notification: Sends the message silently . Users will receive a notification with no sound.'''
    disable_notification: Optional[bool]
    '''reply_to_message_id: If the message is a reply, ID of the original message'''
    reply_to_message_id: Optional[int]
    '''reply_markup: Additional interface options. A JSON-serialized object for an inline keyboard, custom reply keyboard, instructions to remove reply keyboard or to force a reply from the user.'''
    reply_markup: Optional[Union[InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply]]

@dataclass
class sendDice:
    '''chat_id: Unique identifier for the target chat or username of the target channel (in the format @channelusername )'''
    chat_id: Union[int, str]
    '''emoji: Emoji on which the dice throw animation is based. Currently, must be one of “ ”, “ ”, or “ ”. Dice can have values 1-6 for “ ” and “ ”, and values 1-5 for “ ”. Defaults to “ ”'''
    emoji: Optional[str]
    '''disable_notification: Sends the message silently . Users will receive a notification with no sound.'''
    disable_notification: Optional[bool]
    '''reply_to_message_id: If the message is a reply, ID of the original message'''
    reply_to_message_id: Optional[int]
    '''reply_markup: Additional interface options. A JSON-serialized object for an inline keyboard, custom reply keyboard, instructions to remove reply keyboard or to force a reply from the user.'''
    reply_markup: Optional[Union[InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply]]

@dataclass
class sendChatAction:
    '''chat_id: Unique identifier for the target chat or username of the target channel (in the format @channelusername )'''
    chat_id: Union[int, str]
    '''action: Type of action to broadcast. Choose one, depending on what the user is about to receive: typing for text messages, upload_photo for photos, record_video or upload_video for videos, record_audio or upload_audio for audio files, upload_document for general files, find_location for location data, record_video_note or upload_video_note for video notes .'''
    action: str

@dataclass
class getUserProfilePhotos:
    '''user_id: Unique identifier of the target user'''
    user_id: int
    '''offset: Sequential number of the first photo to be returned. By default, all photos are returned.'''
    offset: Optional[int]
    '''limit: Limits the number of photos to be retrieved. Values between 1-100 are accepted. Defaults to 100.'''
    limit: Optional[int]

@dataclass
class getFile:
    '''file_id: File identifier to get info about'''
    file_id: str

@dataclass
class kickChatMember:
    '''chat_id: Unique identifier for the target group or username of the target supergroup or channel (in the format @channelusername )'''
    chat_id: Union[int, str]
    '''user_id: Unique identifier of the target user'''
    user_id: int
    '''until_date: Date when the user will be unbanned, unix time. If user is banned for more than 366 days or less than 30 seconds from the current time they are considered to be banned forever'''
    until_date: Optional[int]

@dataclass
class unbanChatMember:
    '''chat_id: Unique identifier for the target group or username of the target supergroup or channel (in the format @username )'''
    chat_id: Union[int, str]
    '''user_id: Unique identifier of the target user'''
    user_id: int

@dataclass
class restrictChatMember:
    '''chat_id: Unique identifier for the target chat or username of the target supergroup (in the format @supergroupusername )'''
    chat_id: Union[int, str]
    '''user_id: Unique identifier of the target user'''
    user_id: int
    '''permissions: A JSON-serialized object for new user permissions'''
    permissions: ChatPermissions
    '''until_date: Date when restrictions will be lifted for the user, unix time. If user is restricted for more than 366 days or less than 30 seconds from the current time, they are considered to be restricted forever'''
    until_date: Optional[int]

@dataclass
class promoteChatMember:
    '''chat_id: Unique identifier for the target chat or username of the target channel (in the format @channelusername )'''
    chat_id: Union[int, str]
    '''user_id: Unique identifier of the target user'''
    user_id: int
    '''can_change_info: Pass True, if the administrator can change chat title, photo and other settings'''
    can_change_info: Optional[bool]
    '''can_post_messages: Pass True, if the administrator can create channel posts, channels only'''
    can_post_messages: Optional[bool]
    '''can_edit_messages: Pass True, if the administrator can edit messages of other users and can pin messages, channels only'''
    can_edit_messages: Optional[bool]
    '''can_delete_messages: Pass True, if the administrator can delete messages of other users'''
    can_delete_messages: Optional[bool]
    '''can_invite_users: Pass True, if the administrator can invite new users to the chat'''
    can_invite_users: Optional[bool]
    '''can_restrict_members: Pass True, if the administrator can restrict, ban or unban chat members'''
    can_restrict_members: Optional[bool]
    '''can_pin_messages: Pass True, if the administrator can pin messages, supergroups only'''
    can_pin_messages: Optional[bool]
    '''can_promote_members: Pass True, if the administrator can add new administrators with a subset of their own privileges or demote administrators that he has promoted, directly or indirectly (promoted by administrators that were appointed by him)'''
    can_promote_members: Optional[bool]

@dataclass
class setChatAdministratorCustomTitle:
    '''chat_id: Unique identifier for the target chat or username of the target supergroup (in the format @supergroupusername )'''
    chat_id: Union[int, str]
    '''user_id: Unique identifier of the target user'''
    user_id: int
    '''custom_title: New custom title for the administrator; 0-16 characters, emoji are not allowed'''
    custom_title: str

@dataclass
class setChatPermissions:
    '''chat_id: Unique identifier for the target chat or username of the target supergroup (in the format @supergroupusername )'''
    chat_id: Union[int, str]
    '''permissions: New default chat permissions'''
    permissions: ChatPermissions

@dataclass
class exportChatInviteLink:
    '''chat_id: Unique identifier for the target chat or username of the target channel (in the format @channelusername )'''
    chat_id: Union[int, str]

@dataclass
class setChatPhoto:
    '''chat_id: Unique identifier for the target chat or username of the target channel (in the format @channelusername )'''
    chat_id: Union[int, str]
    '''photo: New chat photo, uploaded using multipart/form-data'''
    photo: InputFile

@dataclass
class deleteChatPhoto:
    '''chat_id: Unique identifier for the target chat or username of the target channel (in the format @channelusername )'''
    chat_id: Union[int, str]

@dataclass
class setChatTitle:
    '''chat_id: Unique identifier for the target chat or username of the target channel (in the format @channelusername )'''
    chat_id: Union[int, str]
    '''title: New chat title, 1-255 characters'''
    title: str

@dataclass
class setChatDescription:
    '''chat_id: Unique identifier for the target chat or username of the target channel (in the format @channelusername )'''
    chat_id: Union[int, str]
    '''description: New chat description, 0-255 characters'''
    description: Optional[str]

@dataclass
class pinChatMessage:
    '''chat_id: Unique identifier for the target chat or username of the target channel (in the format @channelusername )'''
    chat_id: Union[int, str]
    '''message_id: Identifier of a message to pin'''
    message_id: int
    '''disable_notification: Pass True, if it is not necessary to send a notification to all chat members about the new pinned message. Notifications are always disabled in channels.'''
    disable_notification: Optional[bool]

@dataclass
class unpinChatMessage:
    '''chat_id: Unique identifier for the target chat or username of the target channel (in the format @channelusername )'''
    chat_id: Union[int, str]

@dataclass
class leaveChat:
    '''chat_id: Unique identifier for the target chat or username of the target supergroup or channel (in the format @channelusername )'''
    chat_id: Union[int, str]

@dataclass
class getChat:
    '''chat_id: Unique identifier for the target chat or username of the target supergroup or channel (in the format @channelusername )'''
    chat_id: Union[int, str]

@dataclass
class getChatAdministrators:
    '''chat_id: Unique identifier for the target chat or username of the target supergroup or channel (in the format @channelusername )'''
    chat_id: Union[int, str]

@dataclass
class getChatMembersCount:
    '''chat_id: Unique identifier for the target chat or username of the target supergroup or channel (in the format @channelusername )'''
    chat_id: Union[int, str]

@dataclass
class getChatMember:
    '''chat_id: Unique identifier for the target chat or username of the target supergroup or channel (in the format @channelusername )'''
    chat_id: Union[int, str]
    '''user_id: Unique identifier of the target user'''
    user_id: int

@dataclass
class setChatStickerSet:
    '''chat_id: Unique identifier for the target chat or username of the target supergroup (in the format @supergroupusername )'''
    chat_id: Union[int, str]
    '''sticker_set_name: Name of the sticker set to be set as the group sticker set'''
    sticker_set_name: str

@dataclass
class deleteChatStickerSet:
    '''chat_id: Unique identifier for the target chat or username of the target supergroup (in the format @supergroupusername )'''
    chat_id: Union[int, str]

@dataclass
class answerCallbackQuery:
    '''callback_query_id: Unique identifier for the query to be answered'''
    callback_query_id: str
    '''text: Text of the notification. If not specified, nothing will be shown to the user, 0-200 characters'''
    text: Optional[str]
    '''show_alert: If true, an alert will be shown by the client instead of a notification at the top of the chat screen. Defaults to false .'''
    show_alert: Optional[bool]
    '''url: URL that will be opened by the user's client. If you have created a Game and accepted the conditions via @Botfather, specify the URL that opens your game — note that this will only work if the query comes from a callback_game button. Otherwise, you may use links like t.me/your_bot?start=XXXX that open your bot with a parameter.'''
    url: Optional[str]
    '''cache_time: The maximum amount of time in seconds that the result of the callback query may be cached client-side. Telegram apps will support caching starting in version 3.14. Defaults to 0.'''
    cache_time: Optional[int]

@dataclass
class setMyCommands:
    '''commands: A JSON-serialized list of bot commands to be set as the list of the bot's commands. At most 100 commands can be specified.'''
    commands: List[BotCommand]

@dataclass
class editMessageText:
    '''chat_id: Required if inline_message_id is not specified. Unique identifier for the target chat or username of the target channel (in the format @channelusername )'''
    chat_id: Optional[Union[int, str]]
    '''message_id: Required if inline_message_id is not specified. Identifier of the message to edit'''
    message_id: Optional[int]
    '''inline_message_id: Required if chat_id and message_id are not specified. Identifier of the inline message'''
    inline_message_id: Optional[str]
    '''text: New text of the message, 1-4096 characters after entities parsing'''
    text: str
    '''parse_mode: Mode for parsing entities in the message text. See formatting options for more details.'''
    parse_mode: Optional[str]
    '''disable_web_page_preview: Disables link previews for links in this message'''
    disable_web_page_preview: Optional[bool]
    '''reply_markup: A JSON-serialized object for an inline keyboard .'''
    reply_markup: Optional[InlineKeyboardMarkup]

@dataclass
class editMessageCaption:
    '''chat_id: Required if inline_message_id is not specified. Unique identifier for the target chat or username of the target channel (in the format @channelusername )'''
    chat_id: Optional[Union[int, str]]
    '''message_id: Required if inline_message_id is not specified. Identifier of the message to edit'''
    message_id: Optional[int]
    '''inline_message_id: Required if chat_id and message_id are not specified. Identifier of the inline message'''
    inline_message_id: Optional[str]
    '''caption: New caption of the message, 0-1024 characters after entities parsing'''
    caption: Optional[str]
    '''parse_mode: Mode for parsing entities in the message caption. See formatting options for more details.'''
    parse_mode: Optional[str]
    '''reply_markup: A JSON-serialized object for an inline keyboard .'''
    reply_markup: Optional[InlineKeyboardMarkup]

@dataclass
class editMessageMedia:
    '''chat_id: Required if inline_message_id is not specified. Unique identifier for the target chat or username of the target channel (in the format @channelusername )'''
    chat_id: Optional[Union[int, str]]
    '''message_id: Required if inline_message_id is not specified. Identifier of the message to edit'''
    message_id: Optional[int]
    '''inline_message_id: Required if chat_id and message_id are not specified. Identifier of the inline message'''
    inline_message_id: Optional[str]
    '''media: A JSON-serialized object for a new media content of the message'''
    media: InputMedia
    '''reply_markup: A JSON-serialized object for a new inline keyboard .'''
    reply_markup: Optional[InlineKeyboardMarkup]

@dataclass
class editMessageReplyMarkup:
    '''chat_id: Required if inline_message_id is not specified. Unique identifier for the target chat or username of the target channel (in the format @channelusername )'''
    chat_id: Optional[Union[int, str]]
    '''message_id: Required if inline_message_id is not specified. Identifier of the message to edit'''
    message_id: Optional[int]
    '''inline_message_id: Required if chat_id and message_id are not specified. Identifier of the inline message'''
    inline_message_id: Optional[str]
    '''reply_markup: A JSON-serialized object for an inline keyboard .'''
    reply_markup: Optional[InlineKeyboardMarkup]

@dataclass
class stopPoll:
    '''chat_id: Unique identifier for the target chat or username of the target channel (in the format @channelusername )'''
    chat_id: Union[int, str]
    '''message_id: Identifier of the original message with the poll'''
    message_id: int
    '''reply_markup: A JSON-serialized object for a new message inline keyboard .'''
    reply_markup: Optional[InlineKeyboardMarkup]

@dataclass
class deleteMessage:
    '''chat_id: Unique identifier for the target chat or username of the target channel (in the format @channelusername )'''
    chat_id: Union[int, str]
    '''message_id: Identifier of the message to delete'''
    message_id: int

@dataclass
class sendSticker:
    '''chat_id: Unique identifier for the target chat or username of the target channel (in the format @channelusername )'''
    chat_id: Union[int, str]
    '''sticker: Sticker to send. Pass a file_id as String to send a file that exists on the Telegram servers (recommended), pass an HTTP URL as a String for Telegram to get a .WEBP file from the Internet, or upload a new one using multipart/form-data. More info on Sending Files »'''
    sticker: Union[InputFile, str]
    '''disable_notification: Sends the message silently . Users will receive a notification with no sound.'''
    disable_notification: Optional[bool]
    '''reply_to_message_id: If the message is a reply, ID of the original message'''
    reply_to_message_id: Optional[int]
    '''reply_markup: Additional interface options. A JSON-serialized object for an inline keyboard, custom reply keyboard, instructions to remove reply keyboard or to force a reply from the user.'''
    reply_markup: Optional[Union[InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply]]

@dataclass
class getStickerSet:
    '''name: Name of the sticker set'''
    name: str

@dataclass
class uploadStickerFile:
    '''user_id: User identifier of sticker file owner'''
    user_id: int
    '''png_sticker: PNG image with the sticker, must be up to 512 kilobytes in size, dimensions must not exceed 512px, and either width or height must be exactly 512px. More info on Sending Files »'''
    png_sticker: InputFile

@dataclass
class createNewStickerSet:
    '''user_id: User identifier of created sticker set owner'''
    user_id: int
    '''name: Short name of sticker set, to be used in t.me/addstickers/ URLs (e.g., animals ). Can contain only english letters, digits and underscores. Must begin with a letter, can't contain consecutive underscores and must end in “_by_<bot username>” . <bot_username> is case insensitive. 1-64 characters.'''
    name: str
    '''title: Sticker set title, 1-64 characters'''
    title: str
    '''png_sticker: PNG image with the sticker, must be up to 512 kilobytes in size, dimensions must not exceed 512px, and either width or height must be exactly 512px. Pass a file_id as a String to send a file that already exists on the Telegram servers, pass an HTTP URL as a String for Telegram to get a file from the Internet, or upload a new one using multipart/form-data. More info on Sending Files »'''
    png_sticker: Optional[Union[InputFile, str]]
    '''tgs_sticker: TGS animation with the sticker, uploaded using multipart/form-data. See https://core.telegram.org/animated_stickers#technical-requirements for technical requirements'''
    tgs_sticker: Optional[InputFile]
    '''emojis: One or more emoji corresponding to the sticker'''
    emojis: str
    '''contains_masks: Pass True, if a set of mask stickers should be created'''
    contains_masks: Optional[bool]
    '''mask_position: A JSON-serialized object for position where the mask should be placed on faces'''
    mask_position: Optional[MaskPosition]

@dataclass
class addStickerToSet:
    '''user_id: User identifier of sticker set owner'''
    user_id: int
    '''name: Sticker set name'''
    name: str
    '''png_sticker: PNG image with the sticker, must be up to 512 kilobytes in size, dimensions must not exceed 512px, and either width or height must be exactly 512px. Pass a file_id as a String to send a file that already exists on the Telegram servers, pass an HTTP URL as a String for Telegram to get a file from the Internet, or upload a new one using multipart/form-data. More info on Sending Files »'''
    png_sticker: Optional[Union[InputFile, str]]
    '''tgs_sticker: TGS animation with the sticker, uploaded using multipart/form-data. See https://core.telegram.org/animated_stickers#technical-requirements for technical requirements'''
    tgs_sticker: Optional[InputFile]
    '''emojis: One or more emoji corresponding to the sticker'''
    emojis: str
    '''mask_position: A JSON-serialized object for position where the mask should be placed on faces'''
    mask_position: Optional[MaskPosition]

@dataclass
class setStickerPositionInSet:
    '''sticker: File identifier of the sticker'''
    sticker: str
    '''position: New sticker position in the set, zero-based'''
    position: int

@dataclass
class deleteStickerFromSet:
    '''sticker: File identifier of the sticker'''
    sticker: str

@dataclass
class setStickerSetThumb:
    '''name: Sticker set name'''
    name: str
    '''user_id: User identifier of the sticker set owner'''
    user_id: int
    '''thumb: A PNG image with the thumbnail, must be up to 128 kilobytes in size and have width and height exactly 100px, or a TGS animation with the thumbnail up to 32 kilobytes in size; see https://core.telegram.org/animated_stickers#technical-requirements for animated sticker technical requirements. Pass a file_id as a String to send a file that already exists on the Telegram servers, pass an HTTP URL as a String for Telegram to get a file from the Internet, or upload a new one using multipart/form-data. More info on Sending Files » . Animated sticker set thumbnail can't be uploaded via HTTP URL.'''
    thumb: Optional[Union[InputFile, str]]

@dataclass
class answerInlineQuery:
    '''inline_query_id: Unique identifier for the answered query'''
    inline_query_id: str
    '''results: A JSON-serialized array of results for the inline query'''
    results: List[InlineQueryResult]
    '''cache_time: The maximum amount of time in seconds that the result of the inline query may be cached on the server. Defaults to 300.'''
    cache_time: Optional[int]
    '''is_personal: Pass True, if results may be cached on the server side only for the user that sent the query. By default, results may be returned to any user who sends the same query'''
    is_personal: Optional[bool]
    '''next_offset: Pass the offset that a client should send in the next query with the same text to receive more results. Pass an empty string if there are no more results or if you don't support pagination. Offset length can't exceed 64 bytes.'''
    next_offset: Optional[str]
    '''switch_pm_text: If passed, clients will display a button with specified text that switches the user to a private chat with the bot and sends the bot a start message with the parameter switch_pm_parameter'''
    switch_pm_text: Optional[str]
    '''switch_pm_parameter: Deep-linking parameter for the /start message sent to the bot when user presses the switch button. 1-64 characters, only A-Z, a-z, 0-9, _ and - are allowed. Example: An inline bot that sends YouTube videos can ask the user to connect the bot to their YouTube account to adapt search results accordingly. To do this, it displays a 'Connect your YouTube account' button above the results, or even before showing any. The user presses the button, switches to a private chat with the bot and, in doing so, passes a start parameter that instructs the bot to return an oauth link. Once done, the bot can offer a switch_inline button so that the user can easily return to the chat where they wanted to use the bot's inline capabilities.'''
    switch_pm_parameter: Optional[str]

@dataclass
class sendInvoice:
    '''chat_id: Unique identifier for the target private chat'''
    chat_id: int
    '''title: Product name, 1-32 characters'''
    title: str
    '''description: Product description, 1-255 characters'''
    description: str
    '''payload: Bot-defined invoice payload, 1-128 bytes. This will not be displayed to the user, use for your internal processes.'''
    payload: str
    '''provider_token: Payments provider token, obtained via Botfather'''
    provider_token: str
    '''start_parameter: Unique deep-linking parameter that can be used to generate this invoice when used as a start parameter'''
    start_parameter: str
    '''currency: Three-letter ISO 4217 currency code, see more on currencies'''
    currency: str
    '''prices: Price breakdown, a JSON-serialized list of components (e.g. product price, tax, discount, delivery cost, delivery tax, bonus, etc.)'''
    prices: List[LabeledPrice]
    '''provider_data: A JSON-serialized data about the invoice, which will be shared with the payment provider. A detailed description of required fields should be provided by the payment provider.'''
    provider_data: Optional[str]
    '''photo_url: URL of the product photo for the invoice. Can be a photo of the goods or a marketing image for a service. People like it better when they see what they are paying for.'''
    photo_url: Optional[str]
    '''photo_size: Photo size'''
    photo_size: Optional[int]
    '''photo_width: Photo width'''
    photo_width: Optional[int]
    '''photo_height: Photo height'''
    photo_height: Optional[int]
    '''need_name: Pass True, if you require the user's full name to complete the order'''
    need_name: Optional[bool]
    '''need_phone_number: Pass True, if you require the user's phone number to complete the order'''
    need_phone_number: Optional[bool]
    '''need_email: Pass True, if you require the user's email address to complete the order'''
    need_email: Optional[bool]
    '''need_shipping_address: Pass True, if you require the user's shipping address to complete the order'''
    need_shipping_address: Optional[bool]
    '''send_phone_number_to_provider: Pass True, if user's phone number should be sent to provider'''
    send_phone_number_to_provider: Optional[bool]
    '''send_email_to_provider: Pass True, if user's email address should be sent to provider'''
    send_email_to_provider: Optional[bool]
    '''is_flexible: Pass True, if the final price depends on the shipping method'''
    is_flexible: Optional[bool]
    '''disable_notification: Sends the message silently . Users will receive a notification with no sound.'''
    disable_notification: Optional[bool]
    '''reply_to_message_id: If the message is a reply, ID of the original message'''
    reply_to_message_id: Optional[int]
    '''reply_markup: A JSON-serialized object for an inline keyboard . If empty, one 'Pay total price ' button will be shown. If not empty, the first button must be a Pay button.'''
    reply_markup: Optional[InlineKeyboardMarkup]

@dataclass
class answerShippingQuery:
    '''shipping_query_id: Unique identifier for the query to be answered'''
    shipping_query_id: str
    '''ok: Specify True if delivery to the specified address is possible and False if there are any problems (for example, if delivery to the specified address is not possible)'''
    ok: bool
    '''shipping_options: Required if ok is True. A JSON-serialized array of available shipping options.'''
    shipping_options: Optional[List[ShippingOption]]
    '''error_message: Required if ok is False. Error message in human readable form that explains why it is impossible to complete the order (e.g. "Sorry, delivery to your desired address is unavailable'). Telegram will display this message to the user.'''
    error_message: Optional[str]

@dataclass
class answerPreCheckoutQuery:
    '''pre_checkout_query_id: Unique identifier for the query to be answered'''
    pre_checkout_query_id: str
    '''ok: Specify True if everything is alright (goods are available, etc.) and the bot is ready to proceed with the order. Use False if there are any problems.'''
    ok: bool
    '''error_message: Required if ok is False . Error message in human readable form that explains the reason for failure to proceed with the checkout (e.g. "Sorry, somebody just bought the last of our amazing black T-shirts while you were busy filling out your payment details. Please choose a different color or garment!"). Telegram will display this message to the user.'''
    error_message: Optional[str]

@dataclass
class setPassportDataErrors:
    '''user_id: User identifier'''
    user_id: int
    '''errors: A JSON-serialized array describing the errors'''
    errors: List[PassportElementError]

@dataclass
class sendGame:
    '''chat_id: Unique identifier for the target chat'''
    chat_id: int
    '''game_short_name: Short name of the game, serves as the unique identifier for the game. Set up your games via Botfather .'''
    game_short_name: str
    '''disable_notification: Sends the message silently . Users will receive a notification with no sound.'''
    disable_notification: Optional[bool]
    '''reply_to_message_id: If the message is a reply, ID of the original message'''
    reply_to_message_id: Optional[int]
    '''reply_markup: A JSON-serialized object for an inline keyboard . If empty, one 'Play game_title' button will be shown. If not empty, the first button must launch the game.'''
    reply_markup: Optional[InlineKeyboardMarkup]

@dataclass
class setGameScore:
    '''user_id: User identifier'''
    user_id: int
    '''score: New score, must be non-negative'''
    score: int
    '''force: Pass True, if the high score is allowed to decrease. This can be useful when fixing mistakes or banning cheaters'''
    force: Optional[bool]
    '''disable_edit_message: Pass True, if the game message should not be automatically edited to include the current scoreboard'''
    disable_edit_message: Optional[bool]
    '''chat_id: Required if inline_message_id is not specified. Unique identifier for the target chat'''
    chat_id: Optional[int]
    '''message_id: Required if inline_message_id is not specified. Identifier of the sent message'''
    message_id: Optional[int]
    '''inline_message_id: Required if chat_id and message_id are not specified. Identifier of the inline message'''
    inline_message_id: Optional[str]

@dataclass
class getGameHighScores:
    '''user_id: Target user id'''
    user_id: int
    '''chat_id: Required if inline_message_id is not specified. Unique identifier for the target chat'''
    chat_id: Optional[int]
    '''message_id: Required if inline_message_id is not specified. Identifier of the sent message'''
    message_id: Optional[int]
    '''inline_message_id: Required if chat_id and message_id are not specified. Identifier of the inline message'''
    inline_message_id: Optional[str]
