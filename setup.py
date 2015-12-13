from distutils.core import setup

setup(
  name = 'wikiquote',
  py_modules = ['wikiquote'],
  version = '0.1.2',
  description = 'Retrieve quotes from any Wikiquote page.',
  author = 'Federico Tedin',
  author_email = 'federicotedin@gmail.com',
  install_requires = ['lxml'],
  url = 'https://github.com/federicotdn/python-wikiquotes',
  download_url = 'https://github.com/federicotdn/python-wikiquotes/tarball/0.1.2',
  keywords = ['quotes', 'wikiquote', 'python', 'api', 'qotd'],
  license = 'MIT',
  classifiers = [],
)
