from .utils import *
from .phrases import *
from telegram import ParseMode, ReplyKeyboardRemove
from telegram.ext import ConversationHandler

__all__ = [
    'bells_schedule',
]


@log_msg
def bells_schedule(update, context):
    update.message.reply_text(
        BELLS_SCHEDULE_TEXT,
        reply_markup=ReplyKeyboardRemove(),
        parse_mode=ParseMode.MARKDOWN_V2
    )
    return ConversationHandler.END
