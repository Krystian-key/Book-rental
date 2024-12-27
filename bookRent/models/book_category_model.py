from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

from bookRent.db_config import Base


class BookCategory(Base):
    __tablename__ = "book_categories"
    #id= Column(Integer, primary_key=True, autoincrement=True)
    book_id = Column(Integer, ForeignKey("books.id"), primary_key=True)
    cat_id = Column(Integer, ForeignKey("categories.id"), primary_key=True)
    #category = relationship("Category")
