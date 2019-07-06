from .quotes import quotes, random_titles, search
from .qotd import quote_of_the_day
from . import langs


def supported_languages():
    return sorted(langs.SUPPORTED_LANGUAGES)


__all__ = [
    'quotes',
    'random_titles',
    'search',
    'quote_of_the_day',
    'supported_languages'
]
