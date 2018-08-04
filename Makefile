PROJECT ?= administration
COMPOSE_FILE = docker-compose.yml
DC=docker-compose -p ${PROJECT} -f ${COMPOSE_FILE}

.PHONY: install
install:
	pipenv install --dev --system --ignore-pipfile --deploy

.PHONY: build
build:
	${DC} build

.PHONY: migrate
migrate:
	${DC} run --rm --entrypoint "python manage.py" app migrate --noinput

.PHONY: server
server: migrate
	${DC} up -d

.PHONY: shell
shell:
	${DC} run --rm --entrypoint "python manage.py" app shell

.PHONY: stop
stop:
	${DC} down

.PHONY: clean
clean:
	${DC} down --remove-orphans --volumes

.PHONY: log
log:
	${DC} logs -f

.PHONY: bash
bash:
	${DC} run --rm app bash

.PHONY: isort
isort:
	${DC} run --rm --no-deps --entrypoint "/bin/bash -c" app "isort --diff --check-only --quiet"

.PHONY: pylint
pylint: isort
	${DC} run --rm --no-deps --entrypoint "/bin/bash -c" app "touch __init__.py; pylint /code; rm __init__.py"
