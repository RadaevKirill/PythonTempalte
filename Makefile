.PHONY: install test lint format typecheck check up down

install:
	pip install -e ".[dev]"

test:
	pytest

lint:
	ruff check .

format:
	ruff format .

typecheck:
	mypy src tests

check:
	ruff format --check .
	ruff check .
	mypy src tests
	pytest

up:
	docker compose -f docker/compose.yaml up --build

down:
	docker compose -f docker/compose.yaml down
