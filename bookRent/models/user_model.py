from pydantic import BaseModel, constr
from sqlalchemy import Integer, Column, String

from sqlalchemy.orm import relationship

from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()



class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    password = Column(String)






class ReaderCreate(BaseModel):
    username: constr(min_length=4, max_length=15)
    password: constr(min_length=8)

    class Config:
        orm_mode = True

class UserLogin(BaseModel):
    username: str
    password: str




