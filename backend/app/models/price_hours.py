from sqlalchemy.orm import mapped_column, Mapped, relationship
from sqlalchemy import Float, ForeignKey, BigInteger, Identity
from ..database import Base


class PriceHours(Base):

    __tablename__ = "price_hours"
    __table_args__ = {
        "schema": "project",
        "comment": "стоимость часа работ по каждому ТО",
    }

    id: Mapped[int] = mapped_column(BigInteger, Identity(always=True), primary_key=True)
    m_1: Mapped[float] = mapped_column(Float, nullable=True)
    m_2: Mapped[float] = mapped_column(Float, nullable=True)
    m_3: Mapped[float] = mapped_column(Float, nullable=True)
    m_4: Mapped[float] = mapped_column(Float, nullable=True)
    m_5: Mapped[float] = mapped_column(Float, nullable=True)
    m_6: Mapped[float] = mapped_column(Float, nullable=True)
    m_7: Mapped[float] = mapped_column(Float, nullable=True)
    m_8: Mapped[float] = mapped_column(Float, nullable=True)
    m_9: Mapped[float] = mapped_column(Float, nullable=True)
    machine = relationship("Machine", back_populates="price_hours")
    machine_id: Mapped[int] = mapped_column(BigInteger, ForeignKey("project.machine.machine_id"))
