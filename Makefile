# Makefile for federicotdn/wikiquote

manual_checks:
	PYTHONPATH=$$(pwd) python3 util/manual_checks.py

clean:
	rm -rf wikiquote.egg-info dist

test:
	uv run pytest tests -vvv -rs

install-types:
	uv run mypy wikiquote --install-types --non-interactive

types:
	uv run mypy wikiquote

lint:
	uv run ruff check --fix --output-format=full --show-fixes wikiquote tests
	uv run ruff format wikiquote tests

package:
	make clean
	uv build

upload: package
	twine upload dist/*

repl:
	uv run python -i -c 'from wikiquote import *; p=lambda xs: [print(x, "\n") for x in xs]'
