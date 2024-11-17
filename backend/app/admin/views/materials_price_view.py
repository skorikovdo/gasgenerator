from sqladmin import ModelView
from ...models import MaterialsPrice


class MaterialsPriceView(ModelView, model=MaterialsPrice):
    name_plural = ""

    column_list = [
        MaterialsPrice.m_1,
        MaterialsPrice.m_2,
        MaterialsPrice.m_3,
        MaterialsPrice.m_4,
        MaterialsPrice.m_5,
        MaterialsPrice.m_6,
        MaterialsPrice.m_7,
        MaterialsPrice.m_8,
        MaterialsPrice.m_9,
        MaterialsPrice.currency,
        MaterialsPrice.machine_id
    ]