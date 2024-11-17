from sqladmin import ModelView

from ...models import CountOperation


class CountOperationView(ModelView, model=CountOperation):
    name_plural = ""
    column_list = [
        CountOperation.id,
        CountOperation.m_1,
        CountOperation.m_2,
        CountOperation.m_3,
        CountOperation.m_4,
        CountOperation.m_5,
        CountOperation.m_6,
        CountOperation.m_7,
        CountOperation.m_8,
        CountOperation.m_9,
        CountOperation.machine_id,
    ]
