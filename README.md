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

>>> james_bond_quote_index = wikiquote.explore_category('Category:James Bond 007')

>>> wikiquote.random_quote_from_categories(james_bond_quote_index)
#("James Bond: Sir! They're not going to do anything! I owe it to Leiter. He's put his life on the line for me many times.", 'License to Kill')

```

Some page titles will lead to a Disambiguation page (like `Matrix`), which will raise a `DisambiguationPageException` exception.  If the page does not exist, a `NoSuchPageException` will be raised instead.

## Tips
While `random_quote_from_categories` works perfectly, it needs a very slow pre-indexing using `explore_category`. If you can use something else, do it.
Use `random.choice()` to select a random quote froma single page:
```python
>>> import wikiquote, random

>>> random.choice(wikiquote.quotes('Linus Torvalds'))
# 'WE DO NOT BREAK USERSPACE!'
```

## Language
Wikiquote.org has multiple languages:
Currently supported languages are english and french.
Use parameter lang if you want a quote in french
```python
>>> import wikiquote

>>> wikiquote.quotes('Dune')[0]
#"A beginning is the time for taking the most delicate care that the balances are correct. This every sister of the Bene Gesserit knows. To begin your study of the life of Muad'Dib, then take care that you first place him in his time: born in the 57th year of the Padishah Emperor, Shaddam IV. And take the most special care that you locate Muad'Dib in his place: the planet Arrakis. Do not be deceived by the fact that he was born on Caladan and lived his first fifteen years there. Arrakis, the planet known as Dune, is forever his place."


>>> wikiquote.quotes('Dune',lang='fr')[0]
#"Je ne connaîtrai pas la peur, car la peur tue l'esprit. La peur est la petite mort qui conduit à l'oblitération totale. J'affronterai ma peur. Je lui permettrai de passer sur moi, au travers de moi. Et lorsqu'elle sera passée, je tournerai mon œil intérieur sur son chemin. Et là où elle sera passée, il n'y aura plus rien. Rien que moi."
```

### French specific functions
Some quotes from the french Wikiquotes are traductions from other languages and come with their original quote.
Use `quotes_fr_original` to get both quotes:
```python
>>> import wikiquote

>>> wikiquote.quotes_fr_original('scarface')[6]
('Dis bonjour à mon ami !', 'Say hello to my little friend!!')
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
