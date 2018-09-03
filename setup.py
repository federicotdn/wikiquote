from distutils.core import setup

with open('requirements.txt') as f:
    requires = f.read().splitlines()

with open('README.md') as f:
    long_description = f.read()

setup(
    name='wikiquote',
    packages=['wikiquote', 'wikiquote.langs'],
    version='0.1.9',
    description='Retrieve quotes from any Wikiquote article.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Federico Tedin',
    author_email='federicotedin@gmail.com',
    install_requires=requires,
    url='https://github.com/federicotdn/python-wikiquotes',
    download_url='https://github.com/federicotdn/python-wikiquotes/archive/0.1.9.tar.gz',
    keywords=['quotes', 'wikiquote', 'python', 'api', 'qotd', 'quote', 'day'],
    license='MIT',
    classifiers=[
        'Programming Language :: Python :: 3 :: Only',
        'License :: OSI Approved :: MIT License',
        'Topic :: Utilities'
    ]
)
