from sqlalchemy import Column, Integer, String
from ..database import Base


class UserDB(Base):
    __tablename__ = "users"
    __table_args__ = {"schema": "users"}

    id = Column(Integer, unique=True, autoincrement=True, primary_key=True)
    name = Column(String)
    hashed_password = Column(String)
