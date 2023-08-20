from typing import List, Text

from . import langs
from .qotd import quote_of_the_day
from .quotes import quotes, random_titles, search
from .utils import (
    DisambiguationPageException,
    MissingQOTDException,
    NoSuchPageException,
    UnsupportedLanguageException,
)


def supported_languages() -> List[Text]:
    return sorted(langs.SUPPORTED_LANGUAGES)


qotd = quote_of_the_day


__all__ = [
    "quotes",
    "random_titles",
    "search",
    "qotd",
    "quote_of_the_day",
    "supported_languages",
    "DisambiguationPageException",
    "NoSuchPageException",
    "UnsupportedLanguageException",
    "MissingQOTDException",
]
