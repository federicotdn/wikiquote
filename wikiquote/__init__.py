from .quotes import quotes, random_titles, search
from .qotd import quote_of_the_day
from . import langs


def supported_languages():
    languages = langs.SUPPORTED_LANGUAGES[:]
    languages.sort()
    return languages
