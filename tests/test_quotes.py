import wikiquote
import unittest

class QuotesTest(unittest.TestCase):
    """
    Test wikiquote.quotes()
    """

    def test_disambiguation(self):
        self.assertRaises(wikiquote.DisambiguationPageException,
                          wikiquote.quotes,
                          'Matrix')

    def test_no_such_page(self):
        self.assertRaises(wikiquote.NoSuchPageException,
                          wikiquote.quotes,
                          'aaksejhfkasehfksdfsa')

    def test_normal_quotes(self):
        quotes = wikiquote.quotes('The Matrix (film)')
        self.assertTrue(len(quotes) > 0)

    def test_max_quotes(self):
        quotes = wikiquote.quotes('The Matrix (film)', max_quotes = 8)
        self.assertEqual(len(quotes), 8)

    def test_is_cast_credit(self):
      cast1 = 'Bryan Cranston - Walter White'.split()
      cast2 = 'Giancarlo Esposito - Gustavo "Gus" Fring'.split()

      self.assertTrue(wikiquote.is_cast_credit(cast1))
      self.assertTrue(wikiquote.is_cast_credit(cast2))
