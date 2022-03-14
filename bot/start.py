# encoding: utf-8

# Telegram API framework core imports
from telegram import Update
# Telegram API framework handlers imports
from telegram.ext import CallbackContext, CommandHandler, Dispatcher
# Helper methods import
from utils.logger import get_logger

# Init logger
logger = get_logger(__name__)


def init(dispatcher: Dispatcher):
    """Provide handlers initialization."""
    dispatcher.add_handler(CommandHandler('start', start))


def start(update: Update, context: CallbackContext):
    """Process a /start command."""
    update.message.reply_text(text="I'm a bot, please talk to me!")
