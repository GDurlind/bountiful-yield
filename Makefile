PYTHON_VERSION = 3.14.6
POETRY_VERSION = 2.4.1
REPO_NAME = bountiful-yield
VENV_DIR = .venv
PLOTS_DIR=.plots

init:
	pyenv install $(PYTHON_VERSION) --skip-existing
	pyenv local $(PYTHON_VERSION)
	pyenv exec python -m venv $(VENV_DIR)

clean: 
	find . -type d -name .pytest_cache | xargs --no-run-if-empty -t rm -r
	find . -type d -name __pycache__ | xargs --no-run-if-empty -t rm -r
	find . -type d -name dist | xargs --no-run-if-empty -t rm -r
	find . -type d -regex ".*\.egg.*"  | xargs --no-run-if-empty -t rm -r

reqs: clean
	poetry export --without-hashes -f requirements.txt -o requirements.txt --without dev --without-urls

install: 
	poetry install -vv

test:
	poetry run pytest -s tests # --without-integration

lock: 
	poetry lock -vv

run: 
	uvicorn src.app.main:app --reload --port 5000 --env-file conf/dev.env

.PHONY: plot notebooks plots-clean test lint format

plot:
	@mkdir -p $(PLOTS_DIR)
	poetry run python scripts/generate_plots.py

plots-clean:
	rm -rf $(PLOTS_DIR)

.PHONY: notebook notebook-all

notebook:
	poetry run jupyter notebook

notebook-all:
	poetry run python scripts/execute_notebooks.py
test:
	poetry run pytest

lint:
	poetry run ruff check .

format:
	poetry run ruff format .