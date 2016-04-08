WORD_BLACKLIST = ['quoted', 'Variant:', 'Retrieved', 'Notes:']
MIN_QUOTE_LEN = 6
MIN_QUOTE_WORDS = 3
MAIN_PAGE = "Main Page"


def is_cast_credit(txt_split):
    # Checks to see if the text is a cast credit:
    #   <actor name> as <character name>
    #   <actor name> - <character name>
    if not 2 < len(txt_split) < 7:
        return False

    separators = ['as', '-', '–']
    return all([w[0].isupper() or w in separators or w[0] == '"'
               for w in txt_split])


def is_quote(txt):
    txt_split = txt.split()
    invalid_conditions = [
        not txt or not txt[0].isupper() or len(txt) < MIN_QUOTE_LEN,
        len(txt_split) < MIN_QUOTE_WORDS,
        any([True for word in txt_split if word in WORD_BLACKLIST]),
        txt.endswith(('(', ':', ']')),
        is_cast_credit(txt_split)
    ]

    # Returns false if any invalid conditions are true, otherwise returns True.
    return not any(invalid_conditions)


def extract_quotes(tree, max_quotes):
    quotes_list = []

    # List items inside unordered lists
    node_list = tree.xpath('//div/ul/li')

    # Description tags inside description lists,
    # first one is generally not a quote
    dd_list = tree.xpath('//div/dl/dd')[1:]
    if len(dd_list) > len(node_list):
        node_list += dd_list

    for node in node_list:
        uls = node.xpath('ul')
        for ul in uls:
            ul.getparent().remove(ul)

        txt = node.text_content().strip()
        if is_quote(txt) and max_quotes > len(quotes_list):
            txt_normal = ' '.join(txt.split())
            quotes_list.append(txt_normal)

            if max_quotes == len(quotes_list):
                break

    return quotes_list


def qotd(html_tree):
    tree = html_tree.get_element_by_id('mf-qotd')

    raw_quote = tree.xpath('div/div/table/tr')[0].text_content().split('~')
    quote = raw_quote[0].strip()
    author = raw_quote[1].strip()
    return quote, author
