# python-wikiquotes
[![Build Status](https://travis-ci.org/federicotdn/python-wikiquotes.svg?branch=travis)](https://travis-ci.org/federicotdn/python-wikiquotes)
![License](http://img.shields.io/pypi/l/wikiquote.svg?style=flat)
[![Version](http://img.shields.io/pypi/v/wikiquote.svg?style=flat)](https://pypi.python.org/pypi/wikiquote)

Retrieve quotes from any Wikiquote.org page, or the quote of the day, with Python 3 (inspired by the `wikipedia` module).  Uses the `lxml` module to parse HTML.  Quotes are not always found correctly because of Wikiquote's varying page layouts.  Contributions are welcome.

## Usage
```python
>>> import wikiquote

>>> wikiquote.search('Dune')
# ['Dune', 'Frank Herbert', 'Children of Dune (TV miniseries)', 'Dune (film)', 'Dune (TV miniseries)']

>>> wikiquote.quotes('Dune', max_quotes = 3) # max_quotes defaults to 20
# ['A popular man arouses the jealousy of the powerful.', 'Parting with friends is a sadness. A place is only a place.', 'Hope clouds observation.']

>>> wikiquote.quote_of_the_day() # returns a (quote, author) tuple
# 'Always forgive your enemies; nothing annoys them so much.', 'Oscar Wilde'

>>> wikiquote.random_titles(max_titles = 3) # max_titles defaults to 20
# ['Dune', 'Johannes Kepler', 'Rosa Parks']

>>> wikiquote.supported_languages()
# ['en', 'es', 'fr']

```

Some page titles will lead to a Disambiguation page (like `Matrix`), which will raise a `DisambiguationPageException` exception.  If the page does not exist, a `NoSuchPageException` will be raised instead.

## Tips
Use `random.choice()` to select a random quote from a single page:
```python
>>> import wikiquote, random

>>> random.choice(wikiquote.quotes('Linus Torvalds'))
# 'WE DO NOT BREAK USERSPACE!'
```

## Languages
The `wikiquote` module currently works for the English, Spanish and French versions of Wikiquote.org.  Use the `lang` parameter to specify the language: `en`, `es`, or `fr` (defaults to `en`).
```python
>>> import wikiquote

>>> wikiquote.search('Dune', lang='fr')
# ['Dune', 'Les Enfants de Dune', 'Les Hérétiques de Dune', 'Le Messie de Dune']

>>> wikiquote.quotes('Dune', lang='fr')[0]
# 'Si les vœux étaient des poissons, nous lancerions tous des filets.'

>>> wikiquote.quote_of_the_day(lang='fr')
# '50 pour cent de toutes les éditions faites sur Wikipédia sont réalisées par seulement 0,7% des utilisateurs', 'Jimmy Wales'

>>> wikiquote.quotes('Nueve reinas', lang='es')[0]
# 'Más ofendido estás... menos sospechoso pareces.'

>>> wikiquote.quote_of_the_day(lang='es')
# 'El universo no fue hecho a medida del hombre; tampoco le es hostil: es indiferente.', 'Carl Edward Sagan'

```

## Developing / Testing
Check that all tests pass:
```bash
$ python3 -m unittest -v
```
Check that the `wikiquote` package follows the PEP8 conventions ([pep8](https://github.com/jcrocholl/pep8) required):
```bash
$ pep8 wikiquote
```

## TODO
- Improve the way quotes are searched for in the HTML page, avoid returning things like external references, links or notes from quotes.
- Add more/better tests.
- Add support for more languages: each language may require a different scrapping method.
