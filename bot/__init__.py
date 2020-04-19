import logging
import os
import telegram.ext
from .conversations import general_conversation

token = os.environ.get('TOKEN')
logging_level = os.environ.get('LOGGING_LEVEL')

# Port is given by Heroku
PORT = os.environ.get('PORT')
NAME = 'fcspm-ksu-bot'


logging.basicConfig(
    level=logging_level,
    format='%(asctime)s | %(levelname)s | %(name)s | %(message)s'
)

logger = logging.getLogger(__name__)


def main():
    updater = telegram.ext.Updater(token=token, use_context=True)

    dispatcher = updater.dispatcher
    dispatcher.add_handler(general_conversation)

    # Start the webhook
    updater.start_webhook(listen="0.0.0.0",
                          port=int(PORT),
                          url_path=token)
    updater.bot.setWebhook("https://{}.herokuapp.com/{}".format(NAME, token))
    updater.idle()
