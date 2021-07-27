from setuptools import setup

VERSION = "0.1.16"


with open("requirements.txt") as f:
    requires = f.read().splitlines()

with open("README.md") as f:
    long_description = f.read()

setup(
    name="wikiquote",
    packages=["wikiquote", "wikiquote.langs"],
    version=VERSION,
    description="Retrieve quotes from any Wikiquote article.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Federico Tedin",
    author_email="federicotedin@gmail.com",
    install_requires=requires,
    python_requires=">=3.6, <4",
    url="https://github.com/federicotdn/wikiquote",
    download_url="https://github.com/federicotdn/wikiquote/archive/{}.tar.gz".format(
        VERSION
    ),
    keywords=["quotes", "wikiquote", "python", "api", "qotd", "quote", "day"],
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3 :: Only",
        "License :: OSI Approved :: MIT License",
        "Topic :: Utilities",
    ],
)
