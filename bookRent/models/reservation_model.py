from enum import Enum as PyEnum
from typing import List, Type

from sqlalchemy import Integer, Column, ForeignKey, DateTime, Enum, Date
from sqlalchemy.orm import relationship

from bookRent.db_config import Base
from bookRent.models.models import User
from bookRent.schematics import reservation_schemas


class ReservationStatus(PyEnum):
    Reserved = "Reserved"
    Awaiting = "Awaiting"
    Cancelled = "Cancelled"
    PastDue = "PastDue"
    Succeeded = "Succeeded"


class Reservation(Base):
    __tablename__ = "reservations"
    id= Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey(User.id), nullable=False)
    copy_id = Column(Integer, ForeignKey("copies.id", ondelete="SET NULL"), nullable=True)
    reserved_at = Column(DateTime, nullable=False)
    reserved_due = Column(Date, nullable=True)
    status = Column(Enum(ReservationStatus), nullable=False)



def model_to_schema(model: Type[Reservation] | Reservation | None):
    if model is None:
        return None

    return reservation_schemas.Reservation(
        id=model.id,
        user_id=model.user_id,
        copy_id=model.copy_id,
        reserved_at=model.reserved_at,
        reserved_due=model.reserved_due,
        status=model.status
    )


def models_to_schemas(models: List[Type[Reservation]]):
    schemas = []
    for model in models:
        schema: reservation_schemas.Reservation = model_to_schema(model)
        schemas.append(schema)
    return schemas