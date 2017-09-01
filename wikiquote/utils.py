import json
import sys

if sys.version_info.major >= 3:
    import urllib.request as request
    import urllib.parse as parser
    from urllib.parse import quote
else:
    import urllib2 as request
    import urlparse as parser
    from urllib2 import quote

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
        url += quote(params)
    res = request.urlopen(url)
    body = res.read().decode()
    return json.loads(body)
