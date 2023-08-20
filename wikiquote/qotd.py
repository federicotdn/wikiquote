from typing import Text, Tuple

import lxml.html

from . import langs, utils
from .constants import DEFAULT_LANG, MAINPAGE_URL


@utils.validate_lang
def quote_of_the_day(lang: Text = DEFAULT_LANG) -> Tuple[Text, Text]:
    main_page = langs.main_page_lang(lang)

    data = utils.json_from_url(MAINPAGE_URL.format(lang=lang), main_page)
    html_tree = lxml.html.fromstring(data["parse"]["text"]["*"])

    try:
        return langs.qotd_lang(lang, html_tree)
    except (IndexError, KeyError):
        raise utils.MissingQOTDException(
            "Unable to retrieve quote of the day. This is probably due to a recent "
            "change in Wikiquote's main page page layout. Please try again later. "
            "If the problem persists, open an issue at: "
            "https://github.com/federicotdn/wikiquote"
        )
