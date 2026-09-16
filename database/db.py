from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker

from core.config import settings

engine = create_async_engine(settings.database_url, echo=True)

Session = async_sessionmaker(bind=engine)

async def get_db():
    async with Session() as session:
         yield session



