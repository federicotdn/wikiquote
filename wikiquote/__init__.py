from .quotes import quotes, random_titles, search  # noqa: F401
from .qotd import quote_of_the_day  # noqa: F401
from . import langs


def supported_languages():
    return sorted(langs.SUPPORTED_LANGUAGES[:])
