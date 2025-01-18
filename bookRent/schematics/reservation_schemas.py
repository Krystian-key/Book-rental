from datetime import datetime, date

from pydantic import BaseModel, ConfigDict


class ReservationBase(BaseModel):
    user_id: int
    copy_id: int | None = None


class ReservationCreate(ReservationBase):
    pass


class Reservation(ReservationBase):
    id: int
    reserved_at: datetime
    reserved_due: date | None
    status: str
    model_config = ConfigDict(from_attributes=True)