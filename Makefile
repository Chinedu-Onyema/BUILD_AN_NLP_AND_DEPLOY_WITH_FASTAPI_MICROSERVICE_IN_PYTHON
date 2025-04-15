install:
	pip install --upgrade pip && \
	pip install -r requirements.txt
	python -m textblob.download_corpora

test:
	python -m pytest -vv --cov=hello

lint:
	pylint --disable=R,C hello.py

all: install lint test