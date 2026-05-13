import os
from dataclasses import dataclass
from functools import lru_cache
from pathlib import Path

from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parents[1]
ENV_FILE = BASE_DIR / ".env"

@dataclass
class Settings:
    db_host: str
    db_port: str
    db_name: str
    db_user: str
    db_password: str
    db_driver_sync: str
    db_driver_async: str

@lru_cache(maxsize=1)
def get_settings() -> Settings:
    '''
        Загружаем настройки из .env файла и кэшируем результат для оптимизации доступа к ним.
        Здесь в значениях по умолчанию должны быть всегда указаны значения из .env.exapmle, 
        чтобы при отсутствии .env файла приложение не падало, а использовало эти значения.
    '''

    load_dotenv(ENV_FILE, override=True)

    return Settings(
        db_host=os.environ.get("DB_HOST", "localhost"),
        db_port=os.environ.get("DB_PORT", "5432"),
        db_name=os.environ.get("DB_NAME", "postgres"),
        db_user=os.environ.get("DB_USER", "postgres"),
        db_password=os.environ.get("DB_PASSWORD", "postgres"),
        db_driver_sync=os.environ.get("DB_DRIVER_SYNC", "postgresql+psycopg"),
        db_driver_async=os.environ.get("DB_DRIVER_ASYNC", "postgresql+psycopg_async"),
    )
