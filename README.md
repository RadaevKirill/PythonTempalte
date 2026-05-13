# Python Template

## Быстрый старт

Для работы с проектом использовать `uv`.

```bash
cp .env.example .env
uv sync --extra dev
make up
make test
make check
```

Если Docker не нужен, достаточно:

```bash
cp .env.example .env
uv sync --extra dev
uv run app
```

Локально `make check` запускает полный набор проверок: форматирование, линтер, типизацию и тесты. Docker-конфигурация находится в `docker/`.

## База данных

В шаблоне уже подключены:

- `SQLAlchemy`
- `psycopg` для синхронной работы с PostgreSQL
- async engine через драйвер `postgresql+psycopg_async`

Настройки подключения читаются из `.env` через [`src/config.py`](src/config.py), а engine и фабрики сессий находятся в [`src/infrastructure/db/engine.py`](src/infrastructure/db/engine.py).

В шаблоне намеренно нет автоматических `commit` / `rollback` внутри session helpers. Это будет зависеть от прикладного сценария и должно определяться на уровне сервисов или use case-слоя, когда они появятся.

Для синхронного кода используйте:

```python
with get_sync_session() as session:
    ...
```

Для асинхронного:

```python
async with get_async_session() as session:
    ...
```

## Что изменить

- Обновить `name`, `description` и `authors` в `pyproject.toml`
- Добавить прикладные зависимости в `dependencies` и `dev`
- Обновить `docker/Dockerfile` и `docker/compose.yaml` под ваш способ запуска
- Расширить `.gitlab-ci.yml` новыми этапами и проверками
- Расширить тесты в `tests/test_main.py` или добавить новые
- Добавить модели в `src/models/`
- Добавить сервисы и определить транзакционные границы для работы с БД

## Структура

- `src/main.py` - точка входа приложения
- `src/config.py` - загрузка настроек из `.env`
- `src/infrastructure/db/engine.py` - sync/async engine и session factories
- `src/models/` - модели SQLAlchemy
- `tests/test_main.py` - базовый пример теста
- `pyproject.toml` - зависимости и настройки инструментов
- `Makefile` - команды `install`, `test`, `lint`, `format`, `typecheck`, `check`, `up`, `down`
- `docker/Dockerfile` - образ приложения
- `docker/compose.yaml` - локальный запуск через Docker Compose
- `.gitlab-ci.yml` - пайплайн GitLab CI для merge request
- `README.md` - описание шаблона
- `.env.example` - пример переменных окружения

## Примечания

- Для установки кастомных пакетов из нашего Registry, следует задать переменные окружения
```bash
export UV_INDEX_GITLAB_USERNAME="read-package"
export UV_INDEX_GITLAB_PASSWORD="GAT"
```
- Dev-зависимости ставятся через `uv sync --extra dev`, поэтому они должны храниться в `[project.optional-dependencies].dev` внутри `pyproject.toml`.
- Для запуска без `Makefile` можно использовать `uv run app`.
