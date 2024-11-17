from sqladmin import ModelView
from ...models import PriceHours


class PriceHoursView(ModelView, model=PriceHours):
    name_plural = ""
    column_list = [
        PriceHours.m_1,
        PriceHours.m_2,
        PriceHours.m_3,
        PriceHours.m_4,
        PriceHours.m_5,
        PriceHours.m_6,
        PriceHours.m_7,
        PriceHours.m_8,
        PriceHours.m_9,
        PriceHours.machine_id,
    ]