from typing import Type, List

from sqlalchemy import Column, Integer, ForeignKey, Boolean
from sqlalchemy.orm import relationship

from bookRent.db_config import Base
from bookRent.schematics import copy_schemas


class Copy(Base):
    __tablename__ = "copies"
    id= Column(Integer, primary_key=True, autoincrement=True)
    ed_id = Column(Integer, ForeignKey("edition_infos.id"), nullable=False)
    rented = Column(Boolean, nullable=False)

    #edition = relationship("EditionInfo")
    #annotations = relationship("Annotation", back_populates="copy")
    #rentals = relationship("Rental", back_populates="copy")



def model_to_schema(model: Type[Copy] | Copy | None):
    if model is None:
        return None

    return copy_schemas.Copy(
        id=model.id,
        ed_id=model.ed_id,
        rented=model.rented
    )


def models_to_schemas(models: List[Type[Copy]]):
    schemas = []
    for model in models:
        schema: copy_schemas.Copy = model_to_schema(model)
        schemas.append(schema)
    return schemas