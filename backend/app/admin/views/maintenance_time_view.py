from sqladmin import ModelView
from ...models import MaintenanceTime


class MaintenanceTimeView(ModelView, model=MaintenanceTime):
    name_plural = ""

    column_list = [
        MaintenanceTime.m_1,
        MaintenanceTime.m_2,
        MaintenanceTime.m_3,
        MaintenanceTime.m_4,
        MaintenanceTime.m_5,
        MaintenanceTime.m_6,
        MaintenanceTime.m_7,
        MaintenanceTime.m_8,
        MaintenanceTime.m_9,
    ]