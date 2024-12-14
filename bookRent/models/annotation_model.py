from typing import Optional

from sqlalchemy import Integer, Column, ForeignKey, String
from sqlalchemy.orm import relationship

from bookRent.db_config import Base


class Annotation(Base):
    __tablename__ = "annotations"
    id= Column(Integer, primary_key=True, autoincrement=True)
    book_id = Column(Optional[Integer], ForeignKey("books.id"), nullable=True)
    ed_id = Column(Optional[Integer], ForeignKey("edition_infos.id"), nullable=True)
    copy_id = Column(Optional[Integer], ForeignKey("copies.id"), nullable=True)
    content = Column(String, nullable=False)

    book = relationship(Optional["Book"], back_populates="annotations")
    edition = relationship(Optional["EditionInfo"], back_populates="annotations")
    copy = relationship(Optional["Copy"], back_populates="annotations")
