.PHONY: all test

PYTHON ?= python

all: ;

test: all
	py.test

dev: all
	pip install -e .
