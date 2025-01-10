from typing import List, Type

from sqlalchemy import Integer, Column, String

from bookRent.db_config import Base
from bookRent.schematics import publisher_schemas


class Publisher(Base):
    __tablename__ = "publishers"
    id= Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    localization = Column(String, nullable=False)
    foundation_year = Column(Integer, nullable=False)



def model_to_schema(model: Type[Publisher] | Publisher | None):
    if model is None:
        return None

    return publisher_schemas.Publisher(
        id=model.id,
        name = model.name,
        localization=model.localization,
        foundation_year=model.foundation_year
    )


def models_to_schemas(models: List[Type[Publisher]]):
    schemas = []
    for model in models:
        schema: publisher_schemas.Publisher = model_to_schema(model)
        schemas.append(schema)
    return schemas