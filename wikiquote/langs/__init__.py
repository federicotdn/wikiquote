from typing import List, Text, Tuple
import os
import glob
import importlib

import lxml


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


def extract_quotes_lang(
    lang: Text, html_tree: lxml.html.HtmlElement, max_quotes: int
) -> List[Text]:
    return lang_dict[lang].extract_quotes(html_tree, max_quotes)  # type: ignore


def qotd_lang(lang: Text, html_tree: lxml.html.HtmlElement) -> Tuple[Text, Text]:
    quote, author = lang_dict[lang].qotd(html_tree)  # type: ignore
    return quote, author.split(",")[0]


def main_page_lang(lang: Text) -> Text:
    return lang_dict[lang].MAIN_PAGE  # type: ignore
