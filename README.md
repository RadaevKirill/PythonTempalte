# Python Template

## Быстрый старт

```bash
python3.13 -m venv venv
source venv/bin/activate
make install
make test
make check
make up
```

Локально `make check` запускает полный набор проверок: форматирование, линтер, типизацию и тесты.
В `GitLab CI` для merge request сейчас запускаются `make lint` и `make test`.
Docker-конфигурация находится в `docker/`.

## Что изменить

- Обновить `name`, `description` и `authors` в `pyproject.toml`
- Добавить зависимости в `dependencies` и `dev`
- Обновить `docker/Dockerfile` и `docker/compose.yaml` под ваш способ запуска
- Расширить `.gitlab-ci.yml` новыми этапами и проверками
- Расширить тесты в `tests/test_main.py` или добавить новые

## Структура

- `src/main.py` - точка входа приложения
- `tests/test_main.py` - базовый пример теста
- `pyproject.toml` - зависимости и настройки инструментов
- `Makefile` - команды `install`, `test`, `lint`, `format`, `typecheck`, `check`, `up`, `down`
- `docker/Dockerfile` - образ приложения
- `docker/compose.yaml` - локальный запуск через Docker Compose
- `.gitlab-ci.yml` - пайплайн GitLab CI для merge request
- `README.md` - описание шаблона
