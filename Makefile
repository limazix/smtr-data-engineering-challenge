SHELL:=/bin/bash
PYTHON_RUNNER=poetry run

PYTHON_TOOLS=tools
PYTHON_TESTS=tests
PYTHON_SCRIPTS=$(PYTHON_TOOLS) $(PYTHON_TESTS)

DOCS_PATH=./docs
REPO_URL="https://github.com/limazix/smtr-data-engineering-challenge"

commit:
	@git add --interactive
	@$(PYTHON_RUNNER) cz commit

install:
	@poetry install

update:
	@poetry update

clean:
	@poetry cache clean

lint:
	@$(PYTHON_RUNNER) black $(PYTHON_SCRIPTS) --check
	@$(PYTHON_RUNNER) flake8 $(PYTHON_SCRIPTS) --statistics

test:
	@$(PYTHON_RUNNER) pytest

test-watch:
	@$(PYTHON_RUNNER) pytest -f

coverage:
	@$(PYTHON_RUNNER) pytest --cov=$(PYTHON_TOOLS)

coverage-report:
	@$(PYTHON_RUNNER) pytest \
		--cov-report=html:htmlcov \
		--cov=$(PYTHON_TOOLS)

docs-gen:
	mkdir -p $(DOCS_PATH)
	@$(PYTHON_RUNNER) lazydocs \
		--output-path=$(DOCS_PATH) \
		--overview-file="overview.md" \
		--src-base-url=$(REPO_URL)/blob/main \
		$(PYTHON_TOOLS)
	cp README.md ./docs
	@$(PYTHON_RUNNER) mkdocs build

docs-publish:
	@$(PYTHON_RUNNER) mkdocs gh-deploy --force
