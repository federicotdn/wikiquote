from typing import List, Text, Tuple

import lxml

from .. import utils

MAIN_PAGE = "Pagina_principale"
HEADINGS = ["Bibliografia", "Opere", "Altri progetti", "Note", "Voci correlate"]


def extract_quotes(tree: lxml.html.HtmlElement, max_quotes: int) -> List[Text]:
    return utils.extract_quotes_li(tree, max_quotes, HEADINGS)


def qotd(html_tree: lxml.html.HtmlElement) -> Tuple[Text, Text]:
    tree = html_tree.xpath("//div[@class='main-page-qotd']/div")[2]

    quote_container = tree.text_content().split("„")

    quote = quote_container[0].lstrip("“").strip()
    author = quote_container[1].strip()

    return quote, author
