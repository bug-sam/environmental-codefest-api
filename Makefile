.PHONY: clean install tests run all

clean:
	find . -type f -name '*.pyc' -delete
	find . -type f -name '*.log' -delete

install:
	virtualenv venv; \
	. venv/bin/activate; \
	pip install -r requirements.txt; \
	python manage.py db init; \
	python manage.py db migrate --message 'initial database migration'; \
	python manage.py db upgrade


run:
	. venv/bin/activate; \
	python manage.py run

all: clean install run