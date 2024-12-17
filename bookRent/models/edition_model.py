from typing import Optional

from sqlalchemy import Integer, Column, ForeignKey, String, BigInteger
from sqlalchemy.orm import relationship

from bookRent.db_config import Base


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

    book = relationship("Book")
    illustrator = relationship("Person")
    translator = relationship("Person")
    ed_lang = relationship("Language")
    publisher = relationship("Publisher")
    form = relationship("Form")
    annotations = relationship("Annotation", back_populates="edition")
