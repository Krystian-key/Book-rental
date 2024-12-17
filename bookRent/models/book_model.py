from typing import Optional

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from bookRent.db_config import Base


class Book(Base):
    __tablename__ = "books"
    id= Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, nullable=False)
    lang_id = Column(Integer, ForeignKey("languages.id"), nullable=False)
    series = Column(String, nullable=True)
    author_id = Column(Integer, ForeignKey("persons.id"), nullable=False)

    lang = relationship("Language", backref="books")
    author = relationship("Person", backref="books")
    categories = relationship("BookCategory")
    annotations = relationship("Annotation", back_populates="book")
