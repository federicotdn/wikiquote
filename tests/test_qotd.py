import wikiquote
import unittest


class QotdTest(unittest.TestCase):
    """
    Test wikiquote.quote_of_the_day()
    """

    def test_qotd_quote(self):
        for lang in wikiquote.supported_languages():
            quote, author = wikiquote.quote_of_the_day(lang=lang)
            self.assertIsInstance(quote, str)
            self.assertTrue(len(quote) > 0)

    def test_unsupported_lang(self):
        with self.assertRaisesRegex(
            wikiquote.UnsupportedLanguageException, "Unsupported language: foobar"
        ):
            wikiquote.quote_of_the_day(lang="foobar")

    def test_qotd_author(self):
        for lang in wikiquote.supported_languages():
            quote, author = wikiquote.quote_of_the_day()
            self.assertIsInstance(author, str)
            self.assertTrue(len(author) > 0)

    def test_qotd_qotd(self):
        self.assertEqual(wikiquote.quote_of_the_day(), wikiquote.qotd())
