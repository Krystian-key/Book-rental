from typing import Type, List

from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

from bookRent.db_config import Base
from bookRent.schematics import book_category_schemas


class BookCategory(Base):
    __tablename__ = "book_categories"
    #id= Column(Integer, primary_key=True, autoincrement=True)
    book_id = Column(Integer, ForeignKey("books.id"), primary_key=True)
    cat_id = Column(Integer, ForeignKey("categories.id"), primary_key=True)
    #category = relationship("Category")



def model_to_schema(model: Type[BookCategory] | BookCategory | None):
    if model is None:
        return None

    return book_category_schemas.BookCategory(
        book_id=model.book_id,
        category_id=model.cat_id
    )


def models_to_schemas(models: List[Type[BookCategory]]):
    schemas = []
    for model in models:
        schema: book_category_schemas.BookCategory = model_to_schema(model)
        schemas.append(schema)
    return schemas