import wikiquote
import unittest


class SearchTest(unittest.TestCase):
    """
    Test wikiquote.search()
    """

    def test_search(self):
        for lang in wikiquote.langs.SUPPORTED_LANGUAGES:
            results = wikiquote.search('Matrix', lang=lang)
            self.assertTrue(len(results) > 0)

    def test_unsupported_lang(self):
        self.assertRaises(wikiquote.utils.UnsupportedLanguageException,
                          wikiquote.search,
                          'Matrix',
                          lang='foobar')

    def test_empty_search(self):
        results = wikiquote.search('')
        self.assertEqual(results, [])
