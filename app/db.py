from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from contextlib import asynccontextmanager
from sqlmodel import SQLModel

from app.core.settings import get_settings

settings = get_settings()

engine = create_async_engine(settings.get_db_url(), echo=True)

async_session_maker = sessionmaker(
    engine,
    class_=AsyncSession,
    expire_on_commit=False
)

async def get_session() -> AsyncSession:
    async with async_session_maker() as session:
        yield session


async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)

