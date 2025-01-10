from typing import List, Type

from sqlalchemy import Integer, Column, ForeignKey, String, BigInteger
from sqlalchemy.orm import relationship

from bookRent.db_config import Base
from bookRent.schematics import edition_schemas


class EditionInfo(Base):
    __tablename__ = "edition_infos"
    id= Column(Integer, primary_key=True, autoincrement=True)
    book_id = Column(Integer, ForeignKey("books.id"), nullable=False)
    ed_title = Column(String, nullable=True)
    ed_series = Column(String, nullable=True)
    illustrator_id = Column(Integer, ForeignKey("persons.id"), nullable=True)
    translator_id = Column(Integer, ForeignKey("persons.id"), nullable=True)
    ed_lang_id = Column(Integer, ForeignKey("languages.id"), nullable=True)
    publisher_id = Column(Integer, ForeignKey("publishers.id"), nullable=False)
    ed_num = Column(Integer, nullable=False)
    ed_year = Column(Integer, nullable=False)
    form_id = Column(Integer, ForeignKey("forms.id"), nullable=False)
    isbn = Column(BigInteger, nullable=False)
    ukd = Column(String, nullable=False)

    #book = relationship("Book")
    #illustrator = relationship("Person", foreign_keys=[illustrator_id])
    #translator = relationship("Person", foreign_keys=[translator_id])
    #ed_lang = relationship("Language")
    #publisher = relationship("Publisher")
    #form = relationship("Form")
    #annotations = relationship("Annotation", back_populates="edition")



def model_to_schema(model: Type[EditionInfo] | EditionInfo | None):
    if model is None:
        return None

    ed_title = ""
    if model.ed_title is not None:
        ed_title = model.ed_title

    ed_series = ""
    if model.ed_series is not None:
        ed_series = model.ed_series

    return edition_schemas.Edition(
        id=model.id,
        book_id=model.book_id,
        ed_title=ed_title,
        ed_series=ed_series,
        illustrator_id=model.illustrator_id,
        translator_id=model.translator_id,
        ed_lang_id=model.ed_lang_id,
        publisher_id=model.publisher_id,
        ed_num=model.ed_num,
        ed_year=model.ed_year,
        form_id=model.form_id,
        isbn=model.isbn,
        ukd=model.ukd
    )


def models_to_schemas(models: List[Type[EditionInfo]]):
    schemas = []
    for model in models:
        schema: edition_schemas.Edition = model_to_schema(model)
        schemas.append(schema)
    return schemas
