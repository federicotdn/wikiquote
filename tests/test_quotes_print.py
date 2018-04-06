import wikiquote
import unittest
import logging

logger = logging.getLogger(__name__)

MAX_LEN = 140

ARTICLES = [
    'The Matrix (film)',
    'Dune',
    'The Lion King',
    'Linus Torvalds',
    'Ada Lovelace',
    'Albert Einstein',
    'Anonymous'
]

# Similar to QuotesTest, except results are logged to stdout
# when module is run as __main__
# Useful for manually checking if quotes are being returned correctly
class QuotesPrintTest(unittest.TestCase):
    """
    Test wikiquote.quotes()
    """
    def test_quotd_all_langs(self):
        logger.info('\n========= QOTD =========\n')
        for lang in wikiquote.supported_languages():
            logger.info(lang.upper() + ':')
            quote, author = wikiquote.quote_of_the_day(lang=lang)
            logger.info('- quote: ' + quote)
            logger.info('- author: ' + author)

            self.assertTrue(len(quote) > 0 and len(author) > 0)

    def test_max_quotes(self):
        for article in ARTICLES:
            logger.info('\n========= ' + article.upper() + ' =========\n')

            quotes = wikiquote.quotes(article, max_quotes=10000)
            self.assertTrue(len(quotes) > 0)

            for quote in quotes:
                if len(quote) > MAX_LEN:
                    diff = len(quote) - MAX_LEN
                    begin = quote[:MAX_LEN] + '...'
                    end = '...' + quote[diff:]
                    logger.info('- ' + begin)
                    logger.info('    ' + end)
                else:
                    logger.info('- ' + quote)

if __name__ == '__main__':
    logger.setLevel(logging.DEBUG)

    ch = logging.StreamHandler()
    formatter = logging.Formatter('%(message)s')
    ch.setFormatter(formatter)
    ch.setLevel(logging.DEBUG)

    logger.addHandler(ch)
    unittest.main()