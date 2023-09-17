"""controllers module."""

from telegram.ext import Application, CommandHandler, MessageHandler, filters

from pogo_telegram_bot.controllers.base import start_cmd, stop_cmd, help_cmd, settings_cmd, unknown_cmd


def init_app(app: Application):
    """Initializes the application routes.

    :param app: Application instance.
    :type app: Application
    """
    app.add_handler(CommandHandler('start', start_cmd))
    app.add_handler(CommandHandler('stop', stop_cmd))
    app.add_handler(CommandHandler('help', help_cmd))
    app.add_handler(CommandHandler('settings', settings_cmd))
    app.add_handler(MessageHandler(filters.COMMAND, unknown_cmd))
