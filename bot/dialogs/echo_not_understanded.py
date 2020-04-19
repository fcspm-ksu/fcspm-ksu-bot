from .utils import *
from .phrases import *
from telegram import ReplyKeyboardRemove
from telegram.ext import ConversationHandler


logger = logging.getLogger(__name__)


@log_msg
def echo_not_understanded(update, context):
    user = update.message.from_user
    text = update.message.text
    update.message.reply_text(
        f'{SORRY} ({text})',
        reply_markup=ReplyKeyboardRemove()
    )
    return ConversationHandler.END
