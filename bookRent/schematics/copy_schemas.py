from pydantic import BaseModel, ConfigDict


class CopyBase(BaseModel):
    ed_id: int


class CopyCreate(CopyBase):
    pass


class Copy(CopyBase):
    id: int
    rented: bool = False
    model_config = ConfigDict(from_attributes=True)