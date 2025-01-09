from sqlalchemy import Column, Integer, ForeignKey, Date
from sqlalchemy.orm import relationship

from bookRent.db_config import Base
from bookRent.models import User


class Rental(Base):
    __tablename__ = "rentals"
    id= Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey(User.id), nullable=False)
    copy_id = Column(Integer, ForeignKey("copies.id"), nullable=False)
    rental_date = Column(Date, nullable=False)
    due_date = Column(Date, nullable=False)
    return_date = Column(Date, nullable=True)

    #user = relationship("User", back_populates="rentals")
    #copy = relationship("Copy", back_populates="rentals")
