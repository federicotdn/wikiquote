from .quotes import quotes, search
from .qotd import quote_of_the_day

from . import langs


def supported_languages():
    l = langs.SUPPORTED_LANGUAGES[:]
    l.sort()
    return l
