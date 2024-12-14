from pydantic import BaseModel

class RentalCreate(BaseModel):
    user_id: int
    copy_id: int

    class Config:
        orm_mode = True