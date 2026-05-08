.PHONY: install test lint format typecheck check up down

install:
	uv sync --extra dev

test:
	uv run pytest

lint:
	uv run ruff check .

format:
	uv run ruff format .

typecheck:
	uv run mypy src tests

check:
	uv run ruff format --check .
	uv run ruff check .
	uv run mypy src tests
	uv run pytest

up:
	docker compose -f docker/compose.yaml up --build

down:
	docker compose -f docker/compose.yaml down
