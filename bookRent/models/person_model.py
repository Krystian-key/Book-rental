from sqlalchemy import Column, String, Integer

from bookRent.db_config import Base


class Person(Base):
    __tablename__ = "persons"
    id= Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    surname = Column(String, nullable=True)
    birth_year = Column(Integer, nullable=True)
    death_year = Column(Integer, nullable=True)