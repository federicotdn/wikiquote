# wikiquote
[![CI Status](https://github.com/federicotdn/wikiquote/workflows/CI/badge.svg)](https://github.com/federicotdn/wikiquote/actions)
![License](https://img.shields.io/pypi/l/wikiquote.svg?style=flat)
![](https://img.shields.io/badge/python-3-blue.svg)
[![Version](https://img.shields.io/pypi/v/wikiquote.svg?style=flat)](https://pypi.python.org/pypi/wikiquote)
![Black](https://img.shields.io/badge/code%20style-black-000000.svg)

The `wikiquote` package for Python (>=3.8) allows you to search and retrieve quotes from any [Wikiquote](https://www.wikiquote.org/) article, as well as retrieve the quote of the day.

## Installation
You can install the `wikiquote` package using, for example, `pip`:
```bash
$ pip install --upgrade wikiquote
```

## Usage
```python
>>> import wikiquote

>>> wikiquote.search('The Matrix')
# ['The Matrix (film)', 'The Matrix Revolutions', 'The Matrix Reloaded', 'The Animatrix']

>>> wikiquote.quotes('The Matrix (film)', max_quotes=2) # max_quotes defaults to 20
# ['Don't think you are, know you are.', 'Fate, it seems, is not without a sense of irony.']

>>> wikiquote.quote_of_the_day() # returns a (quote, author) tuple
# 'Always forgive your enemies; nothing annoys them so much.', 'Oscar Wilde'

>>> wikiquote.qotd() # same as quote_of_the_day()

>>> wikiquote.random_titles(max_titles=3) # max_titles defaults to 20
# ['The Lion King', 'Johannes Kepler', 'Rosa Parks']

>>> wikiquote.supported_languages()
# ['de', 'en', 'es', 'eu', 'fr', 'he', 'it', 'pl', 'pt']

```

Some article titles will lead to a Disambiguation page (like `Matrix`), which will raise a `DisambiguationPageException` exception. Usually this happens because there are many articles matching the search term. When this happens, try using `search()` first, and then use one of the specific article titles found.

If the article searched for does not exist, and no similar results exist, `NoSuchPageException` will be raised instead.

When requesting the quote of the day, a `MissingQOTDException` exception will be raised if the quote of the day could not be extracted from Wikiquote's main page. This usually happens because the page's layout has been changed.

## Languages
The `wikiquote` module currently supports the following languages:

| Language   | ISO 639-1 Code |
|------------|----------------|
| Basque     | `eu`           |
| English    | `en`           |
| French     | `fr`           |
| German     | `de`           |
| Hebrew     | `he`           |
| Italian    | `it`           |
| Polish     | `pl`           |
| Portuguese | `pt`           |
| Spanish    | `es`           |

Use the `lang` parameter to specify the language (defaults to `en`):
```python
>>> import wikiquote

>>> wikiquote.quotes('Dune', lang='en')[0]
# 'Parting with friends is a sadness. A place is only a place.'

>>> wikiquote.quotes('Victor Hugo', lang='fr')[0]
# 'Le plus lourd fardeau, c'est d'exister sans vivre.'

>>> wikiquote.quotes('Nueve reinas', lang='es')[0]
# 'Más ofendido estás... menos sospechoso parecés.'

>>> wikiquote.quote_of_the_day(lang='es')
# 'He sospechado alguna vez que la única cosa sin misterio es la felicidad, porque se justifica por sí sola.', 'Jorge Luis Borges'

>>> wikiquote.quotes('Hermann Hesse', lang='de')[0]
# 'Nun, aller höhere Humor fängt damit an, daß man die eigene Person nicht mehr ernst nimmt.'

>>> wikiquote.quote_of_the_day(lang='it')
# "Siamo angeli con un'ala sola. Possiamo volare solo restando abbracciati.", 'Luciano De Crescenzo'

>>> wikiquote.quote_of_the_day(lang='pl')
# 'Boże pomóż mi być takim człowiekiem, za jakiego uważa mnie mój pies.', 'Janusz Leon Wiśniewski'

>>> wikiquote.quotes('José Saramago', lang='pt')[0]
# 'Nem a juventude sabe o que pode, nem a velhice pode o que sabe.'
```

Specifying an invalid language will result in an `UnsupportedLanguageException` exception.

## Tips
Use `random.choice()` to select a random quote from an article:
```python
>>> import wikiquote, random

>>> random.choice(wikiquote.quotes('Linus Torvalds'))
# 'WE DO NOT BREAK USERSPACE!'
```

## Caveats
In some cases, `wikiquote` may fail to retrieve quotes from some articles, or the quote of the day (QOTD). This is due to Wikiquote.org's varying internal article layouts: some quotes may be contained in `div` elements, others in `li`, etc. depending on the article and the language.

## Developing
[Poetry](https://python-poetry.org/) is required to develop `wikiquote`.

First, make sure you have installed all necessary dependencies, including development dependencies:
```bash
$ poetry install
```

Then, check that all files are correctly formatted, and that the type hints are also correct:
```bash
$ poetry run make lint
$ poetry run make install-types
$ poetry run make types
```

After that, check that all tests pass:
```bash
$ poetry run make test
```
Some tests may be skipped in the QOTD is not available for some languages.

Finally, create a pull request stating your changes.

## Changelog
See the [CHANGELOG.md](CHANGELOG.md) file.

## License
The `wikiquote` package is licensed under the MIT License.
