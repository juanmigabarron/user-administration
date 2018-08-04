PROJECT ?= administration
COMPOSE_FILE = docker-compose.yml
DC=docker-compose -p ${PROJECT} -f ${COMPOSE_FILE}

.PHONY: install
install: ##@development Installs requirements. You can use pipenv shell to activate virtualenv.
	pipenv install --dev --system --ignore-pipfile --deploy

.PHONY: build
build: ##@development Builds docker image. Needed only after changes in requierements.
	${DC} build

.PHONY: _db
_db: ##@development Starts database service and wait until this service is available.
	${DC} up -d db
	sleep 2

.PHONY: migrate
migrate: ##@development Applies migration on your database.
	${DC} run --rm --entrypoint "python manage.py" app migrate --noinput

.PHONY: server
server: ##@development Runs the Administration app in http://localhost:8000/ .
server: _db migrate
	${DC} up -d

.PHONY: shell
shell: ##@development Starts a django shell in a isolate container.
	${DC} run --rm --entrypoint "python manage.py" app shell

.PHONY: stop
stop: ##@development Stops all the docker services.
	${DC} down

.PHONY: clean
clean: ##@development Removes all the docker services and volumes.
	${DC} down --remove-orphans --volumes

.PHONY: log
log: ##@development Shows all the services log entries.
	${DC} logs -f

.PHONY: bash
bash: ##@development Starts a shell in a isolate container.
	${DC} run --rm app bash

.PHONY: isort
isort: ##@linting Runs isort to check imports ordering.
	${DC} run --rm --no-deps --entrypoint "/bin/bash -c" app "isort --diff --check-only --quiet"

.PHONY: pylint
pylint: ##@linting Runs pylint to analyse all the application code.
pylint: isort
	${DC} run --rm --no-deps --entrypoint "/bin/bash -c" app "touch __init__.py; pylint /code; rm __init__.py"

.PHONY: test
test: ##@test Runs all the tests of the application.
test: _db
	${DC} run --rm --entrypoint "/bin/bash -c" app "pytest"

# Add the following 'help' target to your Makefile
# And add help text after each target name starting with '\#\#'
# A category can be added with @category
HELP_FUN = \
    %help; \
    while(<>) { push @{$$help{$$2 // 'options'}}, [$$1, $$3] if /^([a-zA-Z\-]+)\s*:.*\#\#(?:@([a-zA-Z\-]+))?\s(.*)$$/ }; \
    print "usage: make [target]\n\n"; \
    for (sort keys %help) { \
    print "\@$$_:\n"; \
    for (@{$$help{$$_}}) { \
    $$sep = " " x (32 - length $$_->[0]); \
    print "  $$_->[0]$$sep$$_->[1]\n"; \
    }; \
    print "\n"; }

.PHONY: help
help: ##@other Show this help.
	@perl -e '$(HELP_FUN)' $(MAKEFILE_LIST)
