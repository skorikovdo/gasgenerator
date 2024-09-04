from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from ..database import Base


class UserDB(Base):
    __tablename__ = "users"
    __table_args__ = {"schema": "users"}
    """
        Посмотреть на mapping_column
        id - идентификатор(автоинкремент)
        username - логин(уникальное)
        name - имя пользователя(not null)
        surname - фамилия пользователя(not null)
        company - название компании(not null)
        role - роль(дефол user)
    """
    id: Mapped[int] = mapped_column(
        Integer, autoincrement=True, primary_key=True, comment="Идентификатор объекта"
    )
    username: Mapped[str] = mapped_column(
        String, unique=True, nullable=False, comment="Логин для входа"
    )
    name: Mapped[str] = mapped_column(String, comment="Имя пользователя", nullable=True)
    surname: Mapped[str] = mapped_column(String, comment="Фамилия пользователя", nullable=True)
    company: Mapped[str] = mapped_column(String, comment="Название компании", nullable=True)
    hashed_password: Mapped[str] = mapped_column(String, nullable=False)
