import wikiquote
import unittest


class SearchTest(unittest.TestCase):
    """
    Test wikiquote.search()
    """

    def test_search(self):
        for lang in wikiquote.supported_languages():
            results = wikiquote.search("Matrix", lang=lang)
            self.assertTrue(len(results) > 0)

    def test_unsupported_lang(self):
        with self.assertRaisesRegex(
            wikiquote.UnsupportedLanguageException, "Unsupported language: foobar"
        ):
            wikiquote.search("test", lang="foobar")

    def test_empty_search(self):
        results = wikiquote.search("")
        self.assertEqual(results, [])
