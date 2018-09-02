import re

from .. import utils

WORD_BLACKLIST = []
MAIN_PAGE = "Hauptseite"
HEADINGS = ['Überprüft']


def remove_i_tags(tree):
    for i in tree.xpath('//i'):
        i.getparent().remove(i)


def extract_quotes(tree, max_quotes):
    remove_i_tags(tree)

    q_lst = utils.extract_quotes_li(tree, max_quotes, HEADINGS, WORD_BLACKLIST)
    return [utils.remove_credit(q) for q in q_lst]


def qotd(html_tree):
    tree = html_tree.get_element_by_id('mf-ZitatdW')
    raw_text = tree.xpath('div')[1].text_content().strip()
    raw_text = re.sub(r'\(.*?\)', '', raw_text)

    raw_quote = []
    for part in raw_text.split('\n'):
        if part:
            raw_quote.append(part)
        if len(raw_quote) == 2:
            break

    return raw_quote[0], raw_quote[1]
