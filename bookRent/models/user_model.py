from pydantic import BaseModel, constr
from sqlalchemy import Integer, Column, String, Enum
from enum import Enum as PyEnum
from sqlalchemy.orm import relationship

from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class UserRole(PyEnum):
    czytelnik = "czytelnik"
    pracownik = "pracownik"
    admin = "admin"


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    password = Column(String)
    role = Column(Enum(UserRole), nullable=False)






class ReaderCreate(BaseModel):
    username: constr(min_length=4, max_length=15)
    password: constr(min_length=8)

    class Config:
        orm_mode = True

class UserLogin(BaseModel):
    username: str
    password: str




