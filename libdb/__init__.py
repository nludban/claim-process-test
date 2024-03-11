import os

from sqlmodel import SQLModel, create_engine
from sqlmodel.ext.asyncio.session import AsyncSession #, AsyncEngine

# https://github.com/tiangolo/sqlmodel/discussions/706
from sqlalchemy.ext.asyncio import create_async_engine

from sqlalchemy.orm import sessionmaker


def database_url():
    username = os.environ.get('POSTGRES_USER')
    password = os.environ.get('POSTGRES_PASSWORD')
    server = os.environ.get('POSTGRES_SERVER')
    port = os.environ.get('POSTGRES_PORT')
    database = os.environ.get('POSTGRES_DB')
    return f'postgresql+asyncpg://{username}:{password}@{server}:{port}/{database}'

print('database_url=', database_url())


#engine = AsyncEngine(create_engine(database_url(), echo=True, future=True))
engine = create_async_engine(database_url(), echo=True, future=True)


async def get_session() -> AsyncSession:
    async_session = sessionmaker(
        engine, class_=AsyncSession, expire_on_commit=False
    )
    async with async_session() as session:
        yield session


async def init_db():
    async with engine.begin() as conn:
        # await conn.run_sync(SQLModel.metadata.drop_all)
        await conn.run_sync(SQLModel.metadata.create_all)

#--#
