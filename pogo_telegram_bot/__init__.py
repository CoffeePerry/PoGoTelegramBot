"""pogo_telegram_bot factory."""

from typing import Final
from logging import INFO, basicConfig
from os import makedirs, linesep
from os.path import join, isdir, isfile

from telegram.ext import Application, ApplicationBuilder, PicklePersistence

from pogo_telegram_bot.services.config import Config
from pogo_telegram_bot.services.translations import init_app as init_translations
from pogo_telegram_bot.controllers import init_app as init_routes

VERSION: Final = '0.1.1'
INSTANCE_PATH: Final = 'instance'
CONFIG_FILENAME: Final = 'config.py'
PERSISTENCE_FILENAME: Final = 'persistence.bin'

basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=INFO
)


def create_app(options: dict | None = None) -> Application | None:
    """Application factory.

    :param options: Optional application options (default: None).
    :type: dict | None
    :return: An Application instance.
    :rtype: Application | None
    """
    if not isinstance(options, dict | None):
        raise Exception('Invalid options')

    config = Config()
    if (options is None) or (not options.get('TESTING')):
        # Ensure the instance folder exists
        if not isdir(INSTANCE_PATH):
            makedirs(INSTANCE_PATH)
            raise Exception(f'Directory not found, so just created: {INSTANCE_PATH}.{linesep}'
                            f'Put file "{CONFIG_FILENAME}" inside, please.')

        # Load the instance config
        config_file = join(INSTANCE_PATH, CONFIG_FILENAME)
        if not isfile(config_file):
            raise Exception(f'Configuration file not found: {config_file}')
        config.from_pyfile(config_file)

        if config.get('TOKEN') is None:
            raise Exception(f'Set variable TOKEN with Telegram Bot Token string in file: {config_file}')

    if options is not None:
        # Load the options config
        config.from_mapping(options)

    # Build application
    app = (
        ApplicationBuilder()
        .token(config['TOKEN'])
        .persistence(persistence=PicklePersistence(filepath=join(INSTANCE_PATH, PERSISTENCE_FILENAME)))
        .build()
    )
    app.config = config

    # Services initializations
    init_translations(app)
    init_routes(app)

    return app
