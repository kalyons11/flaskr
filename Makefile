default: install test

install:
	pip install -r requirements.txt
	pip install --editable .

deploy:
	pip install pipreqs
	pipreqs . --force

test:
	python -m nose -v --nocapture --with-doctest flaskr

start:
	flask initdb
	flask run