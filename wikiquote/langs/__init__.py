import os
import glob
import importlib


modules = [
    os.path.basename(m)[:-3]
    for m in glob.glob(os.path.dirname(__file__) + "/*.py")
    if not m.endswith("__init__.py")
]

lang_dict = {}

for m in modules:
    module = importlib.import_module("." + m, "wikiquote.langs")
    lang_dict[m] = module


SUPPORTED_LANGUAGES = modules


def extract_quotes_lang(lang, html_tree, max_quotes):
    return lang_dict[lang].extract_quotes(html_tree, max_quotes)


def qotd_lang(lang, html_tree):
    quote, author = lang_dict[lang].qotd(html_tree)
    return quote, author.split(",")[0]


def main_page_lang(lang):
    return lang_dict[lang].MAIN_PAGE
