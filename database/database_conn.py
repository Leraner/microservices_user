from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from ..settings import DATABASE_URL
from ..singleton import SingletonMeta


class SingletonDatabaseConnection(metaclass=SingletonMeta):
    async_engine = create_async_engine(DATABASE_URL, echo=False)
    async_session = async_sessionmaker(
        async_engine, expire_on_commit=False, class_=AsyncSession
    )

    @classmethod
    def create_session(cls, func):
        async def inner(*args, **kwargs):
            async with cls.async_session() as db_session:
                async with db_session.begin():
                    return await func(*args, **kwargs, db_session=db_session)

        return inner
