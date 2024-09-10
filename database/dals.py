from sqlalchemy import select, delete, update
from sqlalchemy.ext.asyncio import AsyncSession
from .models import User


class UserDAL:
    """Data Access Layer for operating user info"""

    def __init__(self, db_session: AsyncSession):
        self.db_session = db_session

    async def get_users(self):
        query = select(User)
        result = await self.db_session.execute(query)
        rows = result.scalars().all()
        if rows:
            return rows

    async def get_user_by_id(self, user_id: str):
        query = select(User).where(User.id == user_id)
        result = await self.db_session.execute(query)
        rows = result.fetchone()
        if rows is not None:
            return rows[0]

    async def get_users_by_ids(self, user_ids: list[str]):
        query = select(User).where(User.id.in_(user_ids))

        result = await self.db_session.execute(query)
        rows = result.scalars().all()
        if rows:
            return rows

    async def create_user(self, name: str, surname: str):
        new_user = User(name=name, surname=surname)
        self.db_session.add(new_user)
        await self.db_session.flush()
        await self.db_session.refresh(new_user)
        return new_user

    async def delete_user(self, user_id: str):
        query = delete(User).where(User.id == user_id).returning(User)
        result = await self.db_session.execute(query)
        rows = result.fetchone()
        if rows is not None:
            return rows[0]
