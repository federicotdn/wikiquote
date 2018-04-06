import lxml.html

from . import utils
from . import langs
from .constants import DEFAULT_LANG


def quote_of_the_day(lang=DEFAULT_LANG):
    if lang not in langs.SUPPORTED_LANGUAGES:
        raise utils.UnsupportedLanguageException(
            'Unsupported language: ' + lang)

    main_page = langs.main_page_lang(lang)

    data = utils.json_from_url(utils.MAINPAGE_URL.format(lang=lang), main_page)
    html_tree = lxml.html.fromstring(data['parse']['text']['*'])
    return langs.qotd_lang(lang, html_tree)
