import logging
import re
from typing import List, Text, Tuple

import lxml

from .. import utils

MAIN_PAGE = "Wikiquote:Accueil"

logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())


def extract_quotes(tree: lxml.html.HtmlElement, max_quotes: int) -> List[Text]:
    # French wiki uses a "citation" HTML class
    nodes = tree.xpath('//div[@class="citation"]')
    quotes = [utils.clean_txt(node.text_content()) for node in nodes]
    return quotes[:max_quotes]


def qotd_old_method(html_tree: lxml.html.HtmlElement) -> Tuple[Text, Text]:
    tree = html_tree.get_element_by_id("mf-cdj")
    tree = tree.xpath("div/div")[1].xpath("table/tbody/tr/td")[1]

    quote = tree.xpath("div/i")[0].text_content()
    author = tree.xpath("div/a")[0].text_content()
    return quote, author


def qotd_new_method(html_tree: lxml.html.HtmlElement) -> Tuple[Text, Text]:
    tree = html_tree.get_element_by_id("mf-cdj")
    lines = [
        line.strip().replace("\xa0", " ") for line in tree.text_content().splitlines()
    ]

    for line in lines:
        matches = re.search(r"«(.+?)»(.+)", line)
        if not matches:
            continue

        quote = matches.group(1).strip()
        author = matches.group(2).strip("-—– \n")

        return quote, author

    raise Exception("Could not parse quote of the day from page contents.")


def qotd(html_tree: lxml.html.HtmlElement) -> Tuple[Text, Text]:
    try:
        return qotd_new_method(html_tree)
    except Exception as e:
        logger.warning("Could not extract French QOTD using new method due to: %s", e)

    try:
        return qotd_by_qotd_lang_title(html_tree)
    except Exception as e:
        logger.warning("Could not extract French QOTD using qotd_by_qotd_lang_title method due to: %s", e)
    return qotd_old_method(html_tree)


def qotd_by_qotd_lang_title(html_tree: lxml.html.HtmlElement) -> Tuple[Text, Text]:
    """Uses QOTD title (translated in lang) to traverse tree and find quotation and author"""
    tree = html_tree.xpath('.//*[text()="Citation au hasard"]')[0]
    quote_author_parts = tree.xpath('..//..//*')[0].getnext().xpath('.//text()')
    quote_author_line = ''.join(quote_author_parts)    
    quote_author_line = quote_author_line.strip().replace('\xa0', ' ').replace('\n', ' ')
    quote_author_line = ''.join(c for c in quote_author_line if c.isprintable()) # Remove unprintable chars
    matches = re.search(r"^(.*?)—(.*?)$", quote_author_line)
    if matches:
        quote = matches.group(1).strip()
        author = matches.group(2).strip()
    return quote, author