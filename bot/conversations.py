import logging
import re
from telegram.ext import *
from .dialogs import *

logger = logging.getLogger(__name__)

general_conversation = ConversationHandler(
    entry_points=[
        CommandHandler('start', start),

        CommandHandler('order_certificate', order_certificate_start),
        MessageHandler(FilterContains([ORDER_CERTIFICATE_PREFIX]), order_certificate_start),

        CommandHandler('bells_schedule', bells_schedule),
        MessageHandler(FilterContains([BELLS_SCHEDULE]), bells_schedule),
    ],

    states={
        State.GENERAL_CHOOSING: [
            MessageHandler(FilterContains([WHERE_IS_SOMETHING]), where_is_all),
            MessageHandler(FilterContains([WHERE_IS_PREFIX]), where_is),

            CommandHandler('order_certificate', order_certificate_start),
            MessageHandler(FilterContains([ORDER_CERTIFICATE_PREFIX]), order_certificate_start),

            CommandHandler('bells_schedule', bells_schedule),
            MessageHandler(FilterContains([BELLS_SCHEDULE]), bells_schedule),
        ],
        State.ORDER_CERTIFICATE_AWAIT_CHOICE: [
            MessageHandler(FilterContains([ORDER_CERTIFICATE_WITH_BOT]), order_certificate_prompt_loop),
        ],
        State.ORDER_CERTIFICATE_CHOICER: [
            MessageHandler(FilterContains(ORDER_CERTIFICATE_COMMANDS), order_certificate_prompt_loop),
            MessageHandler(FilterContains([ORDER_CERTIFICATE_WITH_DATA]), order_certificate_checkout)
        ],
        State.ORDER_CERTIFICATE_NAME: [MessageHandler(Filters.text, order_certificate_input_name)],
        State.ORDER_CERTIFICATE_COURSE: [MessageHandler(Filters.text, order_certificate_input_course)],
        State.ORDER_CERTIFICATE_SPECIALITY: [MessageHandler(Filters.text, order_certificate_input_speciality)],
        State.ORDER_CERTIFICATE_COMMENT: [MessageHandler(Filters.text, order_certificate_input_comment)],
    },

    fallbacks=[
        MessageHandler(Filters.regex(rf'^{re.escape(WHERE_IS_PREFIX)}(.+)$'), where_is),
        MessageHandler(Filters.regex(rf'^{re.escape(THANKS)}$'), cancel),

        CommandHandler('order_certificate', order_certificate_start),
        CommandHandler('cancel', cancel),
        CommandHandler('start', start),

        MessageHandler(Filters.all, echo_not_understanded)
    ]
)
