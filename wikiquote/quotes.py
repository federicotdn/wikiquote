from . import utils
import lxml.html
from . import langs


def _is_disambiguation(categories):
    # Checks to see if at least one category includes 'Disambiguation_pages'
    return not categories or any([
        category['*'] == 'Disambiguation_pages' for category in categories
    ])


def search(s, lang='en'):
    if lang not in langs.SUPPORTED_LANGUAGES:
        raise utils.UnsupportedLanguageException(
            'Unsupported language: ' + lang)

    if not s:
        return []

    local_srch_url = utils.SRCH_URL.format(lang=lang)
    data = utils.json_from_url(local_srch_url, s)
    results = [entry['title'] for entry in data['query']['search']]
    return results


def random_titles(lang='en', max_titles=20):
    if lang not in langs.SUPPORTED_LANGUAGES:
        raise utils.UnsupportedLanguageException(
            'Unsupported language: ' + lang)

    local_random_url = utils.RANDOM_URL.format(lang=lang, limit=max_titles)
    data = utils.json_from_url(local_random_url)
    results = [entry['title'] for entry in data['query']['random']]
    return results


def quotes(page_title, max_quotes=utils.DEFAULT_MAX_QUOTES, lang='en'):
    if lang not in langs.SUPPORTED_LANGUAGES:
        raise utils.UnsupportedLanguageException(
            'Unsupported language: ' + lang)

    local_page_url = utils.PAGE_URL.format(lang=lang)
    data = utils.json_from_url(local_page_url, page_title)
    if 'error' in data:
        raise utils.NoSuchPageException(
            'No pages matched the title: ' + page_title)

    if _is_disambiguation(data['parse']['categories']):
        raise utils.DisambiguationPageException(
            'Title returned a disambiguation page.')

    html_content = data['parse']['text']['*']
    html_tree = lxml.html.fromstring(html_content)
    return langs.extract_quotes_lang(lang, html_tree, max_quotes)
