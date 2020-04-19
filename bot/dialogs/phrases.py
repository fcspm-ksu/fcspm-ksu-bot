EDIT_EMOJI = '🖋 '
MAP_EMOJI = '🗺 '
DOC_EMOJI = '🗒 '
BELL_EMOJI = '🔔 '
TICK_EMOJI = '✔️ '
CROSS_EMOJI = '❌ '
SIGN_EMOJI = '❗ '
WEB_EMOJI = '🌐 '

THANKS = 'Дякую!'
WHERE_IS_PREFIX = MAP_EMOJI + 'Де знаходиться'
WHERE_IS_SOMETHING = WHERE_IS_PREFIX + '...?'

ORDER_CERTIFICATE_PREFIX = DOC_EMOJI + 'Замовити довідку'
ORDER_CERTIFICATE_WITH_BOT = ORDER_CERTIFICATE_PREFIX + ' через бота'
ORDER_CERTIFICATE_WITH_DATA = ORDER_CERTIFICATE_WITH_BOT + ' з введеними даними'

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

INPUT_PROMPT = 'Введіть, будь-ласка'
FULFILL = 'Необхідно заповнити інформацію'
UPDATE_OR_REQUEST = 'За необхідності можна виправити, якщо інформація вірна - замовити'

CANCEL = 'Скасувати'

SORRY = 'Вибачте, я нічого не знайшов для вас'

BELLS_SCHEDULE_TEXT = '''```
Розклад дзвінків:
І   пара:  08.30 – 09.50
ІІ  пара:  10.10 – 11.30
ІІІ пара:  11.50 – 13.10
ІV  пара:  13.20 – 14.40
V   пара:  14.50 – 16.10
VІ  пара:  16.20 – 17.40
```'''

KSPU_ORDER_CERTIFICATE_PAGE = 'http://www.kspu.edu/About/Faculty/FPhysMathemInformatics/storinki_faculti' \
                              '/OrderCertificateFromDeansOffice.aspx '

