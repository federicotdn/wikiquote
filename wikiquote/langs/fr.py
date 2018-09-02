from .. import utils

MAIN_PAGE = "Wikiquote:Accueil"


def extract_quotes(tree, max_quotes):
    # French wiki uses a "citation" HTML class
    nodes = tree.xpath('//div[@class="citation"]')
    quotes = [utils.clean_txt(node.text_content()) for node in nodes]
    return quotes[:max_quotes]


def qotd(html_tree):
    # French QOTD not available
    # TODO: Re-enable when QOTD appears again on welcome page
    # Note added on 2018/09/02
    raise utils.UnsupportedLanguageException(
        'Quote of the day not available for lang="fr".')
