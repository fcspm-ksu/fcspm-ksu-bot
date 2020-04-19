import logging
import difflib
from telegram.ext import BaseFilter
from typing import *


class State:
    CANCEL = 0
    GENERAL_CHOOSING = 1

    ORDER_CERTIFICATE_PROMPT = 20
    ORDER_CERTIFICATE_AWAIT_CHOICE = 21

    ORDER_CERTIFICATE_CHOICER = 30
    ORDER_CERTIFICATE_NAME = 31
    ORDER_CERTIFICATE_SPECIALITY = 32
    ORDER_CERTIFICATE_COURSE = 33
    ORDER_CERTIFICATE_COMMENT = 34


def log_msg(func):
    def wrapper(update, context):
        result = func(update, context)
        c = update.effective_chat
        msg = update.message.text
        if c["type"] == "private":
            msg = f'{c["username"]}({c["last_name"]} {c["first_name"]}) | State => {result}: {update.message.text}'
        elif c["type"] == "group":
            msg = f'{c["title"]}): {update.message.text}'
        logging.log(logging.INFO, msg)
        return result

    return wrapper


def similarity(s1: str, s2: str) -> float:
    return difflib.SequenceMatcher(a=s1.lower(), b=s2.lower()).ratio()


class FilterContains(BaseFilter):

    def filter(self, message):
        return contains_from_list(message.text, self.__list)

    def __init__(self, list_: List[str]):
        self.__list = list_


def contains_from_list(str_: str, list_: List[str]):
    list_ = list_ or []
    str_ = str_ or ""
    return any([str_ in txt for txt in list_])
