# telegram-bot-api-schema
Telegram Bot API Schema generated from the official docs

# Usage:

```bash
poetry run python generate_schema.py jsonschema > schema.json

# Then, for example:
quicktype -o telegram_bot_api.py --python-version 3.7 --src-lang schema schema.json
```
