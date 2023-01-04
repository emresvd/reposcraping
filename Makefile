all: build

build:
	venv/Scripts/python setup.py sdist bdist_wheel

clear:
	venv/Scripts/python setup.py clean --all
