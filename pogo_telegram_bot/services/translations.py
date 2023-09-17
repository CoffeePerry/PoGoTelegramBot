"""translations service."""

from functools import wraps
from gettext import gettext, translation

from telegram.ext import Application, ContextTypes


def init_app(app: Application):
    """Initializes the application translations.

    :param app: Application instance.
    :type app: Application
    """
    translations = {language: translation('messages', './pogo_telegram_bot/translations',
                                          languages=[language]) for language in app.config['LANGUAGES']}
    app.translations = translations


def get_translations(context: ContextTypes.DEFAULT_TYPE):
    """Get user translations.

    :param context: Context instance.
    :type context: ContextTypes.DEFAULT_TYPE
    """
    lang_code = context.user_data.get('lang_code')
    if lang_code and (lang_code != 'en'):
        return context.application.translations[lang_code].gettext
    return gettext


def add_translations():
    """Add translations."""
    def wrapper(func):
        """Add translations (wrapper)."""
        @wraps(func)
        async def wrapped(*args):
            """Add translations (wrapped)."""
            context = args[1]
            _ = get_translations(context)
            new_args = args + (_,)

            return await func(*new_args)
        return wrapped
    return wrapper
