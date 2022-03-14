# coding: utf-8
import os
import signal
import sys
from importlib import import_module

from telegram.ext import Dispatcher, Updater

import configurations.settings as settings
import utils.logger as logger


def load_handlers(dispatcher: Dispatcher):
    """Load handlers from files in a 'bot' directory."""
    base_path = os.path.join(os.path.dirname(__file__), "bot")
    files = os.listdir(base_path)

    for file_name in files:
        handler_module, _ = os.path.splitext(file_name)

        module = import_module(f".{handler_module}", "bot")
        module.init(dispatcher)


def graceful_exit(*_, **__):
    """Provide a graceful exit from a webhook server."""
    if updater is not None:
        updater.bot.delete_webhook()

    sys.exit(0)


if __name__ == "__main__":
    logger.init_logger(f"logs/{settings.NAME}.log")

    updater = Updater(token=settings.TOKEN)

    load_handlers(updater.dispatcher)

    if settings.WEBHOOK:
        signal.signal(signal.SIGINT, graceful_exit)
        updater.start_webhook(**settings.WEBHOOK_OPTIONS)
    else:
        updater.start_polling()
