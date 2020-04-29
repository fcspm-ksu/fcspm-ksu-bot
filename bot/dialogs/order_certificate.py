import os

from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove
from .utils import *
from .phrases import *
from .data import COURSES, SPECIALITIES

logger = logging.getLogger(__name__)

CERTIFICATE_NOTIFY_LIST = os.environ.get('CERTIFICATE_NOTIFY_LIST', '').split(',')

FULL_NAME = 'full_name'
COURSE = 'course'
SPECIALITY = 'speciality'
COMMENT = 'comment'


@log_msg
def order_certificate_start(update, context):
    reply_keyboard = [
        [WHERE_IS_FCSPM_DEANS_OFFICE],
        [WEB_EMOJI + KSPU_ORDER_CERTIFICATE_PAGE],
        [ORDER_CERTIFICATE_WITH_BOT]
    ]
    reply_markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True, resize_keyboard=True)
    update.message.reply_text(
        HOW_TO_ORDER_CERTIFICATE,
        reply_markup=reply_markup
    )
    return State.ORDER_CERTIFICATE_AWAIT_CHOICE


@log_msg
def order_certificate_prompt_loop(update, context):
    action = update.message.text
    if contains_from_list(action, [PUT_NAME, POST_NAME]):
        prompt_text(update, context)
        return State.ORDER_CERTIFICATE_NAME
    if contains_from_list(action, [PUT_COURSE, POST_COURSE]):
        prompt_text(update, context, [[c] for c in COURSES])
        return State.ORDER_CERTIFICATE_COURSE
    if contains_from_list(action, [PUT_SPECIALITY, POST_SPECIALITY]):
        prompt_text(update, context, [[s] for s in SPECIALITIES])
        return State.ORDER_CERTIFICATE_SPECIALITY
    if contains_from_list(action, [PUT_COMMENT, POST_COMMENT]):
        prompt_text(update, context)
        return State.ORDER_CERTIFICATE_COMMENT

    order_certificate_choicer(update, context)
    return State.ORDER_CERTIFICATE_CHOICER


@log_msg
def order_certificate_input_name(update, context):
    text = update.message.text
    context.user_data[FULL_NAME] = text
    order_certificate_choicer(update, context)
    return State.ORDER_CERTIFICATE_CHOICER


@log_msg
def order_certificate_input_course(update, context):
    text = update.message.text
    context.user_data[COURSE] = text
    order_certificate_choicer(update, context)
    return State.ORDER_CERTIFICATE_CHOICER


@log_msg
def order_certificate_input_speciality(update, context):
    text = update.message.text
    context.user_data[SPECIALITY] = text
    order_certificate_choicer(update, context)
    return State.ORDER_CERTIFICATE_CHOICER


@log_msg
def order_certificate_input_comment(update, context):
    text = update.message.text
    context.user_data[COMMENT] = text
    order_certificate_choicer(update, context)
    return State.ORDER_CERTIFICATE_CHOICER


@log_msg
def order_certificate_checkout(update, context):
    msg = ORDER_CERTIFICATE_HASHTAG
    msg += f'\n{update.effective_user.name}'
    msg += f'\n{context.user_data.get(FULL_NAME)}'
    msg += f'\n{context.user_data.get(SPECIALITY)}'
    msg += f'\n{context.user_data.get(COURSE)}'
    msg += f'\n{context.user_data.get(COMMENT)}' if context.user_data.get(COMMENT) else ''
    update.message.reply_text(
        msg,
        reply_markup=ReplyKeyboardRemove()
    )
    for notify in CERTIFICATE_NOTIFY_LIST:
        update.message.bot.sendMessage(
            notify,
            msg
        )
    update.message.reply_text(
        'Замовлення довідки надіслано',
        reply_markup=ReplyKeyboardRemove()
    )
    return State.GENERAL_CHOOSING


def formatter(condition: str, message: str, placeholder: str):
    if condition:
        return f'{message} з `{condition}`'
    return placeholder


def is_full(user_data):
    return user_data.get(FULL_NAME) and user_data.get(SPECIALITY) and user_data.get(COURSE)


def order_certificate_choicer(update, context):
    reply_keyboard = [
        [formatter(context.user_data.get(FULL_NAME), PUT_NAME, POST_NAME)],
        [formatter(context.user_data.get(SPECIALITY), PUT_SPECIALITY, POST_SPECIALITY)],
        [formatter(context.user_data.get(COURSE), PUT_COURSE, POST_COURSE)],
        [formatter(context.user_data.get(COMMENT), PUT_COMMENT, POST_COMMENT)],
    ]

    message = FULFILL
    if is_full(context.user_data):
        message = UPDATE_OR_REQUEST
        reply_keyboard.append([ORDER_CERTIFICATE_WITH_DATA])
    reply_markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True, resize_keyboard=True)

    update.message.reply_text(
        message,
        reply_markup=reply_markup
    )


def prompt_text(update, context, keyboard: List[List] = None):
    reply_markup = ReplyKeyboardRemove()
    if keyboard:
        reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard=True, resize_keyboard=True)

    update.message.reply_text(
        INPUT_PROMPT,
        reply_markup=reply_markup
    )
