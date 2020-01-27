#! /usr/bin/make

VENV_DIR?=.venv
VENV_ACTIVATE=$(VENV_DIR)/bin/activate
WITH_VENV=. $(VENV_ACTIVATE);

.PHONY: help
help:  ## Print the help documentation
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

.PHONY: prereqs
prereqs: ## Ensure prereqs are installed
	./scripts/prereqs

$(VENV_ACTIVATE): app/requirements.txt app/requirements-dev.txt
	test -f $@ || virtualenv --python=python3.8 $(VENV_DIR)
	$(WITH_VENV) pip install -r app/requirements.txt
	$(WITH_VENV) pip install -r app/requirements-dev.txt
	touch $@

.PHONY: venv
venv: $(VENV_ACTIVATE) ## Install virtualenv and activate it

.PHONY: setup
setup: prereqs venv ensure_pre_commit ## Run all setup actions

# This target ensures that the pre-commit hook is installed and kept up to date
# if pre-commit updates.
.PHONY: ensure_pre_commit
ensure_pre_commit: .git/hooks/pre-commit ## Ensure pre-commit is installed
.git/hooks/pre-commit: /usr/local/bin/pre-commit
	pre-commit install
	pre-commit install-hooks

.PHONY: pre_commit_update_deps
pre_commit_update_deps: ## Update pre-commit dependencies
	pre-commit autoupdate

.PHONY: update_deps
update_deps: pre_commit_update_deps ## Update all dependencies

.PHONY: pre_commit_tests
pre_commit_tests: ## Run pre-commit tests
	pre-commit run --all-files

.PHONY: clean
clean: ## Clean all generated files
	find ./ -type d -name '__pycache__' -delete
	find ./ -type f -name '*.pyc' -delete
	rm -rf ./app/staticfiles/

.PHONY: teardown
teardown: ## Remove all virtualenv files
	rm -rf $(VENV_DIR)/

.PHONY: pretty
pretty: venv ## Prettify the code
	$(WITH_VENV) black .

.PHONY: lint
lint: venv ## Run linting tests
	$(WITH_VENV) flake8 .

.PHONY: migrate
migrate: venv  ## Migrate the database
	psql postgres://postgres:"${DB_PASSWORD}"@${DB_HOST}:"${DB_PORT}"/"${DB_NAME}" -c "CREATE SCHEMA IF NOT EXISTS django"
	$(WITH_VENV) python app/manage.py migrate

.PHONY: generate_models
generate_models: venv  ## Generate new app models.py file
	$(WITH_VENV) python app/manage.py inspectdb --database milmove > new_models.py
	mv new_models.py app/milmove_app/models.py
	pre-commit run --all-files black || true
	pre-commit run --all-files fix-encoding-pragma || true
	@echo "Ignore errors from pre-commit, they are expected"

.PHONY: prepare_key
prepare_key: venv
	$(WITH_VENV) python ./scripts/convert_key_to_jwk_set.py

.PHONY: runserver
runserver: venv  ## Run django server with built-in server
	$(WITH_VENV) python app/manage.py runserver 0.0.0.0:3000

.PHONY: runserver_docker
runserver_docker:  ## Run django server from Docker with built-in server
	$(WITH_VENV) ./scripts/runserver-docker

.PHONY: runserver_docker_prod
runserver_docker_prod:  ## Run django server from Docker with Nginx/Gunicorn
	$(WITH_VENV) ./scripts/runserver-docker-prod

default: help
