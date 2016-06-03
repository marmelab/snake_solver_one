.PHONY: tests

install:
	pip install numpy

test:
	python -m unittest discover

run:
	python main.py
