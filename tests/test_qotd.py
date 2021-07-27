"""
Test wikiquote.quote_of_the_day()
"""
import pytest

import wikiquote


@pytest.mark.parametrize("lang", wikiquote.supported_languages())
def test_qotd_quote(lang):
    try:
        quote, _ = wikiquote.quote_of_the_day(lang=lang)
    except wikiquote.MissingQOTDException:
        pytest.skip("No QOTD for {lang}".format(lang=lang))

    assert isinstance(quote, str)
    assert len(quote) > 0


def test_unsupported_lang():
    with pytest.raises(wikiquote.UnsupportedLanguageException):
        wikiquote.quote_of_the_day(lang="foobar")


@pytest.mark.parametrize("lang", wikiquote.supported_languages())
def test_qotd_author(lang):
    try:
        _, author = wikiquote.quote_of_the_day(lang=lang)
    except wikiquote.MissingQOTDException:
        pytest.skip("No QOTD for {lang}".format(lang=lang))

    assert isinstance(author, str)
    assert len(author) > 0


def test_qotd_qotd():
    assert wikiquote.quote_of_the_day() == wikiquote.qotd()
