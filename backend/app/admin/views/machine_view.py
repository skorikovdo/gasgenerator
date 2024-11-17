from sqladmin import ModelView
from ...models import Machine


class MachineView(ModelView, model=Machine):
    name = "Machine (Машины)"
    name_plural = ""
    form_excluded_columns = [
        Machine.children,
        Machine.engine_hours_period,
        Machine.maintenance_time,
        Machine.price_hours,
        Machine.materials_price
    ]
    column_list = [
        Machine.machine_id,
        Machine.price_gpu,
        Machine.currency,
        Machine.brand_model,
        Machine.engine_speed,
        Machine.normal_oil_consumption,
        Machine.max_oil_consumption,
        Machine.electric_power_50,
        Machine.electric_power_75,
        Machine.electric_power_100,
        Machine.thermal_power_50,
        Machine.thermal_power_75,
        Machine.thermal_power_100,
        Machine.energy_power_on_fuel_50,
        Machine.energy_power_on_fuel_75,
        Machine.energy_power_on_fuel_100,
        Machine.electro_efficiency_50,
        Machine.electro_efficiency_75,
        Machine.electro_efficiency_100,
        Machine.thermal_efficiency_50,
        Machine.thermal_efficiency_75,
        Machine.thermal_efficiency_100,
        Machine.fuel_consumption_50,
        Machine.fuel_consumption_75,
        Machine.fuel_consumption_100,
        Machine.brand_generator,
        Machine.model_generator,
        Machine.brand_engine,
        Machine.model_engine,
        Machine.specification
    ]
    column_sortable_list = [Machine.machine_id]
