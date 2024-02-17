from typing import List, Text, Tuple

import lxml

from .. import utils

MAIN_PAGE = "Portada"
WORD_BLOCKLIST = ["Fuente:", "Traducción:", "Nota:"]
HEADINGS = ["enlaces externos", "referencias"]


def extract_quotes(tree: lxml.html.HtmlElement, max_quotes: int) -> List[Text]:
    return utils.extract_quotes_li(tree, max_quotes, HEADINGS, WORD_BLOCKLIST)


def qotd(html_tree: lxml.html.HtmlElement) -> Tuple[Text, Text]:
    tree = html_tree.get_element_by_id("mf-FDD")

    quote_container = tree.xpath("div/table/tbody/tr")
    raw_quote = quote_container[0].text_content().split("~")
    quote = raw_quote[0].strip()

    raw_author = quote_container[1].xpath("td/div/a")[0].text_content()
    author = raw_author.strip()

    return utils.clean_txt(quote), author
