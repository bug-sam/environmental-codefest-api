.PHONY: clean install tests run all

clean:
	find . -type f -name '*.pyc' -delete
	find . -type f -name '*.log' -delete

install:
	virtualenv venv; \
	. venv/bin/activate; \
	pip install -r requirements.txt; \
	python manage.py initialize_database

install-windows:
	virtualenv venv; \
	. venv/Scripts/activate.bat; \
	pip install -r requirements.txt; \
	python manage.py initialize_database

run:
	. venv/bin/activate; \
	python manage.py run

run-windows:
	. venv/Scripts/activate.bat; \
	python manage.py run

all: clean install run
