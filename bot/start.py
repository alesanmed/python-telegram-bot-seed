# encoding: utf-8

from logging import getLogger

from telegram import Update
from telegram.ext import CallbackContext, CommandHandler, Dispatcher

# Init logger
logger = getLogger(__name__)


def init(dispatcher: Dispatcher):
    """Provide handlers initialization."""
    dispatcher.add_handler(CommandHandler("start", start))


def start(update: Update, _: CallbackContext):
    """Process a /start command."""
    update.message.reply_text(text="I'm a bot, please talk to me!")
