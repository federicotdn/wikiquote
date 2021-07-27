import logging
import re

from .. import utils

MAIN_PAGE = "Wikiquote:Accueil"

logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())


def extract_quotes(tree, max_quotes):
    # French wiki uses a "citation" HTML class
    nodes = tree.xpath('//div[@class="citation"]')
    quotes = [utils.clean_txt(node.text_content()) for node in nodes]
    return quotes[:max_quotes]


def qotd_old_method(html_tree):
    tree = html_tree.get_element_by_id("mf-cdj")
    tree = tree.xpath("div/div")[1].xpath("table/tbody/tr/td")[1]

    quote = tree.xpath("div/i")[0].text_content()
    author = tree.xpath("div/a")[0].text_content()
    return quote, author


def qotd_new_method(html_tree):
    tree = html_tree.get_element_by_id("mf-cdj")
    lines = [
        line.strip().replace(u"\xa0", " ") for line in tree.text_content().splitlines()
    ]

    for line in lines:
        matches = re.search(r"«(.+?)»(.+)", line)
        if not matches:
            continue

        quote = matches.group(1).strip()
        author = matches.group(2).strip("-—– \n")

        return quote, author

    raise Exception("Could not parse quote of the day from page contents.")


def qotd(html_tree):
    try:
        return qotd_new_method(html_tree)
    except Exception as e:
        logger.warning("Could not extract French QOTD using new method due to: %s", e)

    return qotd_old_method(html_tree)
