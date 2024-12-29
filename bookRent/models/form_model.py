from sqlalchemy import Column, Integer, String

from bookRent.db_config import Base


class Form(Base):
    __tablename__ = "forms"
    id= Column(Integer, primary_key=True, autoincrement=True)
    form = Column(String, nullable=False, unique=True)
