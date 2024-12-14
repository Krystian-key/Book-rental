from datetime import datetime

from pydantic import BaseModel


class ReservationBase(BaseModel):
    user_id: int
    copy_id: int


class ReservationCreate(ReservationBase):
    pass


class Reservation(ReservationBase):
    id: int
    reserved_at: datetime
    reserved_due: datetime
    status: str

    class Config:
        orm_mode = True