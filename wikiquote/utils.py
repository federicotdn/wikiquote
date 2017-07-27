import json


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
    try:
        from urllib.request import urlopen as Urlopen
        from urllib.parse import quote as Quote
    except ImportError:
        from urllib import pathname2url as Quote
        from urllib2 import urlopen as Urlopen
    if params:
        url += Quote(params)
    res = Urlopen(url)
    body = res.read().decode()
    return json.loads(body)