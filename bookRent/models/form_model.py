from typing import List, Type

from sqlalchemy import Column, Integer, String

from bookRent.db_config import Base
from bookRent.schematics import form_schemas


class Form(Base):
    __tablename__ = "forms"
    id= Column(Integer, primary_key=True, autoincrement=True)
    form = Column(String, nullable=False, unique=True)



def model_to_schema(model: Type[Form] | Form | None):
    if model is None:
        return None

    return form_schemas.Form(
        id=model.id,
        form=model.form
    )


def models_to_schemas(models: List[Type[Form]]):
    schemas = []
    for model in models:
        schema: form_schemas.Form = model_to_schema(model)
        schemas.append(schema)
    return schemas