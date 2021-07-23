import wikiquote
import unittest


class SupportedLangsTest(unittest.TestCase):
    """
    Test wikiquote.supported_languages()
    """

    def test_supported_languages(self):
        # Check that all language modules are being loaded
        self.assertListEqual(
            wikiquote.supported_languages(),
            ["de", "en", "es", "eu", "fr", "he", "it", "pl", "pt"],
        )
