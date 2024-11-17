from sqlalchemy.orm import mapped_column, Mapped, relationship
from sqlalchemy import ForeignKey, BigInteger, Identity
from ..database import Base


class MaintenanceTime(Base):

    __tablename__ = "maintenance_time"
    __table_args__ = {
        "schema": "project",
        "comment": "количество часов для проведения соответствующего ТО",
    }

    id: Mapped[float] = mapped_column(BigInteger, Identity(always=True), primary_key=True)
    m_1: Mapped[int] = mapped_column(BigInteger, nullable=True)
    m_2: Mapped[int] = mapped_column(BigInteger, nullable=True)
    m_3: Mapped[int] = mapped_column(BigInteger, nullable=True)
    m_4: Mapped[int] = mapped_column(BigInteger, nullable=True)
    m_5: Mapped[int] = mapped_column(BigInteger, nullable=True)
    m_6: Mapped[int] = mapped_column(BigInteger, nullable=True)
    m_7: Mapped[int] = mapped_column(BigInteger, nullable=True)
    m_8: Mapped[int] = mapped_column(BigInteger, nullable=True)
    m_9: Mapped[int] = mapped_column(BigInteger, nullable=True)
    machine = relationship("Machine", back_populates="maintenance_time")
    machine_id: Mapped[int] = mapped_column(BigInteger, ForeignKey("project.machine.machine_id"))
