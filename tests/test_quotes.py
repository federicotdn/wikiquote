import wikiquote
import unittest

class QuotesTest(unittest.TestCase):
    """
    Test wikiquote.quotes()
    """

    def test_disambiguation(self):
        self.assertRaises(wikiquote.utils.DisambiguationPageException,
                          wikiquote.quotes,
                          'Matrix')

    def test_no_such_page(self):
        self.assertRaises(wikiquote.utils.NoSuchPageException,
                          wikiquote.quotes,
                          'aaksejhfkasehfksdfsa')

    def test_unsupported_lang(self):
        self.assertRaises(wikiquote.utils.UnsupportedLanguageException,
                         wikiquote.quotes,
                         'Matrix',
                         lang='hlhljopjpojkopijj')

    def test_normal_quotes(self):
        for lang in wikiquote.langs.SUPPORTED_LANGUAGES:
            quotes = wikiquote.quotes('Barack Obama', lang=lang)
            self.assertTrue(len(quotes) > 0)

    def test_max_quotes(self):
        quotes = wikiquote.quotes('The Matrix (film)', max_quotes = 8)
        self.assertEqual(len(quotes), 8)

    def test_max_quotes_and_lang(self):
        quotes = wikiquote.quotes('Matrix', lang='fr', max_quotes = 8)
        self.assertEqual(len(quotes), 8)
