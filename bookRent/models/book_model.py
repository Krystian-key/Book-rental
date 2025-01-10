from typing import List, Type

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from bookRent.db_config import Base
from bookRent.schematics import book_schemas


class Book(Base):
    __tablename__ = "books"
    id= Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, nullable=False)
    lang_id = Column(Integer, ForeignKey("languages.id"), nullable=False)
    series = Column(String, nullable=True)
    author_id = Column(Integer, ForeignKey("persons.id"), nullable=False)

    #lang = relationship("Language", backref="books")
    #author = relationship("Person", backref="books")
    #categories = relationship("BookCategory")
    #annotations = relationship("Annotation", back_populates="book")



def model_to_schema(model: Type[Book] | Book | None):
    if model is None:
        return None

    series = ""
    if model.series is not None:
        series = model.series
    return book_schemas.Book(
        id=model.id,
        title=model.title,
        series=series,
        lang_id=model.lang_id,
        author_id=model.author_id
    )


def models_to_schemas(models: List[Type[Book]]):
    schemas = []
    for model in models:
        schema: book_schemas.Book = model_to_schema(model)
        schemas.append(schema)
    return schemas