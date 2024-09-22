from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import MetaData
from sqlalchemy.ext.asyncio import (
    async_sessionmaker,
    create_async_engine,
)
import contextlib

engine = create_async_engine(
    'postgresql+asyncpg://sesiadmin:sesi1234@localhost:5432/sesidb')


# 세션 생성기
SessionLocal = async_sessionmaker(
    autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


async def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        await db.close()
