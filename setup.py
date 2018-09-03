from distutils.core import setup

with open('requirements.txt') as f:
    requires = f.read().splitlines()

setup(
    name='wikiquote',
    packages=['wikiquote', 'wikiquote.langs'],
    version='0.1.8',
    description='Retrieve quotes from any Wikiquote article.',
    author='Federico Tedin',
    author_email='federicotedin@gmail.com',
    install_requires=requires,
    url='https://github.com/federicotdn/python-wikiquotes',
    download_url='https://github.com/federicotdn/python-wikiquotes/archive/0.1.8.tar.gz',
    keywords=['quotes', 'wikiquote', 'python', 'api', 'qotd', 'quote', 'day'],
    license='MIT',
    classifiers=[
        'Programming Language :: Python :: 3 :: Only',
        'License :: OSI Approved :: MIT License',
        'Topic :: Utilities'
    ]
)
