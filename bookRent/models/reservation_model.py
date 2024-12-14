from enum import Enum as PyEnum

from sqlalchemy import Integer, Column, ForeignKey, DateTime, Enum
from sqlalchemy.orm import relationship

from bookRent.db_config import Base


class ReservationStatus(PyEnum):
    Reserved = "Reserved"
    Awaiting = "Awaiting"
    Cancelled = "Cancelled"
    PastDue = "PastDue"
    Succeeded = "Succeeded"


class Reservation(Base):
    __tablename__ = "reservations"
    id= Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    copy_id = Column(Integer, ForeignKey("copies.id"), nullable=False)
    reserved_at = Column(DateTime, nullable=False)
    reserved_due = Column(DateTime, nullable=False)
    status = Column(Enum(ReservationStatus), nullable=False)

    user = relationship("User")
    copy = relationship("Copy")