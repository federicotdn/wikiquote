from typing import List, Text, Tuple

import lxml

from .. import utils

MAIN_PAGE = "Strona_główna"


def extract_quotes(tree: lxml.html.HtmlElement, max_quotes: int) -> List[Text]:
    q_lst = utils.extract_quotes_li(tree, max_quotes)
    return [utils.remove_credit(q) for q in q_lst]


def qotd(html_tree: lxml.html.HtmlElement) -> Tuple[Text, Text]:
    qotd_lang_title = 'Cytat dnia'
    qotd_title_query = html_tree.xpath(f'.//div[text()="{qotd_lang_title}"]')
    if qotd_title_query:
        qotd_title = qotd_title_query[0]
    else:
        qotd_title = html_tree.xpath(f'.//span[text()="{qotd_lang_title}"]')[0].getparent()

    qotd_element = qotd_title.getnext()
    qotd_components = qotd_element.xpath("table/tbody/tr")

    quote = qotd_components[0].text_content().strip()
    author = qotd_components[1].text_content().strip()
    return quote, author
