from datetime import datetime, date

from pydantic import BaseModel


class ReservationBase(BaseModel):
    user_id: int
    copy_id: int


class ReservationCreate(ReservationBase):
    pass


class Reservation(ReservationBase):
    id: int
    reserved_at: datetime
    reserved_due: date | None
    status: str

    class Config:
        from_attributes = True