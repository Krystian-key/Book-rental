from typing import Type, List

from sqlalchemy import Integer, Column, ForeignKey, String
from sqlalchemy.orm import relationship

from bookRent.db_config import Base
from bookRent.schematics import annotation_schemas


class Annotation(Base):
    __tablename__ = "annotations"
    id= Column(Integer, primary_key=True, autoincrement=True)
    book_id = Column(Integer, ForeignKey("books.id"), nullable=True)
    ed_id = Column(Integer, ForeignKey("edition_infos.id"), nullable=True)
    copy_id = Column(Integer, ForeignKey("copies.id", ondelete="CASCADE"), nullable=True)
    content = Column(String, nullable=False)

    #book = relationship("Book", back_populates="annotations")
    #edition = relationship("EditionInfo", back_populates="annotations")
    #copy = relationship("Copy", back_populates="annotations")



def model_to_schema(model: Type[Annotation] | Annotation | None):
    if model is None:
        return None

    return annotation_schemas.Annotation(
        id=model.id,
        book_id=model.book_id,
        ed_id=model.ed_id,
        copy_id=model.copy_id,
        content=model.content,
    )


def models_to_schemas(models: List[Type[Annotation]]):
    schemas = []
    for model in models:
        schema: annotation_schemas.Annotation = model_to_schema(model)
        schemas.append(schema)
    return schemas