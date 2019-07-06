# Makefile for federicotdn/wikiquote

manual_checks:
	PYTHONPATH=$$(pwd) python3 util/manual_checks.py 

test:
	python3 -m unittest -v

flake8:
	flake8 wikiquote tests

package:
	mkdir -p dist
	rm -rf dist/*
	python setup.py sdist

upload: package
	twine upload dist/*
