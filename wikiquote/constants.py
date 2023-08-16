DEFAULT_LANG = "en"
DEFAULT_MAX_QUOTES = 20
MIN_QUOTE_LEN = 6
MIN_QUOTE_WORDS = 3
W_URL = "http://{lang}.wikiquote.org/w/api.php"
SRCH_URL = W_URL + "?format=json&action=query&list=search&continue=&srsearch="
RANDOM_URL = W_URL + "?format=json&action=query&list=random&rnnamespace=0&rnlimit={limit}"
PAGE_URL = W_URL + "?format=json&action=parse&prop=text|categories&" "disableeditsection&page="
MAINPAGE_URL = W_URL + "?format=json&action=parse&prop=text&page="