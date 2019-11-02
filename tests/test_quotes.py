import wikiquote
import unittest


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
        for lang in wikiquote.supported_languages():
            quotes = wikiquote.quotes("Barack Obama", lang=lang)
            self.assertTrue(len(quotes) > 0)

    def test_max_quotes(self):
        quotes = wikiquote.quotes("The Matrix (film)", max_quotes=8)
        self.assertEqual(len(quotes), 8)

    def test_max_quotes_and_lang(self):
        quotes = wikiquote.quotes("Matrix", lang="fr", max_quotes=8)
        self.assertEqual(len(quotes), 8)
