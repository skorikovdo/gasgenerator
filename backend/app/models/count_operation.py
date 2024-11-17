from sqlalchemy.orm import mapped_column, Mapped, relationship
from sqlalchemy import BigInteger, ForeignKey, Identity
from ..database import Base


class CountOperation(Base):

    __tablename__ = "count_operation"
    __table_args__ = {
        "schema": "project",
    }

    id: Mapped[int] = mapped_column(BigInteger, Identity(always=True), primary_key=True)
    m_1: Mapped[int] = mapped_column(BigInteger, nullable=True)
    m_2: Mapped[int] = mapped_column(BigInteger, nullable=True)
    m_3: Mapped[int] = mapped_column(BigInteger, nullable=True)
    m_4: Mapped[int] = mapped_column(BigInteger, nullable=True)
    m_5: Mapped[int] = mapped_column(BigInteger, nullable=True)
    m_6: Mapped[int] = mapped_column(BigInteger, nullable=True)
    m_7: Mapped[int] = mapped_column(BigInteger, nullable=True)
    m_8: Mapped[int] = mapped_column(BigInteger, nullable=True)
    m_9: Mapped[int] = mapped_column(BigInteger, nullable=True)
    machine_id: Mapped[int] = mapped_column(BigInteger, ForeignKey("project.machine.machine_id"))
    parent = relationship("Machine", back_populates="children")
