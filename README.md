# python-wikiquotes
[![Build Status](https://travis-ci.org/federicotdn/python-wikiquotes.svg?branch=travis)](https://travis-ci.org/federicotdn/python-wikiquotes)
![License](https://pypip.in/license/wikiquote/badge.svg?style=flat)
[![Downloads](https://pypip.in/download/wikiquote/badge.svg?style=flat)](https://pypi.python.org/pypi/wikiquote)

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

```

Some page titles will lead to a Disambiguation page (like `Matrix`), which will raise a `DisambiguationPageException` exception.  If the page does not exist, a `NoSuchPageException` will be raised instead.

## Tips
Use `random.choice()` to select a random quote:
```python
>>> import wikiquote, random

>>> random.choice(wikiquote.quotes('Linus Torvalds'))
# 'WE DO NOT BREAK USERSPACE!'
```

## Developing / Testing
Check that all tests pass:
```bash
$ python3 -m unittest -v
```
Check that `wikiquote.py` follows the PEP8 conventions ([pep8](https://github.com/jcrocholl/pep8) required):
```bash
$ pep8 wikiquote.py
```

## TODO
- Improve the way quotes are searched for in the HTML page, avoid returning things like external references, links or notes from quotes.
- Add more/better tests.
