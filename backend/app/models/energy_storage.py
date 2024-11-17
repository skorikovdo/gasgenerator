from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import Float, String, BigInteger, Identity
from ..database import Base


class EnergyStorage(Base):
    __tablename__ = 'energy_storage'
    __table_args__ = (
        {
            'schema': 'project',
            'comment': 'Дополнительное оборудование для снятия пиков'
         }
    )

    id: Mapped[int] = mapped_column(BigInteger, Identity(always=True), primary_key=True)
    model: Mapped[str] = mapped_column(String, nullable=False, comment='Модель накопителя')
    power: Mapped[float] = mapped_column(Float, nullable=False, comment='Мощность')
    capacitance: Mapped[int] = mapped_column(BigInteger, nullable=False, comment='Ёмкость')
    cycle_count: Mapped[int] = mapped_column(BigInteger, nullable=False, comment='Количество циклов')
    price: Mapped[float] = mapped_column(Float, nullable=False, comment='Стоимость накопителя')
