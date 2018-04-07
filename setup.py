from distutils.core import setup

setup(
    name = 'wikiquote',
    packages = ['wikiquote', 'wikiquote.langs'],
    version = '0.1.7',
    description = 'Retrieve quotes from any Wikiquote page.',
    author = 'Federico Tedin',
    author_email = 'federicotedin@gmail.com',
    install_requires = [
        'lxml>=4.2, <5.0'
    ],
    url = 'https://github.com/federicotdn/python-wikiquotes',
    download_url = 'https://github.com/federicotdn/python-wikiquotes/archive/0.1.7.tar.gz',
    keywords = ['quotes', 'wikiquote', 'python', 'api', 'qotd', 'quote', 'day'],
    license = 'MIT',
    classifiers = [
        'Programming Language :: Python :: 3 :: Only',
        'License :: OSI Approved :: MIT License',
        'Topic :: Utilities'
    ]
)
