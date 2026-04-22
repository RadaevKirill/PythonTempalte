.PHONY: install test lint format typecheck check docker-up docker-down

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

docker-up:
	docker compose -f docker/compose.yaml up --build

docker-down:
	docker compose -f docker/compose.yaml down
