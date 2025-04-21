# Makefile for federicotdn/wikiquote

manual_checks:
	PYTHONPATH=$$(pwd) python3 util/manual_checks.py

clean:
	rm -rf wikiquote.egg-info dist

test:
	pytest tests -vvv -rs

install-types:
	mypy wikiquote --install-types --non-interactive

types:
	mypy wikiquote

lint:
	ruff check --fix --output-format=full --show-fixes wikiquote tests
	ruff format wikiquote tests

package:
	make clean
	uv build

upload: package
	twine upload dist/*

repl:
	python3 -i -c 'from wikiquote import *; p=lambda xs: [print(x, "\n") for x in xs]'
