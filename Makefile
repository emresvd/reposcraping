all: build

build:
	venv/Scripts/python setup.py sdist bdist_wheel