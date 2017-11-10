import lxml.etree
from .. import utils

WORD_BLACKLIST = ['quoted', 'Variant:', 'Retrieved', 'Notes:', 'article:']
MAIN_PAGE = "Main Page"
HEADINGS = ['cast', 'see also', 'external links']


def extract_quotes(tree, max_quotes):
    return utils.extract_quotes_li(tree, max_quotes, HEADINGS, WORD_BLACKLIST)


def qotd(html_tree):
    tree = html_tree.get_element_by_id('mf-qotd')

    raw_quote = tree.xpath('div/div/table/tr')[0].text_content().split('~')
    quote = raw_quote[0].strip()
    author = raw_quote[1].strip()
    return quote, author
