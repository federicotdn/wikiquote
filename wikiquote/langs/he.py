from .. import utils

MAIN_PAGE = "עמוד_ראשי"
HEADINGS = ["הערות שוליים", "ראו גם", "קישורים חיצוניים", "נאמר עליו"]


def extract_quotes(tree, max_quotes):
    q_lst = utils.extract_quotes_li(tree, max_quotes, headings=HEADINGS)
    return [remove_credit_he(q) for q in q_lst]


def remove_credit_he(quote):
    if "~" in quote:
        return quote.split("~")[0]

    return quote.strip()


def qotd(html_tree):

    quote_box = html_tree.xpath("//div[1]/table[3]/tbody/tr[2]/td")[0]

    quote = quote_box.xpath("b")[0]
    author = quote_box.xpath("small")[0]

    return quote.text_content(), author.text_content()
