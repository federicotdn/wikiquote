# python-wikiquotes
Retrieve quotes from any Wikiquote.org page, with Python 3 (inspired by the `wikipedia` module).  Uses the `lxml` module to parse HTML.  Quotes are not always found correctly because of Wikiquote's varying page layouts.  Contributions are welcome.

## Usage
```python
>>> import wikiquote

>>> wikiquote.search('Fight Club')
# ['Fight Club', 'Fight Club (film)', 'Main Page', 'Chuck Palahniuk', 'Fight Club (novel)']

>>> wikiquote.quotes('Fight Club (film)', 4) # will return 4 quotes, default is 20
# ['On a long enough time line, the survival rate for everyone drops to zero.', 'I felt like destroying something beautiful.', "I am Jack's wasted life.", "I am Jack's smirking revenge."]
```

Some page titles will lead to a Disambiguation page (like `Matrix`), which will raise a `DisambiguationPageException` exception.  If the page does not exist, a `NoSuchPageException` will be raised instead.

## Tips
Use `random.choice()` to select a random quote:
```python
>>> import wikiquote, random

>>> random.choice(wikiquote.quotes('Dune'))
# 'Hope clouds observation.'
```

## TODO
Improve the way quotes are searched for in the HTML page, avoid returning things like external references, links or notes from quotes.
