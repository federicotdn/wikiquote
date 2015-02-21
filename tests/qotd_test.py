import wikiquote
import unittest

class QotdTest(unittest.TestCase):
    """
    Test wikiquote.quote_of_the_day()
    """

    def test_qotd_quote(self):
        quote, author = wikiquote.quote_of_the_day()
        self.assertIsInstance(quote, str)
        self.assertTrue(len(quote) > 0)

    def test_qotd_author(self):
        quote, author = wikiquote.quote_of_the_day()
        self.assertIsInstance(author, str)
        self.assertTrue(len(author) > 0)