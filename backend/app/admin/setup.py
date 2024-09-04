from fastapi import FastAPI
from sqladmin import Admin
from ..database import engine
from .views.user_admin import UserAdmin


def init_admin(app: FastAPI):
    admin = Admin(app=app, engine=engine)
    admin.add_view(UserAdmin)
