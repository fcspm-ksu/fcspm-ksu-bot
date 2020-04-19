import os

from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove
from .utils import *
from .phrases import *
from .data import COURSES, SPECIALITIES

logger = logging.getLogger(__name__)

CERTIFICATE_NOTIFY_LIST = os.environ.get('CERTIFICATE_NOTIFY_LIST', '').split(',')


@log_msg
def order_certificate_start(update, context):
    reply_keyboard = [
        [WHERE_IS_PREFIX + ' деканат на факультеті комп`ютерних наук, фізики та математики'],
        [WEB_EMOJI + KSPU_ORDER_CERTIFICATE_PAGE],
        [ORDER_CERTIFICATE_WITH_BOT]
    ]
    reply_markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True, resize_keyboard=True)
    update.message.reply_text(
        'Довідку можна замовити особисто в деканаті, використавши форму на сайті або з допомогою бота',
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
    context.user_data['full_name'] = text
    order_certificate_choicer(update, context)
    return State.ORDER_CERTIFICATE_CHOICER


@log_msg
def order_certificate_input_course(update, context):
    text = update.message.text
    context.user_data['course'] = text
    order_certificate_choicer(update, context)
    return State.ORDER_CERTIFICATE_CHOICER


@log_msg
def order_certificate_input_speciality(update, context):
    text = update.message.text
    context.user_data['speciality'] = text
    order_certificate_choicer(update, context)
    return State.ORDER_CERTIFICATE_CHOICER


@log_msg
def order_certificate_input_comment(update, context):
    text = update.message.text
    context.user_data['comment'] = text
    order_certificate_choicer(update, context)
    return State.ORDER_CERTIFICATE_CHOICER


@log_msg
def order_certificate_checkout(update, context):
    msg = '#ЗАМОВЛЕННЯ_ДОВІДКИ'
    msg += f'\n{update.effective_user.name}'
    msg += f'\n{context.user_data.get("full_name")}'
    msg += f'\n{context.user_data.get("speciality")}'
    msg += f'\n{context.user_data.get("course")}'
    msg += f'\n{context.user_data.get("comment")}' if context.user_data.get("comment") else ''
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
    return user_data.get('full_name') and user_data.get('speciality') and user_data.get('course')


def order_certificate_choicer(update, context):
    reply_keyboard = [
        [formatter(context.user_data.get('full_name'), PUT_NAME, POST_NAME)],
        [formatter(context.user_data.get("speciality"), PUT_SPECIALITY, POST_SPECIALITY)],
        [formatter(context.user_data.get("course"), PUT_COURSE, POST_COURSE)],
        [formatter(context.user_data.get("comment"), PUT_COMMENT, POST_COMMENT)],
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
