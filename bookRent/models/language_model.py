from sqlalchemy import Column, Integer, String

from bookRent.db_config import Base


class Language(Base):
    __tablename__ = "languages"
    id= Column(Integer, primary_key=True, autoincrement=True)
    lang = Column(String, nullable=False, unique=True)
