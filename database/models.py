from uuid import UUID, uuid4
from sqlalchemy.orm import (
    DeclarativeBase,
    mapped_column,
    Mapped,
)
from datetime import datetime


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "users"

    id: Mapped[UUID] = mapped_column(primary_key=True, default=uuid4)
    name: Mapped[str] = mapped_column()
    surname: Mapped[str] = mapped_column()
    is_deleted: Mapped[bool] = mapped_column(default=False)
    created_at: Mapped[datetime] = mapped_column(default=datetime.now)
