from .. import utils

MAIN_PAGE = "Pagina_principale"
WORD_BLACKLIST = []
HEADINGS = [
    'Bibliografia',
    'Opere',
    'Altri progetti',
    'Note',
    'Voci correlate'
]


def extract_quotes(tree, max_quotes):
    return utils.extract_quotes_li(tree, max_quotes, HEADINGS, WORD_BLACKLIST)


def qotd(html_tree):
    tree = html_tree.get_element_by_id('mf-Qotd')

    quote_container = tree.xpath('div')[0].text_content().split('„')

    quote = quote_container[0].lstrip('“').strip()
    author = quote_container[1].strip()

    return quote, author
