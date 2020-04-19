from telegram import ReplyKeyboardMarkup
from .location_processor import Location
from .data import WHERE_IS
from .phrases import *
from .utils import *


__all__ = [
    'where_is_all',
    'where_is',
]


def response_location(update, response: Optional[Location]):
    reply_markup = None
    reply_text = SORRY
    if response:
        reply_keyboard = [
                             [f'{WHERE_IS_PREFIX} {location.name.lower()}'] for location in response.children
                         ] + [[THANKS]]
        reply_markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True, resize_keyboard=True)
        reply_text = response.info()
        update.message.bot.sendLocation(update.message.chat_id, location=response.location())

    update.message.reply_text(
        reply_text,
        reply_markup=reply_markup
    )


@log_msg
def where_is_all(update, context):
    reply_keyboard = [
        [f'{WHERE_IS_PREFIX} {location.name}'] for location in WHERE_IS.base()
    ]
    update.message.reply_text(
        WHERE_IS_SOMETHING,
        reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True, resize_keyboard=True))
    return State.GENERAL_CHOOSING


@log_msg
def where_is(update, context):
    text = update.message.text
    response = WHERE_IS.similar(text)
    response_location(update, response)
    return State.GENERAL_CHOOSING
