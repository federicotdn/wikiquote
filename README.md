[![Build Status](https://travis-ci.org/federicotdn/python-wikiquotes.svg?branch=travis)](https://travis-ci.org/federicotdn/python-wikiquotes)
![License](https://img.shields.io/badge/license-MIT-blue.svg)

# python-wikiquotes
Retrieve quotes from any Wikiquote.org page, with Python 3 (inspired by the `wikipedia` module).  Uses the `lxml` module to parse HTML.  Quotes are not always found correctly because of Wikiquote's varying page layouts.  Contributions are welcome.

## Usage
```python
>>> import wikiquote

>>> wikiquote.search('Dune')
# ['Dune', 'Frank Herbert', 'Children of Dune (TV miniseries)', 'Dune (film)', 'Dune (TV miniseries)']

>>> wikiquote.quotes('Dune', max_quotes = 3) # max_quotes defaults to 20
# ['A popular man arouses the jealousy of the powerful.', 'Parting with friends is a sadness. A place is only a place.', 'Hope clouds observation.']
```

Some page titles will lead to a Disambiguation page (like `Matrix`), which will raise a `DisambiguationPageException` exception.  If the page does not exist, a `NoSuchPageException` will be raised instead.

## Tips
Use `random.choice()` to select a random quote:
```python
>>> import wikiquote, random

>>> random.choice(wikiquote.quotes('Linus Torvalds'))
# 'WE DO NOT BREAK USERSPACE!'
```

## TODO
- Improve the way quotes are searched for in the HTML page, avoid returning things like external references, links or notes from quotes.
- Quote of the day.
- ~~Further PEP8 formatting.~~ (done, checked with [pep8](https://github.com/jcrocholl/pep8))
