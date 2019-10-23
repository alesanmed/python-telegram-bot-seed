# encoding: utf-8

# Telegram API framework core imports
from telegram.ext import Dispatcher, CallbackContext
from telegram import Update
# Helper methods import
from utils.logger import get_logger

# Telegram API framework handlers imports
from telegram.ext import CommandHandler

# Init logger
logger = get_logger(__name__)


def init(dispatcher: Dispatcher):
    """Provide handlers initialization."""
    dispatcher.add_handler(CommandHandler('start', start))


def start(update: Update, context: CallbackContext):
    """Process a /start command."""
    update.effective_message.reply_text(text="I'm a bot, please talk to me!")
