#! /usr/bin/make

VENV_DIR?=.venv
VENV_ACTIVATE=$(VENV_DIR)/bin/activate
WITH_VENV=. $(VENV_ACTIVATE);

.PHONY: help
help:  ## Print the help documentation
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

$(VENV_ACTIVATE): requirements.txt
	brew list libev || brew install libev
	which virtualenv || pip install virtualenv
	test -f $@ || virtualenv --python=python3 $(VENV_DIR)
	$(WITH_VENV) pip install -r requirements.txt
	touch $@

.PHONY: venv
venv: $(VENV_ACTIVATE)

.PHONY: setup
setup: venv ensure_pre_commit

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

.PHONY: teardown
teardown: ## Remove all virtualenv files
	rm -rf $(VENV_DIR)/

.PHONY: pretty
pretty: venv ## Prettify the code
	$(WITH_VENV) black .

.PHONY: lint
lint: venv ## Run linting tests
	$(WITH_VENV) flake8 .

.PHONY: generate_models
generate_models: venv
	$(WITH_VENV) python manage.py inspectdb > new_models.py
	mv new_models.py milmoveapp/models.py
	$(WITH_VENV) black milmoveapp/
	pre-commit run --all-files fix-encoding-pragma

.PHONY: run_server
run_server: venv
	$(WITH_VENV) python manage.py runserver

default: help
