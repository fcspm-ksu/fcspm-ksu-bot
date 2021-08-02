"""
Any phrases used by bot.

Tips:
Avoid prefix commands as keywords wor different sates: shortest prefix will intercept handling
"""


EDIT_EMOJI = '🖋 '
MAP_EMOJI = '🗺 '
DOC_EMOJI = '🗒 '
BELL_EMOJI = '🔔 '
TICK_EMOJI = '✔️ '
CROSS_EMOJI = '❌ '
SIGN_EMOJI = '❗ '
WEB_EMOJI = '🌐 '

HOW_TO_ORDER_CERTIFICATE = 'Довідку можна замовити в деканаті, використавши форму на сайті або за допомогою бота'
ORDER_CERTIFICATE_HASHTAG = '#ЗАМОВЛЕННЯ_ДОВІДКИ'

THANKS = 'Дякую!'
WHERE_IS_PREFIX = MAP_EMOJI + 'Де знаходиться'
WHERE_IS_SOMETHING = WHERE_IS_PREFIX + '...?'
WHERE_IS_FCSPM_DEANS_OFFICE = WHERE_IS_PREFIX + ' деканат на факультеті комп`ютерних наук, фізики та математики'

ORDER_CERTIFICATE_PREFIX = DOC_EMOJI + 'Замовити довідку'
ORDER_CERTIFICATE_WITH_BOT = ORDER_CERTIFICATE_PREFIX + ' через бота'
ORDER_CERTIFICATE_WITH_DATA = DOC_EMOJI + 'Підтвердити замовлення через бота з введеними даними'

BELLS_SCHEDULE = BELL_EMOJI + 'Розклад дзвінків'

PUT_NAME = TICK_EMOJI + 'Змінити ПІП'
POST_NAME = SIGN_EMOJI + 'Ввесити ПІП'
PUT_SPECIALITY = TICK_EMOJI + 'Змінити спеціальність'
POST_SPECIALITY = SIGN_EMOJI + 'Обрати спеціальність'
PUT_COURSE = TICK_EMOJI + 'Змінити курс'
POST_COURSE = SIGN_EMOJI + 'Обрати курс'
PUT_COMMENT = EDIT_EMOJI + 'Змінити коментар'
POST_COMMENT = EDIT_EMOJI + 'Додати коментар'

ORDER_CERTIFICATE_COMMANDS = [
    ORDER_CERTIFICATE_WITH_BOT,
    PUT_NAME, POST_NAME,
    PUT_SPECIALITY, POST_SPECIALITY,
    PUT_COURSE, POST_COURSE,
    PUT_COMMENT, POST_COMMENT
]

INPUT_PROMPT = 'Введіть, будь ласка'
FULFILL = 'Необхідно заповнити інформацію'
UPDATE_OR_REQUEST = 'За необхідності можна виправити, якщо інформація вірна - замовити'

CANCEL = 'Скасувати'

SORRY = 'Вибачте, я нічого не знайшов для вас'

BELLS_SCHEDULE_TEXT = '''```
Розклад дзвінків:
І   пара:  08.30 – 09.50
ІІ  пара:  10.00 – 11.20
ІІІ пара:  11.50 – 13.10
ІV  пара:  13.30 – 14.50
V   пара:  15.00 – 16.20
VІ  пара:  16.30 – 17.50
```'''

KSPU_ORDER_CERTIFICATE_PAGE = 'http://www.kspu.edu/About/Faculty/FPhysMathemInformatics/storinki_faculti' \
                              '/OrderCertificateFromDeansOffice.aspx '

