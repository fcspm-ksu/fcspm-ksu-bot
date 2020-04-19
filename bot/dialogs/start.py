import telegram
from .utils import *
from .phrases import *

GENERAL_QUESTIONS = [
    WHERE_IS_SOMETHING,
    ORDER_CERTIFICATE_PREFIX,
    BELLS_SCHEDULE,
]


@log_msg
def start(update, context):
    reply_keyboard = [
        [question] for question in GENERAL_QUESTIONS
    ]

    update.message.reply_text(
        'Чим можу допомогти?',
        reply_markup=telegram.ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True, resize_keyboard=True))

    return State.GENERAL_CHOOSING
