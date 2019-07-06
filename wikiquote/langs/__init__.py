import os
import glob
import importlib

from .. import utils

modules = [
    os.path.basename(m)[:-3]
    for m in glob.glob(os.path.dirname(__file__) + '/*.py')
    if not m.endswith('__init__.py')
]

lang_dict = {}

for m in modules:
    module = importlib.import_module('.' + m, 'wikiquote.langs')
    lang_dict[m] = module


SUPPORTED_LANGUAGES = modules


def check_lang(lang):
    if lang not in SUPPORTED_LANGUAGES:
        raise utils.UnsupportedLanguageException(
            'Unsupported language: ' + lang)


def extract_quotes_lang(lang, html_tree, max_quotes):
    check_lang(lang)
    return lang_dict[lang].extract_quotes(html_tree, max_quotes)


def qotd_lang(lang, html_tree):
    check_lang(lang)
    quote, author = lang_dict[lang].qotd(html_tree)
    return quote, author.split(',')[0]


def main_page_lang(lang):
    check_lang(lang)
    return lang_dict[lang].MAIN_PAGE
