from .. import utils

MAIN_PAGE = "Página_principal"
WORD_BLACKLIST = ["Fonte"]
HEADINGS = ["Veja também", "Referências"]


def extract_quotes(tree, max_quotes):
    # Remove all description elements
    dl_list = tree.xpath("//dl")
    for dl in dl_list:
        dl.getparent().remove(dl)

    return utils.extract_quotes_li(tree, max_quotes, HEADINGS, WORD_BLACKLIST)


def qotd(html_tree):
    tree = html_tree.get_element_by_id("mf-cdd")
    quote_author = tree.xpath(".//td")[2].text_content().split("-")

    quote = "-".join(quote_author[:-1]).strip().strip('"')
    author = quote_author[-1].strip()

    return quote, author
