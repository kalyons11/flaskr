default: install test

install:
	pip install -r requirements.txt
	pip install . --upgrade

deploy:
	pip install pipreqs
	pipreqs . --force

test:
	docker ps
	docker build . -f Dockerfile.test -t flaskr-test
	docker run -p 5000:5000 --rm -it flaskr-test

start:
	docker build . -t flaskr
	docker run -p 5000:5000 --rm -it flaskr