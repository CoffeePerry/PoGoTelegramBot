# PoGoTelegramBot
 The Telegram bot to assist Pokémon Go trainers.

## Translation

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

### Update

To extract and update the sentences to translate run:

```Shell
pybabel extract -F babel.cfg -o pogo_telegram_bot/translations/messages.pot pogo_telegram_bot
pybabel update -i pogo_telegram_bot/translations/messages.pot -d pogo_telegram_bot/translations
```

After creating the translations into all files *messages.po*, run:

```Shell
pybabel compile -d pogo_telegram_bot/translations
```
