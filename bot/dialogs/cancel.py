from .utils import *
from telegram import ReplyKeyboardRemove
from telegram.ext import ConversationHandler


logger = logging.getLogger(__name__)


@log_msg
def cancel(update, context):
    user = update.message.from_user
    logger.info("User %s canceled the conversation.", user.username)
    update.message.reply_text(
        'Бувай!',
        reply_markup=ReplyKeyboardRemove()
    )
    return ConversationHandler.END
