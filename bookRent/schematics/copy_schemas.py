from pydantic import BaseModel


class CopyBase(BaseModel):
    ed_id: int


class CopyCreate(CopyBase):
    pass


class Copy(CopyBase):
    id: int
    rented: bool = False

    class Config:
        orm_mode = True