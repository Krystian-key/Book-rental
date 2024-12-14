from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class RentalBase(BaseModel):
    user_id: int
    copy_id: int


class RentalCreate(RentalBase):
    pass


class Rental(RentalBase):
    id: int
    rental_date: datetime
    due_date: datetime
    return_date: Optional[datetime] = None

    class Config:
        orm_mode = True