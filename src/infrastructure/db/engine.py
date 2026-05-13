from collections.abc import AsyncIterator, Iterator
from contextlib import asynccontextmanager, contextmanager
from functools import lru_cache

from sqlalchemy.engine import URL, Engine, create_engine
from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import Session, sessionmaker

from src.config import get_settings


@lru_cache(maxsize=1)
def get_sync_engine() -> Engine:
    settings = get_settings()

    url = URL.create(
        drivername=settings.db_driver_sync,
        username=settings.db_user,
        password=settings.db_password,
        host=settings.db_host,
        port=int(settings.db_port),
        database=settings.db_name,
    )

    return create_engine(url)


@lru_cache(maxsize=1)
def get_async_engine() -> AsyncEngine:
    settings = get_settings()

    url = URL.create(
        drivername=settings.db_driver_async,
        username=settings.db_user,
        password=settings.db_password,
        host=settings.db_host,
        port=int(settings.db_port),
        database=settings.db_name,
    )

    return create_async_engine(url)


@lru_cache(maxsize=1)
def sync_session_factory() -> sessionmaker[Session]:
    return sessionmaker(bind=get_sync_engine(), autoflush=False, expire_on_commit=False)


@lru_cache(maxsize=1)
def async_session_factory() -> async_sessionmaker[AsyncSession]:
    return async_sessionmaker(bind=get_async_engine(), autoflush=False, expire_on_commit=False)


@contextmanager
def get_sync_session() -> Iterator[Session]:
    factory = sync_session_factory()
    with factory() as session:
        yield session


@asynccontextmanager
async def get_async_session() -> AsyncIterator[AsyncSession]:
    factory = async_session_factory()
    async with factory() as session:
        yield session
