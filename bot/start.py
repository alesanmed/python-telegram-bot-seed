'''
start.py

Created by Ale Sanchez on 2018-07-23

Copyright (c) 2018. All rights reserved.
'''

def main(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="I'm a bot, please talk to me!")