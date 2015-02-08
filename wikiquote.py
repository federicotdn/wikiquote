import urllib.request, urllib.parse, json, lxml.html

class NoSuchPageException(Exception):
	pass

class DisambiguationPageException(Exception):
	pass

SEARCH_URL = 'http://en.wikiquote.org/w/api.php?format=json&action=query&list=search&continue=&srsearch='
PAGE_URL = 'http://en.wikiquote.org/w/api.php?format=json&action=parse&prop=text|categories&page='
MIN_QUOTE_LEN = 6
MIN_QUOTE_WORDS = 3
DEFAULT_MAX_QUOTES = 20
WORD_BLACKLIST = ['quoted', 'Variant:', 'Retrieved', 'Notes:']

def json_from_url(url):
	res = urllib.request.urlopen(url)
	body = res.read().decode()
	return json.loads(body)

def search(s):
	search_terms = urllib.parse.quote(s)
	data = json_from_url(SEARCH_URL + search_terms)

	results = []
	for entry in data['query']['search']:
		results.append(entry['title'])

	return results

def is_disambiguation(categories):
	if not categories:
		return True

	for cat in categories:
		if cat['*'] == 'Disambiguation_pages':
			return True
	return False

def is_quote(txt):
	if not txt or not txt[0].isupper() or len(txt) < MIN_QUOTE_LEN:
		return False

	txt_split = txt.split()
	if len(txt_split) < MIN_QUOTE_WORDS:
		return False

	for word in txt_split:
		if word in WORD_BLACKLIST:
			return False

	if txt.endswith(('(', ':', ']')):
		return False

	return True

def extract_quotes(html_content, max_quotes):
	tree = lxml.html.fromstring(html_content)
	quotes_list = []

	txt_list = tree.xpath('//div/ul/li')
	for txt in txt_list:

		uls = txt.xpath('ul')
		for ul in uls:
			ul.getparent().remove(ul)

		txt = txt.text_content().strip()
		if is_quote(txt):
			txt_normal = ' '.join(txt.split())
			quotes_list.append(txt_normal)

			if max_quotes == len(quotes_list):
				break

	return quotes_list

def quotes(page_title, max_quotes = DEFAULT_MAX_QUOTES):
	data = json_from_url(PAGE_URL + urllib.parse.quote(page_title))
	if 'error' in data:
		raise NoSuchPageException('No pages matched the title: ' + page_title)

	if is_disambiguation(data['parse']['categories']):
		raise DisambiguationPageException('Title returned a disambiguation page.')

	html_content = data['parse']['text']['*']
	return extract_quotes(html_content, max_quotes)
