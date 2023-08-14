import pytest
import wikiquote

from collections import defaultdict


def test_disambiguation():
    """Test that a disambiguation page raises an exception is raised when appropriate."""
    with pytest.raises(wikiquote.DisambiguationPageException):
        wikiquote.quotes("Matrix")


def test_no_such_page():
    """Test that a no such page exception is raised when appropriate."""
    with pytest.raises(wikiquote.utils.NoSuchPageException):
        wikiquote.quotes("foobarfoobar")


def test_unsupported_lang():
    """Test that an exception is raised when an unsupported language is passed."""
    with pytest.raises(wikiquote.UnsupportedLanguageException, match="Unsupported language: foobar"):
        wikiquote.quotes("Matrix", lang="foobar")


def test_normal_quotes():
    """Test that quotes are returned when working arguments are passed."""
    query_by_lang = defaultdict(lambda: "Barack Obama")
    # Special case: The Hebrew wikiquote doesn't support searches in English
    query_by_lang["he"] = "ברק אובמה"
    # Special case: The Basque wikiquote doesn't have a page for Barack Obama
    query_by_lang["eu"] = "Simón Bolívar"

    for lang in wikiquote.supported_languages():
        quotes = wikiquote.quotes(query_by_lang[lang], lang=lang)
        assert len(quotes) > 0


def test_max_quotes():
    """Test that the max_quotes argument returns the correct number of quotes."""
    quotes = wikiquote.quotes("The Matrix (film)", max_quotes=8)
    assert len(quotes) == 8


def test_max_quotes_and_lang():
    """Test that the max_quotes argument returns the correct number of quotes when a language is specified."""
    quotes = wikiquote.quotes("Matrix", lang="fr", max_quotes=8)
    assert len(quotes) == 8
