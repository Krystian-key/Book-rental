from sqlalchemy import Integer, Column, String

from bookRent.db_config import Base


class Category(Base):
    __tablename__ = "categories"
    id= Column(Integer, primary_key=True, autoincrement=True)
    category = Column(String, nullable=False, unique=True)
