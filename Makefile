# Makefile for federicotdn/wikiquote

manual_checks:
	PYTHONPATH=$$(pwd) python3 util/manual_checks.py 

test:
	pytest tests -vvv -rs

format:
	black wikiquote tests

lint:
	black --check wikiquote tests
	flake8 wikiquote tests

package:
	mkdir -p dist
	rm -rf dist/*
	python3 setup.py sdist

upload: package
	twine upload dist/*

repl:
	python3 -i -c 'from wikiquote import *; p=lambda xs: [print(x, "\n") for x in xs]'
