import wikiquote
import unittest

class SearchTest(unittest.TestCase):
    """
    Test wikiquote.search()
    """

    def test_search(self):
        results = wikiquote.search('Matrix')
        self.assertTrue(len(results) > 0)

    def test_empty_search(self):
        results = wikiquote.search('')
        self.assertEqual(results, [])