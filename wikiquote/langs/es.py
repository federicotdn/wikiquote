from .. import utils

MAIN_PAGE = "Portada"
WORD_BLACKLIST = ['Fuente:', 'Traducción:', 'Nota:']
HEADINGS = ['enlaces externos', 'referencias']


def extract_quotes(tree, max_quotes):
    return utils.extract_quotes_li(tree, max_quotes, HEADINGS, WORD_BLACKLIST)


def qotd(html_tree):
    tree = html_tree.get_element_by_id('mf-FDD')

    quote_container = tree.xpath('div/table/tbody/tr')
    raw_quote = quote_container[0].text_content().split('~')
    quote = raw_quote[0].strip()

    raw_author = quote_container[1].xpath('td/div/a')[0].text_content()
    author = raw_author.strip()

    return quote, author
