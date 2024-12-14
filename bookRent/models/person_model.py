from typing import Optional

from sqlalchemy import Column, String, Integer

from bookRent.db_config import Base


class Person(Base):
    __tablename__ = "persons"
    id= Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    surname = Column(String, nullable=False)
    birth_year = Column(Optional[Integer], nullable=True)
    death_year = Column(Optional[Integer], nullable=True)