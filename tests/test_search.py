import wikiquote
import unittest

from collections import defaultdict


class SearchTest(unittest.TestCase):
    """
    Test wikiquote.search()
    """

    def test_search(self):

        query_by_lang = defaultdict(lambda: 'Matrix')
        special_cases = {
            # The hebrew wikiquote doesn't support searches in English
            'he': 'מטריקס',
        }

        query_by_lang.update(special_cases)

        for lang in wikiquote.supported_languages():
            results = wikiquote.search(query_by_lang[lang], lang=lang)
            self.assertTrue(len(results) > 0)

    def test_unsupported_lang(self):
        with self.assertRaisesRegex(
            wikiquote.UnsupportedLanguageException, "Unsupported language: foobar"
        ):
            wikiquote.search("test", lang="foobar")

    def test_empty_search(self):
        results = wikiquote.search("")
        self.assertEqual(results, [])
