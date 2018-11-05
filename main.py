#coding: utf-8
import signal
import sys
import os

from telegram.ext import Updater
from importlib import import_module
import inflection

import utils.logger as logger
import configurations.bot_config as bot_config

updater = None

def load_commands(dispatcher):
    base_path = os.path.join(os.path.dirname(__file__), 'bot')
    files = os.listdir(base_path)

    for file_name in files:
        command, _ = os.path.splitext(file_name)

        module = import_module('.%s' % (command,), 'bot')

        module.main(dispatcher)
        

def graceful_exit(signum, frame):
    if(updater is not None):
        updater.bot.delete_webhook()
    
    sys.exit(1)

if __name__ == "__main__":
    logger.init_logger('logs/%s.log' % (bot_config.NAME,))

    updater = Updater(token=bot_config.TOKEN)

    dispatcher = updater.dispatcher

    load_commands(dispatcher)
    
    if(bot_config.WEBHOOK):
        signal.signal(signal.SIGINT, graceful_exit)
        updater.start_webhook(listen=bot_config.IP, port=bot_config.PORT, url_path=bot_config.URL_PATH)
        updater.bot.set_webhook(url=bot_config.WEBHOOK_URL)
    else:
        updater.start_polling()