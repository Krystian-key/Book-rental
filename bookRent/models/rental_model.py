from typing import Optional

from sqlalchemy import Column, Integer, ForeignKey, DateTime
from sqlalchemy.orm import relationship

from bookRent.db_config import Base


class Rental(Base):
    __tablename__ = "rentals"
    id= Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    copy_id = Column(Integer, ForeignKey("copies.id"), nullable=False)
    rental_date = Column(DateTime, nullable=False)
    due_date = Column(DateTime, nullable=False)
    return_date = Column(Optional[DateTime], nullable=True)

    user = relationship("User")
    copy = relationship("Copy")
