from itertools import islice


MAIN_PAGE = "Wikiquote:Accueil"


def extract_quotes(tree, max_quotes):
    # French wiki uses a "citation" HTML class
    node_list = tree.xpath('//p/span[@class="citation"]')
    quotes = list(islice((span.text_content()
                          for span in node_list),
                         max_quotes))

    return quotes


def qotd(html_tree):
    tree = html_tree.get_element_by_id('mf-cdj')
    tree = tree.xpath('div/div')[1].xpath('table/tr/td')[1]

    quote = tree.xpath('div/i')[0].text_content().replace(u'\xa0', u' ')
    author = tree.xpath('div/a')[0].text_content()
    return quote, author
