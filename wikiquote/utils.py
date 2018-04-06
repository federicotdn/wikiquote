import urllib.request
import urllib.parse
import json
import lxml

MIN_QUOTE_LEN = 6
MIN_QUOTE_WORDS = 3


class NoSuchPageException(Exception):
    pass


class DisambiguationPageException(Exception):
    pass


class UnsupportedLanguageException(Exception):
    pass


W_URL = 'http://{lang}.wikiquote.org/w/api.php'
SRCH_URL = W_URL + '?format=json&action=query&list=search&continue=&srsearch='
RANDOM_URL = W_URL + \
    '?format=json&action=query&list=random&rnnamespace=0&rnlimit={limit}'
PAGE_URL = W_URL + '?format=json&action=parse&prop=text|categories&' \
    'disableeditsection&page='
MAINPAGE_URL = W_URL + '?format=json&action=parse&prop=text&page='
DEFAULT_MAX_QUOTES = 20


def json_from_url(url, params=None):
    if params:
        url += urllib.parse.quote(params)
    res = urllib.request.urlopen(url)
    body = res.read().decode('utf-8')
    return json.loads(body)


def clean_txt(txt):
    to_remove = '«»"'
    for ch in to_remove:
        txt = txt.replace(ch, '')
    return txt.strip()


def remove_credit(quote):
    if quote.endswith(('–', '-')):
        quote = quote[:-1].rstrip()
    return quote


def is_quote(txt, word_blacklist):
    txt_split = txt.split()
    invalid_conditions = [
        txt and txt[0].isalpha() and txt[0].islower(),
        len(txt) < MIN_QUOTE_LEN,
        len(txt_split) < MIN_QUOTE_WORDS,
        any(True for word in txt_split if word in word_blacklist),
        txt.endswith(('(', ':', ']')),
    ]

    # Returns False if any invalid conditions are True, otherwise returns True.
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


def extract_quotes_li(tree, max_quotes, headings, word_blacklist):
    # Check for quotes inside list items and description lists
    # This function works well for EN and ES versions of Wikiquote articles
    quotes_list = []

    # Remove table of contents
    toc_list = tree.xpath('//div[@id="toc"]')
    for toc in toc_list:
        toc.getparent().remove(toc)

    # Scan list items description tags inside description lists.
    # Also grab headlines to skip some sections.
    node_list = tree.xpath('//div/ul/li|//div/dl|//h2|//h3')

    # Skip all quotes above the first heading
    skip_to_next_heading = True

    for node in node_list:
        if node.tag not in ['h2', 'h3'] and skip_to_next_heading:
            continue

        if node.tag in ['h2', 'h3']:
            skip_to_next_heading = False
            heading_text = node.text_content().lower()

            # Commence skipping
            for unwanted_heading in headings:
                if heading_text.startswith(unwanted_heading.lower()):
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
            full_dialogue = clean_txt(full_dialogue)
            if is_quote(full_dialogue, word_blacklist):
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

        txt = node.text_content()
        txt = clean_txt(txt)
        if is_quote(txt, word_blacklist) and max_quotes > len(quotes_list):
            txt_normal = ' '.join(txt.split())
            quotes_list.append(txt_normal)

            if max_quotes == len(quotes_list):
                break

    return quotes_list
