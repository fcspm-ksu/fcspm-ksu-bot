import logging
from environs import Env
import telegram.ext
from .conversations import general_conversation

env = Env()
env.read_env(env.str('ENV_PATH', 'bot/env/dev.env'))
token = env.str('TOKEN')
logging_level = env.str('LOGGING_LEVEL', 20)

logging.basicConfig(
    level=logging_level,
    format='%(asctime)s | %(levelname)s | %(name)s | %(message)s'
)

logger = logging.getLogger(__name__)


def main():
    updater = telegram.ext.Updater(token=token, use_context=True)

    dispatcher = updater.dispatcher
    dispatcher.add_handler(general_conversation)

    updater.start_polling()
    updater.idle()
