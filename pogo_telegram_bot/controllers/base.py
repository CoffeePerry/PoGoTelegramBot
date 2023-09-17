"""base controller."""

from logging import exception
from os import linesep

from telegram import Update
from telegram.ext import ContextTypes

from pogo_telegram_bot.services.translations import add_translations


@add_translations()
async def start_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE, _):  # pylint: disable=unused-argument
    """Start command.

    :param update: Update instance.
    :type update: Update
    :param context: Context instance.
    :type context: ContextTypes.DEFAULT_TYPE
    :param _: Translations instance.
    """
    try:
        await update.message.reply_text(_('Welcome') + f' {update.effective_user.first_name}! 🤖{linesep}' +
                                        _('If you don\'t know where to start I recommend you start by typing '
                                          'the command') + ' /help')
    except AttributeError:
        return
    except Exception as ex:
        exception(ex)
        await update.message.reply_text(_('I encountered an internal error. Please try again.'))


@add_translations()
async def stop_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE, _):  # pylint: disable=unused-argument
    """Stop command.

    :param update: Update instance.
    :type update: Update
    :param context: Context instance.
    :type context: ContextTypes.DEFAULT_TYPE
    :param _: Translations instance.
    """
    try:
        await update.message.reply_text(_('Bye') + f' {update.effective_user.first_name} 👋')
    except AttributeError:
        return
    except Exception as ex:
        exception(ex)
        await update.message.reply_text(_('I encountered an internal error. Please try again.'))


@add_translations()
async def help_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE, _):  # pylint: disable=unused-argument
    """Help command.

    :param update: Update instance.
    :type update: Update
    :param context: Context instance.
    :type context: ContextTypes.DEFAULT_TYPE
    :param _: Translations instance.
    """
    try:
        await update.message.reply_text(_('This Telegram bot assists Pokémon Go trainers. Try it now. '
                                          'Type /login to authenticate.') + f'{linesep}{linesep}')
    except AttributeError:
        return
    except Exception as ex:
        exception(ex)
        await update.message.reply_text(_('I encountered an internal error. Please try again.'))


@add_translations()
async def settings_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE, _):  # pylint: disable=unused-argument
    """Settings command.

    :param update: Update instance.
    :type update: Update
    :param context: Context instance.
    :type context: ContextTypes.DEFAULT_TYPE
    :param _: Translations instance.
    """
    try:
        message = update.message.text
        if not message.startswith('/settings language'):
            await update.message.reply_text(_('Wrong command! You need to add the language settings parameter '
                                              '(for example') + ': /settings language it).')
            return

        language = message[19:]
        if not language:
            values = f'{linesep}- en'
            for lang_code in context.application.translations.keys():
                values += f'{linesep}- {lang_code}'
            await update.message.reply_text(_('Wrong command! The parameter relating to the language to be set must be '
                                              'added.') + linesep + _('The possible values are') + f':{values}')
            return

        if (language not in context.application.translations.keys()) and (language != 'en'):
            await update.message.reply_text(_('Language ') + language + _(' not supported.'))
            return

        context.user_data['lang_code'] = language
        await update.message.reply_text(_('Language ') + language + _(' set successfully.'))
    except AttributeError:
        return
    except Exception as ex:
        exception(ex)
        await update.message.reply_text(_('I encountered an internal error. Please try again.'))


@add_translations()
async def unknown_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE, _):  # pylint: disable=unused-argument
    """Unknown command.

    :param update: Update instance.
    :type update: Update
    :param context: Context instance.
    :type context: ContextTypes.DEFAULT_TYPE
    :param _: Translations instance.
    """
    try:
        await update.message.reply_text(_('Sorry, I don\'t know this command') + ' 😕')
    except AttributeError:
        return
    except Exception as ex:
        exception(ex)
        await update.message.reply_text(_('I encountered an internal error. Please try again.'))
