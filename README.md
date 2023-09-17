# PoGoTelegramBot
 The Telegram bot to assist Pokémon Go trainers.

## Quick Start

In order to start the project quickly, you need to follow the following steps:

1. Setup [instance](#instance);
2. Compile translations: `pybabel compile -d pogo_telegram_bot/translations`.

## Instance

The project requires the **config.py** file to exist in the **instance** folder, it should look like this:

```Python
"""config file."""

from typing import Final

# python-telegram-bot
TOKEN: Final = '[TELEGRAM_TOKEN]'

# i18n
LANGUAGES: Final = ['it']
```

**[TELEGRAM_TOKEN]** must be replaced with your Telegram bot token issued by [BotFather](https://t.me/botfather).

## Translations

### Setup New Locale

To extract the sentences to translate and create a new locale (**IT** in this case) run:

```Shell
pybabel extract -F babel.cfg -o pogo_telegram_bot/translations/messages.pot pogo_telegram_bot
pybabel init -i pogo_telegram_bot/translations/messages.pot -d pogo_telegram_bot/translations -l it
```

After creating the translations in the file *pogo_telegram_bot/translations/it/LC_MESSAGES/messages.po*, run:

```Shell
pybabel compile -d pogo_telegram_bot/translations
```

### Update Translations

To extract and update the sentences to translate run:

```Shell
pybabel extract -F babel.cfg -o pogo_telegram_bot/translations/messages.pot pogo_telegram_bot
pybabel update -i pogo_telegram_bot/translations/messages.pot -d pogo_telegram_bot/translations
```

After creating the translations into all files *messages.po*, run:

```Shell
pybabel compile -d pogo_telegram_bot/translations
```
