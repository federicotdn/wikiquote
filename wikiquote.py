import urllib.request
import urllib.parse
import json
import lxml.html


class NoSuchPageException(Exception):
    pass


class DisambiguationPageException(Exception):
    pass

W_URL = 'http://en.wikiquote.org/w/api.php'
SRCH_URL = W_URL + '?format=json&action=query&list=search&continue=&srsearch='
PAGE_URL = W_URL + '?format=json&action=parse&prop=text|categories&page='
MAINPAGE_URL = W_URL + '?format=json&action=parse&page=Main%20Page&prop=text'
MIN_QUOTE_LEN = 6
MIN_QUOTE_WORDS = 3
DEFAULT_MAX_QUOTES = 20
WORD_BLACKLIST = ['quoted', 'Variant:', 'Retrieved', 'Notes:']


def json_from_url(url):
    res = urllib.request.urlopen(url)
    body = res.read().decode()
    return json.loads(body)


def search(s):
    if not s:
        return []
    search_terms = urllib.parse.quote(s)
    data = json_from_url(SRCH_URL + search_terms)
    results = [entry['title'] for entry in data['query']['search']]
    return results


def is_disambiguation(categories):
    # Checks to see if at least one category includes 'Disambiguation_pages'
    return not categories or any([
        category['*'] == 'Disambiguation_pages' for category in categories
    ])


def is_cast_credit(txt_split):
    # Checks to see if the text is a cast credit:
    #   <actor name> as <character name>
    #   <actor name> - <character name>
    if not 2 < len(txt_split) < 7:
        return False

    separators = ['as', '-', '–']
    return all([w[0].isupper() or w in separators for w in txt_split])


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


def extract_quotes(html_content, max_quotes):
    tree = lxml.html.fromstring(html_content)
    quotes_list = []

    # List items inside unordered lists
    node_list = tree.xpath('//div/ul/li')

    # Description tags inside description lists,
    # first one is generally not a quote
    dd_list = tree.xpath('//div/dl/dd')[1:]
    if len(dd_list) > len(node_list):
        node_list += dd_list

    for txt in node_list:
        uls = txt.xpath('ul')
        for ul in uls:
            ul.getparent().remove(ul)

        txt = txt.text_content().strip()
        if is_quote(txt) and max_quotes > len(quotes_list):
            txt_normal = ' '.join(txt.split())
            quotes_list.append(txt_normal)

            if max_quotes == len(quotes_list):
                break

    return quotes_list


def quotes(page_title, max_quotes=DEFAULT_MAX_QUOTES):
    data = json_from_url(PAGE_URL + urllib.parse.quote(page_title))
    if 'error' in data:
        raise NoSuchPageException('No pages matched the title: ' + page_title)

    if is_disambiguation(data['parse']['categories']):
        raise DisambiguationPageException(
            'Title returned a disambiguation page.')

    html_content = data['parse']['text']['*']
    return extract_quotes(html_content, max_quotes)


def quote_of_the_day():
    data = json_from_url(MAINPAGE_URL)
    tree = lxml.html.fromstring(data['parse']['text']['*'])
    tree = tree.get_element_by_id('mf-qotd')

    raw_quote = tree.xpath('div/div/table/tr')[0].text_content().split('~')
    quote = raw_quote[0].strip()
    author = raw_quote[1].strip()
    return quote, author
