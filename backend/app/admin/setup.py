from fastapi import FastAPI
from sqladmin import Admin

from .views.count_operation_view import CountOperationView
from ..database import engine
from .views.user_admin import UserAdmin
from .views.machine_view import MachineView
from .views.energy_storage_view import EnergyStorageView
from .views.engine_hours_period_view import EngineHoursPeriodVies
from .views.maintenance_time_view import MaintenanceTimeView
from .views.materials_price_view import MaterialsPriceView
from .views.price_hours_view import PriceHoursView
from .views.admin_auth import AdminAuth
from ..config import settings


def init_admin(app: FastAPI):
    # auth_back = AdminAuth(secret_key=settings.SECRET_KEY)
    # admin = Admin(app=app, engine=engine, authentication_backend=auth_back)
    admin = Admin(app=app, engine=engine)
    admin.add_view(UserAdmin)
    admin.add_view(CountOperationView)
    admin.add_view(MachineView)
    admin.add_view(EnergyStorageView)
    admin.add_view(EngineHoursPeriodVies)
    admin.add_view(MaintenanceTimeView)
    admin.add_view(MaterialsPriceView)
    admin.add_view(PriceHoursView)
