from .quotes import quotes, random_titles, search
from .qotd import quote_of_the_day

from . import langs


def supported_languages():
    l = langs.SUPPORTED_LANGUAGES[:]
    l.sort()
    return l
