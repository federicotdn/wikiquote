import wikiquote
import unittest


class SearchTest(unittest.TestCase):
    """
    Test wikiquote.random_titles()
    """

    def test_random(self):
        for lang in wikiquote.supported_languages():
            results = wikiquote.random_titles(lang=lang, max_titles=20)
            self.assertTrue(len(results) == 20)

    def test_unsupported_lang(self):
        with self.assertRaisesRegex(
            wikiquote.UnsupportedLanguageException, "Unsupported language: foobar"
        ):
            wikiquote.random_titles(lang="foobar")
