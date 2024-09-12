.PHONY: init
init:
	pip install --upgrade pip
	pip install -r requirements.txt
	pip install -r requirements-dev.txt

.PHONY: lint
lint:
	ruff --version
	ruff check
	mypy .

.PHONY: fmt
fmt:
	ruff --version
	ruff format
	ruff check --fix
