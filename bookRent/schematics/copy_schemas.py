from pydantic import BaseModel


class CopyBase(BaseModel):
    ed_id: int
    rented: bool


class CopyCreate(CopyBase):
    pass


class Copy(CopyBase):
    id: int

    class Config:
        orm_mode = True