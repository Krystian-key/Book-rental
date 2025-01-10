from datetime import date
from typing import Optional

from pydantic import BaseModel


class RentalBase(BaseModel):
    user_id: int
    copy_id: int


class RentalCreate(RentalBase):
    pass


class Rental(RentalBase):
    id: int
    rental_date: date
    due_date: date
    return_date: Optional[date] = None

    class Config:
        from_attributes = True