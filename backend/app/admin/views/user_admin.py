from typing import Any
from fastapi import Request
from sqladmin import ModelView
from ...models.user import UserDB
from ...services.auth import create_pwd_hash


class UserAdmin(ModelView, model=UserDB):
    name = "Пользователи"
    name_plural = ""
    column_labels = {
        UserDB.username: "Логин для входа",
        UserDB.name: "Имя пользователя",
        UserDB.surname: "Фамилия пользователя",
        UserDB.company: "Название компании",
        UserDB.hashed_password: "Пароль",
    }
    column_list = [
        UserDB.username,
        UserDB.name,
        UserDB.surname,
        UserDB.company,
    ]

    async def on_model_change(
        self, data: dict, model: Any, is_created: bool, request: Request
    ) -> None:
        if is_created:
            data["hashed_password"] = create_pwd_hash(data["hashed_password"])
