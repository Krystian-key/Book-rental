from typing import Type, List

from sqlalchemy import Integer, Column, String

from bookRent.db_config import Base
from bookRent.schematics import category_schemas


class Category(Base):
    __tablename__ = "categories"
    id= Column(Integer, primary_key=True, autoincrement=True)
    category = Column(String, nullable=False, unique=True)



def model_to_schema(model: Type[Category] | Category | None):
    if model is None:
        return None

    return category_schemas.Category(
        id = model.id,
        category = model.category,
    )


def models_to_schemas(models: List[Type[Category]]):
    schemas = []
    for model in models:
        schema: category_schemas.Category = model_to_schema(model)
        schemas.append(schema)
    return schemas