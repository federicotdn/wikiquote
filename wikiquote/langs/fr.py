from .. import utils

MAIN_PAGE = "Wikiquote:Accueil"


def extract_quotes(tree, max_quotes):
    # French wiki uses a "citation" HTML class
    nodes = tree.xpath('//div[@class="citation"]')
    quotes = [utils.clean_txt(node.text_content()) for node in nodes]
    return quotes[:max_quotes]


def qotd(html_tree):
    tree = html_tree.get_element_by_id('mf-cdj')
    tree = tree.xpath('div/div')[1].xpath('table/tbody/tr/td')[1]

    quote = tree.xpath('div/i')[0].text_content()
    author = tree.xpath('div/a')[0].text_content()
    return quote, author
