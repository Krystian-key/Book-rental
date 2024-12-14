from pydantic import BaseModel

class ReservationCreate(BaseModel):
    user_id: int
    copy_id: int

    class Config:
        orm_mode = True