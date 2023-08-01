# Documentation

## Project Structure
This project consists of multiple Python modules that work together to provide a simple API for fetching quotes from Wikiquote.

```angular2html
wikiquote/
├── tests/
│   ├── test_qotd.py
│   ├── test_quotes.py
│   ├── test_random_titles.py
│   ├── test_search.py
│   ├── test_supported_langs.py
├── util/
│   ├── manual_checks.py
├── wikiquote/
│   ├── langs/
│   │   ├── de.py
│   │   ├── en.py
│   │   ├── ...
│   ├── constants.py
│   ├── qotd.py
│   ├── quotes.py
│   ├── utils.py
├── .gitignore
├── LICENSE
├── README.md
├── requirements.txt
├── setup.py
```

### Overview of Modules

- `tests/`: This directory contains the unit tests for the Wikiquote API. Each test file corresponds to a module in the wikiquote directory, and each test function corresponds to a function in the corresponding module. Python's built-in unittest module is used throughout.


- `util/`: This directory contains only one utility, `manual_checks.py`, which is used to manually check the output of the API functions. It is not used in the main API. It could be expanded in a future release.


- `wikiquote/`: This directory contains the main API modules.
  - `qotd.py`: This module contains the `quote_of_the_day` function. When given a language (default is English), it returns a tuple with the quote of the day and its author from the Wikiquote page of the corresponding language. It communicates with utils.py to validate the language and fetch data, and langs.py to parse the fetched data.
  - `quotes.py`: This module contains the functions `search`, `quotes`, and `random_titles`, which are the main features of the API.
    - `search` function takes a string and an optional language as arguments and returns a list of page titles matching the query.
    - `quotes` fetches a list of quotes from the specified page
    - `random_titles` fetches a list of random titles from Wikiquote in the specified language 


- `utils.py`: The module contains various helper functions and exception classes that are used throughout the project, primarily `extract_quotes_li` and `fetch_data`
  - `fetch_data` takes a URL and returns the HTML tree from the corresponding page
  - `extract_quotes_li` takes an HTML tree from a Wikiquote page and returns a list of quotes from the tree 
  - constants.py: constants used in the project:
  ```
      DEFAULT_LANG = "en"
      DEFAULT_MAX_QUOTES = 20
      MIN_QUOTE_LEN = 6
      MIN_QUOTE_WORDS = 3
  ```
- `langs/`: This directory contains `qotd` and `extract_quotes` functions for each langauge. These functions are called by the `qotd` and `quotes` functions in the main API. The functions are named after the corresponding language code. The current langauges are supported: `de`, `en`, `es`, `fr`, `it`, `nl`, `pl`, `pt`, `ru`, `zh`.

## Current State
The current state of the Wikiquote API allows for basic extraction of quotes from a given page in multiple languages. It allows users to fetch the quote of the day, search for quotes by string or title, fetch random titles, and extract quotes from specified Wikiquote pages.

## Usage

### Fetching a New Quote (English)

To obtain a list of quotes:

```python

import wikiquote

# Fetch quotes from Albert Einstein's Wikiquote page 
# https://en.wikiquote.org/wiki/Albert_Einstein
einstein_quotes = wikiquote.quotes("Albert Einstein")

for quote in einstein_quotes[:3]:
    print(quote)

# Information is not knowledge. The only source of knowledge is experience.
# Nuclear power is a hell of a way to boil water
# Computers are incredibly fast, accurate and stupid; humans are incredibly slow, inaccurate and brilliant; together they are powerful beyond imagination.

```
