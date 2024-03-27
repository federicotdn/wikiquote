import logging
from typing import List, Text, Tuple

import lxml

from .. import utils

MAIN_PAGE = "Página_principal"
WORD_BLOCKLIST = ["Fonte"]
HEADINGS = ["Veja também", "Referências"]

logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())

def extract_quotes(tree: lxml.html.HtmlElement, max_quotes: int) -> List[Text]:
    # Remove all description elements
    dl_list = tree.xpath("//dl")
    for dl in dl_list:
        dl.getparent().remove(dl)

    return utils.extract_quotes_li(tree, max_quotes, HEADINGS, WORD_BLOCKLIST)


def qotd_by_element_id(html_tree: lxml.html.HtmlElement) -> Tuple[Text, Text]:
    tree = html_tree.get_element_by_id("mf-cdd")
    quote_author = tree.xpath(".//td")[2].text_content().split("-")

    quote = "-".join(quote_author[:-1]).strip().strip('"')
    author = quote_author[-1].strip()

    return quote, author


def qotd(html_tree: lxml.html.HtmlElement) -> Tuple[Text, Text]:
    try:
        return qotd_by_element_id(html_tree)
    except Exception as e:
        logger.warning("Could not extract pt QOTD using qotd_by_element_id due to: %s", e)
    raise utils.MissingQOTDException('Could not extract: All Attempts failed')