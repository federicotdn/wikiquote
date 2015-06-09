import wikiquote
import unittest

class CategoryTest(unittest.TestCase):
    """
    Test wikiquote.category_members() and wikiquote.explore_category()
    """

    def test_subcat(self):
        subcats = wikiquote.category_members('Category:Action films')
        self.assertTrue(len(list(subcats)) > 0)

    def test_lang(self):
        subcats = wikiquote.category_members('Catégorie:Kaamelott',
                                             lang='fr',
                                             command='page')
        self.assertTrue(len(list(subcats)) > 0)

    def test_pages(self):
        subcats = wikiquote.category_members('Category:James Bond 007',
                                             command='page')
        self.assertTrue(len(list(subcats)) > 0)

    def text_explore(self):
        quote_index = wikiquote.explore_category('Category:Samurai films')
        self.assertTrue(len(quote_index) > 0)
