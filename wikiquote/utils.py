import urllib.request
import urllib.parse
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
    if params:
        url += urllib.parse.quote(params)
    res = urllib.request.urlopen(url)
    body = res.read().decode()
    return json.loads(body)
