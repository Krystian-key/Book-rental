from sqlalchemy import Integer, Column, String, Enum, DateTime, ForeignKey
from enum import Enum as PyEnum
from sqlalchemy.orm import relationship
from datetime import datetime
from sqlalchemy.orm import declarative_base


Base = declarative_base()

class UserRole(PyEnum):
    User = "User"
    Worker = "Worker"
    Admin = "Admin"

class UserInfo(Base):
    __tablename__ = "user_infos"

    id= Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    surname = Column(String, nullable=False)
    phone = Column(String(20), nullable=True)
    card_num = Column(String, nullable=False)

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    user_infos_id = Column(Integer, ForeignKey("user_infos.id"), nullable=False)
    role = Column(Enum(UserRole), nullable=False)
    created_at = Column(DateTime, default=datetime.now(), nullable=False)

    user_info = relationship("UserInfo", backref="users")
