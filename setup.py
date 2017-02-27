from distutils.core import setup

setup(
  name = 'wikiquote',
  packages = ['wikiquote', 'wikiquote.langs'],
  version = '0.1.5',
  description = 'Retrieve quotes from any Wikiquote page.',
  author = 'Federico Tedin',
  author_email = 'federicotedin@gmail.com',
  install_requires = ['lxml'],
  url = 'https://github.com/federicotdn/python-wikiquotes',
  download_url = 'https://github.com/federicotdn/python-wikiquotes/archive/0.1.5.tar.gz',
  keywords = ['quotes', 'wikiquote', 'python', 'api', 'qotd'],
  license = 'MIT',
  classifiers = [
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'License :: OSI Approved :: MIT License'
  ],
)
