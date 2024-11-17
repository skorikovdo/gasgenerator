from ..database import Base
from sqlalchemy.orm import mapped_column, Mapped, relationship
from sqlalchemy import Integer, String, CheckConstraint, Float, Identity, DECIMAL


class Machine(Base):

    __tablename__ = "machine"
    __table_args__ = (
        CheckConstraint("engine_speed <= 3000"),
        {
            'schema': 'project',
            'comment': 'Основные технические и стоимостные характеристики установки'
         }
    )

    machine_id: Mapped[int] = mapped_column(Integer, Identity(always=True), primary_key=True,
                                            comment="Идентификатор объекта", nullable=False)
    price_gpu: Mapped[str] = mapped_column(String, comment="Стоимость установки в валюте поставщика", nullable=False)
    currency: Mapped[str] = mapped_column(String, comment="Валюта", nullable=False)
    brand_model: Mapped[str] = mapped_column(String, comment="Бренд производителя", nullable=False)
    engine_speed: Mapped[int] = mapped_column(Integer, comment="Обороты двигателя", nullable=False)
    normal_oil_consumption: Mapped[float] = mapped_column(DECIMAL(), comment="Расход масла по норме гр/ед. выработки",
                                                          nullable=False)
    max_oil_consumption: Mapped[float] = mapped_column(Float, comment="Расход масла максимальный", nullable=False)
    electric_power_50: Mapped[float] = mapped_column(Float, comment="Электрическая мощность при 50% нагрузки",
                                                     nullable=False)
    electric_power_75: Mapped[float] = mapped_column(Float, comment="Электрическая мощность при 50% нагрузки",
                                                     nullable=False)
    electric_power_100: Mapped[float] = mapped_column(Float, comment="Электрическая мощность при 50% нагрузки",
                                                      nullable=False)
    thermal_power_50: Mapped[float] = mapped_column(Float, comment="Тепловая мощность при 50% нагрузки",
                                                    nullable=False)
    thermal_power_75: Mapped[float] = mapped_column(Float, comment="Тепловая мощность при 50% нагрузки",
                                                    nullable=False)
    thermal_power_100: Mapped[float] = mapped_column(Float, comment="Тепловая мощность при 50% нагрузки",
                                                     nullable=False)
    energy_power_on_fuel_50: Mapped[float] = mapped_column(Float, comment="Энергетическая мощность топлива",
                                                           nullable=False)
    energy_power_on_fuel_75: Mapped[float] = mapped_column(Float, comment="Энергетическая мощность топлива",
                                                           nullable=False)
    energy_power_on_fuel_100: Mapped[float] = mapped_column(Float, comment="Энергетическая мощность топлива",
                                                            nullable=False)
    electro_efficiency_50: Mapped[float] = mapped_column(Float, comment="КПД электрический при 50%", nullable=False)
    electro_efficiency_75: Mapped[float] = mapped_column(Float, comment="КПД электрический при 75%", nullable=False)
    electro_efficiency_100: Mapped[float] = mapped_column(Float, comment="КПД электрический при 100%", nullable=False)
    thermal_efficiency_50: Mapped[float] = mapped_column(Float, comment="КПД тепловой при 50%", nullable=False)
    thermal_efficiency_75: Mapped[float] = mapped_column(Float, comment="КПД тепловой при 75%", nullable=False)
    thermal_efficiency_100: Mapped[float] = mapped_column(Float, comment="КПД тепловой при 100%", nullable=False)
    fuel_consumption_50: Mapped[float] = mapped_column(Float, comment="Расход топлива при 50%", nullable=False)
    fuel_consumption_75: Mapped[float] = mapped_column(Float, comment="Расход топлива при 75%", nullable=False)
    fuel_consumption_100: Mapped[float] = mapped_column(Float, comment="Расход топлива при 100%", nullable=False)
    brand_generator: Mapped[str] = mapped_column(String, comment="Бренд генератора", nullable=False)
    model_generator: Mapped[str] = mapped_column(String, comment="Модель генератора", nullable=False)
    brand_engine: Mapped[str] = mapped_column(String, comment="Бренд двигателя", nullable=False)
    model_engine: Mapped[str] = mapped_column(String, comment="Модель двигателя", nullable=False)
    specification: Mapped[str] = mapped_column(String, comment="Адрес файла pdf", nullable=True)
    children = relationship("CountOperation", back_populates="parent", cascade="all, delete")
    engine_hours_period = relationship("EngineHoursPeriod", back_populates="machine", cascade="all, delete")
    maintenance_time = relationship("MaintenanceTime", back_populates="machine", cascade="all, delete")
    materials_price = relationship("MaterialsPrice", back_populates="machine", cascade="all, delete")
    price_hours = relationship("PriceHours", back_populates="machine", cascade="all, delete")

    def __repr__(self):
        return str(self.machine_id)
