# coding: utf-8
import signal
import sys
import os

from telegram.ext import Updater, Dispatcher
from importlib import import_module
import inflection

import utils.logger as logger
import configurations.settings as settings


def load_handlers(dispatcher: Dispatcher):
    """Load handlers from files in a 'bot' directory."""
    base_path = os.path.join(os.path.dirname(__file__), 'bot')
    files = os.listdir(base_path)

    for file_name in files:
        handler_module, _ = os.path.splitext(file_name)

        module = import_module(f'.{handler_module}', 'bot')
        module.init(dispatcher)


def graceful_exit(*args, **kwargs):
    """Provide a graceful exit from a webhook server."""
    if updater is not None:
        updater.bot.delete_webhook()

    sys.exit(1)


if __name__ == "__main__":
    global updater
    logger.init_logger(f'logs/{settings.NAME}.log')

    updater = Updater(token=settings.TOKEN, use_context=True)

    load_handlers(updater.dispatcher)

    if settings.WEBHOOK:
        signal.signal(signal.SIGINT, graceful_exit)
        updater.start_webhook(**settings.WEBHOOK_OPTIONS)
        updater.bot.set_webhook(url=settings.WEBHOOK_URL)
    else:
        updater.start_polling()
