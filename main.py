"""main file."""

from pogo_telegram_bot import create_app

if __name__ == '__main__':
    print('PoGo Telegram Bot start...')
    create_app().run_polling()
    print('PoGo Telegram stopped.')
