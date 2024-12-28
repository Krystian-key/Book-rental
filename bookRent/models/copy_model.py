from sqlalchemy import Column, Integer, ForeignKey, Boolean
from sqlalchemy.orm import relationship

from bookRent.db_config import Base


class Copy(Base):
    __tablename__ = "copies"
    id= Column(Integer, primary_key=True, autoincrement=True)
    ed_id = Column(Integer, ForeignKey("edition_infos.id"), nullable=False)
    rented = Column(Boolean, nullable=False)

    #edition = relationship("EditionInfo")
    #annotations = relationship("Annotation", back_populates="copy")
    #rentals = relationship("Rental", back_populates="copy")