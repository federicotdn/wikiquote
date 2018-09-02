# python-wikiquotes
[![Build Status](https://travis-ci.org/federicotdn/python-wikiquotes.svg?branch=travis)](https://travis-ci.org/federicotdn/python-wikiquotes)
![License](https://img.shields.io/pypi/l/wikiquote.svg?style=flat)
[![Version](https://img.shields.io/pypi/v/wikiquote.svg?style=flat)](https://pypi.python.org/pypi/wikiquote)

The `wikiquote` Python module allows you to search and retrieve quotes from any [Wikiquote](https://www.wikiquote.org/) article, and also retrieve the quote of the day. Please keep in mind that due to Wikiquote's varying HTML page layouts, some quotes may not be retrieved correctly. If you wish to collaborate, head over to the [Developing](https://github.com/federicotdn/python-wikiquotes#developing) section below. 

## Installation
You can install the `wikiquote` module using `pip`:
```bash
$ pip3 install --upgrade wikiquote
```

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
# ['The Lion King', 'Johannes Kepler', 'Rosa Parks']

>>> wikiquote.supported_languages()
# ['de', 'en', 'es', 'fr', 'it']

```

Some page titles will lead to a Disambiguation page (like `Matrix`), which will raise a `DisambiguationPageException` exception.  If the page does not exist, a `NoSuchPageException` will be raised instead.

## Languages
The `wikiquote` module currently supports the following languages:

| Language | ISO 639-1 Code |
|----------|----------------|
| English  | `en`           |
| Spanish  | `es`           |
| German   | `de`           |
| French   | `fr`           |
| Italian  | `it`           |

Use the `lang` parameter to specify the language (defaults to `en`):
```python
>>> import wikiquote

>>> wikiquote.search('Dune', lang='fr')
# ['Dune', 'Les Enfants de Dune', 'Les Hérétiques de Dune', 'Le Messie de Dune']

>>> wikiquote.quotes('Dune', lang='fr')[0]
# 'Si les vœux étaient des poissons, nous lancerions tous des filets.'

>>> wikiquote.quotes('Nueve reinas', lang='es')[0]
# 'Más ofendido estás... menos sospechoso pareces.'

>>> wikiquote.quote_of_the_day(lang='es')
# 'El universo no fue hecho a medida del hombre; tampoco le es hostil: es indiferente.', 'Carl Edward Sagan'

>>> wikiquote.quotes('Hermann Hesse', lang='de')[0]
# 'Nun, aller höhere Humor fängt damit an, daß man die eigene Person nicht mehr ernst nimmt.'

>>> wikiquote.quote_of_the_day(lang='it')
# "Siamo angeli con un'ala sola. Possiamo volare solo restando abbracciati.", 'Luciano De Crescenzo'
```

## Tips
Use `random.choice()` to select a random quote from a single page:
```python
>>> import wikiquote, random

>>> random.choice(wikiquote.quotes('Linus Torvalds'))
# 'WE DO NOT BREAK USERSPACE!'
```

## Developing
First, check that all tests pass:
```bash
$ python3 -m unittest -v
```
After that, check that the `wikiquote` package follows the PEP 8 conventions ([pycodestyle](https://github.com/PyCQA/pycodestyle) required):
```bash
$ pycodestyle wikiquote tests
```
Finally, create a pull request stating your changes.

## TODO
- Improve the way quotes are searched for in the HTML page, avoid returning things like external references, links or notes from quotes.
- Add more/better tests (for example, check that returned quotes do not contain characters like '(' or ')').
- Add support for more languages: each language may require a different scrapping method.
