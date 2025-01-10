from typing import List, Type

from sqlalchemy import Column, Integer, String

from bookRent.db_config import Base
from bookRent.schematics import language_schemas


class Language(Base):
    __tablename__ = "languages"
    id= Column(Integer, primary_key=True, autoincrement=True)
    lang = Column(String, nullable=False, unique=True)



def model_to_schema(model: Type[Language] | Language | None):
    if model is None:
        return None

    return language_schemas.Language(
        id=model.id,
        lang=model.lang
    )


def models_to_schemas(models: List[Type[Language]]):
    schemas = []
    for model in models:
        schema: language_schemas.Language = model_to_schema(model)
        schemas.append(schema)
    return schemas