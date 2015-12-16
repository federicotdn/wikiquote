import os
import glob
import importlib

from .. import utils

modules = glob.glob(os.path.dirname(__file__) + '/*.py')
modules = [m for m in modules if not m.endswith('__init__.py')]
modules = [os.path.basename(f)[:-3] for f in modules]

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
    return lang_dict[lang].qotd(html_tree)


def main_page_lang(lang):
    check_lang(lang)
    return lang_dict[lang].MAIN_PAGE
