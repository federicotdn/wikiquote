from .. import utils

MAIN_PAGE = "Strona_główna"


def extract_quotes(tree, max_quotes):
    q_lst = utils.extract_quotes_li(tree, max_quotes)
    return [utils.remove_credit(q) for q in q_lst]


def qotd(html_tree):
    qotd_title = html_tree.xpath('.//div[text()="Cytat dnia"]')[0]
    qotd_element = qotd_title.getnext()
    qotd_components = qotd_element.xpath('table/tbody/tr')

    quote = qotd_components[0].text_content().strip()
    author = qotd_components[1].text_content().strip()
    return quote, author
