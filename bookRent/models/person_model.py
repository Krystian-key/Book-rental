from typing import List, Type

from sqlalchemy import Column, String, Integer

from bookRent.db_config import Base
from bookRent.schematics import person_schemas


class Person(Base):
    __tablename__ = "persons"
    id= Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    surname = Column(String, nullable=True)
    birth_year = Column(Integer, nullable=True)
    death_year = Column(Integer, nullable=True)


def model_to_schema(model: Type[Person] | Person | None):
    if model is None:
        return None

    return person_schemas.Person(
        id=model.id,
        name = model.name,
        surname = model.surname,
        birth_year=model.birth_year,
        death_year=model.death_year
    )


def models_to_schemas(models: List[Type[Person]]):
    schemas = []
    for model in models:
        schema: person_schemas.Person = model_to_schema(model)
        schemas.append(schema)
    return schemas