.PHONY: clean install tests run all

clean:
	find . -type f -name '*.pyc' -delete
	find . -type f -name '*.log' -delete

install:
	virtualenv venv; \
	. venv/bin/activate; \
	pip install -r requirements.txt; \
	python manage.py initialize_database

remake-test-db:
	rm ./api/environmental_codefest.db; \
	python manage.py initialize_database; \
	sqlite3 ./api/environmental_codefest.db < ./scripts/test_db.sql

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
