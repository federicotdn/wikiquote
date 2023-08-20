import unittest
from collections import defaultdict

import wikiquote


class QuotesTest(unittest.TestCase):
    """
    Test wikiquote.quotes()
    """

    def test_disambiguation(self):
        with self.assertRaises(wikiquote.DisambiguationPageException):
            wikiquote.quotes("Matrix")

    def test_no_such_page(self):
        with self.assertRaises(wikiquote.utils.NoSuchPageException):
            wikiquote.quotes("foobarfoobar")

    def test_unsupported_lang(self):
        with self.assertRaisesRegex(
            wikiquote.UnsupportedLanguageException, "Unsupported language: foobar"
        ):
            wikiquote.quotes("Matrix", lang="foobar")

    def test_normal_quotes(self):
        query_by_lang = defaultdict(lambda: "Barack Obama")
        # Special case: The hebrew wikiquote doesn't support searches in English
        query_by_lang["he"] = "ברק אובמה"
        # Special case: The basque wikiquote doesn't have a page for Barack Obama
        query_by_lang["eu"] = "Simón Bolívar"

        for lang in wikiquote.supported_languages():
            quotes = wikiquote.quotes(query_by_lang[lang], lang=lang)
            self.assertTrue(len(quotes) > 0)

    def test_max_quotes(self):
        quotes = wikiquote.quotes("The Matrix (film)", max_quotes=8)
        self.assertEqual(len(quotes), 8)

    def test_max_quotes_and_lang(self):
        quotes = wikiquote.quotes("Matrix", lang="fr", max_quotes=8)
        self.assertEqual(len(quotes), 8)
