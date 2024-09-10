from user_microservice.database.database_conn import SingletonDatabaseConnection
from user_microservice.database.dals import UserDAL
from sqlalchemy.ext.asyncio import AsyncSession


class Handler(SingletonDatabaseConnection):
    @SingletonDatabaseConnection.create_session
    async def get_users(self, db_session: AsyncSession):
        user_dal = UserDAL(db_session=db_session)
        return await user_dal.get_users()

    @SingletonDatabaseConnection.create_session
    async def get_user_by_id(self, user_id, db_session: AsyncSession):
        user_dal = UserDAL(db_session=db_session)
        return await user_dal.get_user_by_id(user_id)

    @SingletonDatabaseConnection.create_session
    async def get_users_by_ids(self, user_ids: list[str], db_session: AsyncSession):
        user_dal = UserDAL(db_session=db_session)
        return await user_dal.get_users_by_ids(user_ids=user_ids)

    @SingletonDatabaseConnection.create_session
    async def create_user(self, name: str, surname: str, db_session: AsyncSession):
        user_dal = UserDAL(db_session=db_session)
        return await user_dal.create_user(name=name, surname=surname)

    @SingletonDatabaseConnection.create_session
    async def delete_user(self, user_id: str, db_session: AsyncSession):
        user_dal = UserDAL(db_session=db_session)
        return await user_dal.delete_user(user_id=user_id)
