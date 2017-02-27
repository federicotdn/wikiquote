import lxml.etree

WORD_BLACKLIST = ['quoted', 'Variant:', 'Retrieved', 'Notes:', 'article:']
MIN_QUOTE_LEN = 6
MIN_QUOTE_WORDS = 3
MAIN_PAGE = "Main Page"


def is_quote(txt):
    txt_split = txt.split()
    invalid_conditions = [
        not txt or not txt[0].isupper() or len(txt) < MIN_QUOTE_LEN,
        len(txt_split) < MIN_QUOTE_WORDS,
        any(True for word in txt_split if word in WORD_BLACKLIST),
        txt.endswith(('(', ':', ']')),
    ]

    # Returns false if any invalid conditions are true, otherwise returns True.
    return not any(invalid_conditions)


def is_quote_node(node):
    # Discard nodes with the <small> tag
    if node.find('small') is not None:
        return False

    # Discard nodes that are just a link
    # (using xpath so lxml will show text nodes)
    # The link may be inside <i> or <b> tags, so keep peeling layers
    suspect_node = node
    while True:
        node_children = suspect_node.xpath('child::node()')
        if len(node_children) != 1:
            break

        suspect_node = node_children[0]
        if not isinstance(suspect_node, lxml.etree._Element):
            break

        if suspect_node.tag == 'a':
            return False

    return True


def extract_quotes(tree, max_quotes):
    quotes_list = []

    # Remove table of contents
    toc_list = tree.xpath('//div[@id="toc"]')
    for toc in toc_list:
        toc.getparent().remove(toc)

    # Scan list items description tags inside description lists.
    # Also grab headlines to skip some sections.
    node_list = tree.xpath('//div/ul/li|//div/dl|//h2')

    # Skip all quotes above the first heading
    skip_to_next_heading = True

    for node in node_list:
        if node.tag != 'h2' and skip_to_next_heading:
            continue

        if node.tag == 'h2':
            skip_to_next_heading = False
            heading_text = node.text_content().lower()

            # Commence skipping
            if heading_text in ('cast', 'see also', 'external links'):
                skip_to_next_heading = True

            continue

        # <dl>'s are assumed to be multi-line dialogue
        if node.tag == 'dl':
            dds = node.xpath('dd')

            if not all(is_quote_node(dd) for dd in dds):
                continue

            full_dialogue = '\n'.join(
                dd.text_content().strip()
                for dd in dds)

            if is_quote(full_dialogue):
                quotes_list.append(full_dialogue)

            if max_quotes == len(quotes_list):
                break

            continue

        # Handle <li>'s
        uls = node.xpath('ul')
        for ul in uls:
            ul.getparent().remove(ul)

        if not is_quote_node(node):
            continue

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
