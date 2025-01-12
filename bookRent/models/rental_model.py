from typing import List, Type

from sqlalchemy import Column, Integer, ForeignKey, Date
from sqlalchemy.orm import relationship

from bookRent.db_config import Base
from bookRent.models import User
from bookRent.schematics import rental_schemas


class Rental(Base):
    __tablename__ = "rentals"
    id= Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey(User.id), nullable=False)
    copy_id = Column(Integer, ForeignKey("copies.id", ondelete="SET NULL"), nullable=True)
    rental_date = Column(Date, nullable=False)
    due_date = Column(Date, nullable=False)
    return_date = Column(Date, nullable=True)

    #user = relationship("User", back_populates="rentals")
    #copy = relationship("Copy", back_populates="rentals")



def model_to_schema(model: Type[Rental] | Rental | None):
    if model is None:
        return None

    return rental_schemas.Rental(
        id=model.id,
        user_id=model.user_id,
        copy_id=model.copy_id,
        rental_date=model.rental_date,
        due_date=model.due_date,
        return_date=model.return_date
    )


def models_to_schemas(models: List[Type[Rental]]):
    schemas = []
    for model in models:
        schema: rental_schemas.Rental = model_to_schema(model)
        schemas.append(schema)
    return schemas