import wikiquote

# manual_checks.py
# A short script to manually test wikiquote's functionality

MAX_QUOTE_LEN = 70

articles = [
    'Barack Obama',
    'Albert Einstein',
    'Ada Lovelace',
    'Leonard Cohen'
]

for lang in wikiquote.supported_languages():
    print('\n----------------------------------------------------')
    print('\nLanguage: {}'.format(lang))
    print('\n----------------------------------------------------\n')

    print('QOTD:')
    try:
        qotd, author = wikiquote.quote_of_the_day(lang=lang)
        print(qotd)
        print('   by: {}'.format(author))
    except Exception as e:
        print(e)

    for article in articles:
        print('\nArticle: {}'.format(article))
        try:
            results = wikiquote.search(article, lang=lang)

            if results:
                print('Results:')
                for result in results:
                    print(' - {}'.format(result))
                print()

                quotes = wikiquote.quotes(results[0], lang=lang, max_quotes=10)
                if quotes:
                    for quote in quotes:
                        if len(quote) > MAX_QUOTE_LEN:
                            quote = quote[:MAX_QUOTE_LEN] + '...'
                            print(' - {}'.format(quote))
                else:
                    print('NO QUOTES!')
            else:
                print('NO RESULTS!')
        except Exception as e:
            print(e)
