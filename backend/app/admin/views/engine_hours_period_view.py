from sqladmin import ModelView
from ...models import EngineHoursPeriod


class EngineHoursPeriodVies(ModelView, model=EngineHoursPeriod):
    name = "Engine Hours Period"
    name_plural = ""
    column_list = [
        EngineHoursPeriod.m_1,
        EngineHoursPeriod.m_2,
        EngineHoursPeriod.m_3,
        EngineHoursPeriod.m_4,
        EngineHoursPeriod.m_5,
        EngineHoursPeriod.m_6,
        EngineHoursPeriod.m_7,
        EngineHoursPeriod.m_8,
        EngineHoursPeriod.m_9,
        EngineHoursPeriod.machine_id
    ]
