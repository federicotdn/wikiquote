import pytest
import wikiquote


# def test_disambiguation():
#     """Test that a disambiguation page raises an exception is raised when appropriate."""
#     with pytest.raises(wikiquote.DisambiguationPageException):
#         wikiquote.quotes("Matrix")
#
#
# def test_no_such_page():
#     """Test that a no such page exception is raised when appropriate."""
#     with pytest.raises(wikiquote.utils.NoSuchPageException):
#         wikiquote.quotes("foobarfoobar")
#
#
# def test_unsupported_lang():
#     """Test that an exception is raised when an unsupported language is passed."""
#     with pytest.raises(wikiquote.UnsupportedLanguageException, match="Unsupported language: foobar"):
#         wikiquote.quotes("Matrix", lang="foobar")
#
#
# @pytest.mark.parametrize(
#     "lang, query",
#     [("en", "Barack Obama"), ("he", "ברק אובמה"), ("es", "Simón Bolívar"), ("fr", "Victor Hugo")],
# )
# def test_quotes_valid_lang_page(lang, query):
#     """Test that quotes are returned when working arguments are passed."""
#     quotes = wikiquote.quotes(query, lang=lang)
#     assert len(quotes) > 0, f"No quotes found for {query} in {lang}."
#
#
# @pytest.mark.parametrize(
#     "lang, query",
#     [("en", "foobar1"), ("he", "foobar2"), ("es", "foobar3"), ("fr", "foobar4")]
# )
# def test_quotes_invalid_lang_page(lang, query):
#     """Test that an exception is raised when an invalid page is passed."""
#     with pytest.raises(wikiquote.utils.NoSuchPageException):
#         wikiquote.quotes(query, lang=lang)
#
#
# def test_max_quotes():
#     """Test that the max_quotes argument returns the correct number of quotes."""
#     quotes = wikiquote.quotes("The Matrix (film)", max_quotes=8)
#     assert len(quotes) == 8
#
#
# def test_max_quotes_and_lang():
#     """Test that the max_quotes argument returns the correct number of quotes when a language is specified."""
#     quotes = wikiquote.quotes("Matrix", lang="fr", max_quotes=8)
#     assert len(quotes) == 8


def test_valid_search():
    """Test that a valid search returns a list of results containing the query"""
    query = "Albert Einstein"
    results = wikiquote.search(query)
    assert isinstance(results, list)
    assert query in results


def test_invalid_search():
    """Test that an invalid search returns a list of results not containing the query"""
    query = "foobar1"
    results = wikiquote.search(query)
    assert isinstance(results, list)
    assert query not in results


def test_empty_search():
    """Test that an empty search returns an empty list"""
    # Test that an empty search returns an empty list
    assert wikiquote.search("") == []

    # Test that an empty search (None) raises a TypeError
    with pytest.raises(TypeError):
        assert wikiquote.search() == []


def test_valid_random_titles():
    """Test that a valid random_titles returns a list of results equal in length to the max_titles argument"""
    num_titles = 5
    titles = wikiquote.random_titles(max_titles=num_titles)
    assert len(titles) == num_titles


@pytest.mark.xfail(reason="This test is expected to fail because we are requesting more quotes than exist for the page.")
def test_max_quotes_exceed_limit():
    """Test requesting more quotes than exist for a page returns the maximum number of quotes."""
    query = "Albert Einstein"
    all_quotes = wikiquote.quotes(query)
    num_all_quotes = len(all_quotes)
    excessive_quotes = wikiquote.quotes(query, max_quotes=num_all_quotes + 1)
    assert len(excessive_quotes) == num_all_quotes


@pytest.mark.parametrize(
    "input_value",
    [123, [], {}, 12.34, None]
)
def test_invalid_inputs(input_value):
    """Test various non-string inputs to ensure they raise the standard TypeError."""
    with pytest.raises(TypeError):
        wikiquote.search(input_value)

    with pytest.raises(TypeError):
        wikiquote.quotes(input_value)

    with pytest.raises(TypeException):
        wikiquote.random_titles(lang=input_value)