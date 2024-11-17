from sqladmin import ModelView

from ...models import EnergyStorage


class EnergyStorageView(ModelView, model=EnergyStorage):
    name = "Energy Storage (Накопитель)"
    name_plural = ""
    column_labels = {
        # EnergyStorage.id: ,
        EnergyStorage.model: EnergyStorage.model.comment,
        EnergyStorage.power: EnergyStorage.power.comment,
        EnergyStorage.capacitance: EnergyStorage.capacitance.comment,
        EnergyStorage.cycle_count: EnergyStorage.cycle_count.comment,
        EnergyStorage.price: EnergyStorage.price.comment
    }
    column_list = [
        EnergyStorage.id,
        EnergyStorage.model,
        EnergyStorage.power,
        EnergyStorage.capacitance,
        EnergyStorage.cycle_count,
        EnergyStorage.price
    ]
