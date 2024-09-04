from enum import Enum

from pydantic import BaseModel, ConfigDict


class Role(Enum):
    USER = "user"
    ADMIN = "admin"


class BaseUser(BaseModel):
    username: str


class LoginUser(BaseUser):
    password: str


class User(BaseUser):
    id: int
    model_config = ConfigDict(from_attributes=True)
