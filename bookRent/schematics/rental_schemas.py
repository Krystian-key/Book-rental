from datetime import date
from typing import Optional

from pydantic import BaseModel, ConfigDict


class RentalBase(BaseModel):
    user_id: int
    copy_id: int | None = None


class RentalCreate(RentalBase):
    pass


class Rental(RentalBase):
    id: int
    rental_date: date
    due_date: date
    return_date: Optional[date] = None
    model_config = ConfigDict(from_attributes=True)