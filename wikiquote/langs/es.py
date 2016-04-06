MAIN_PAGE = "Portada"


def extract_quotes(tree, max_quotes):
    quotes_list = []

    # List items inside unordered lists
    node_list = tree.xpath('//div/ul/li')
    for node in node_list:
        print(node.text_content())
        print('-------')

    return quotes_list


def qotd(html_tree):
    tree = html_tree.get_element_by_id('mf-FDD')

    quote_container = tree.xpath('div/table/tr')
    raw_quote = quote_container[0].text_content().split('~')
    quote = raw_quote[0].strip()

    raw_author = quote_container[1].xpath('td/div/a')[0].text_content()
    author = raw_author.strip()

    return quote, author
