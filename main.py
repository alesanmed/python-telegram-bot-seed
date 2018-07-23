#coding: utf-8
'''
main.py

Created by Ale Sanchez on 2018-07-23

Copyright (c) 2018. All rights reserved.
'''

from telegram.ext import Updater, CommandHandler

import utils.logger as logger
import configurations.bot_config as bot_config
from commands import commands

if __name__ == "__main__":
    logger.init_logger(f'logs/{bot_config.NAME}.log')

    updater = Updater(token=bot_config.TOKEN)

    dispatcher = updater.dispatcher

    for command in commands:
        command_handler = CommandHandler(command['command'], command['function'])

        dispatcher.add_handler(command_handler)
    if(bot_config.WEBHOOK):
        updater.start_webhook(listen=bot_config.IP, port=bot_config.PORT, url_path=bot_config.URL_PATH)
        updater.bot.set_webhook(webhook_url=bot_config.WEBHOOK_ULR, certificate=open(bot_config.CERT, 'rb'))
    else:
        updater.start_polling()