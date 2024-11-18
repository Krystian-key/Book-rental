from pydantic import BaseModel, constr
from typing import Optional


class ReaderCreate(BaseModel):
    email: str
    password: str
    name: str
    surname: str
    phone: Optional[str]

    class Config:
        orm_mode = True

class UserLogin(BaseModel):
    username: str
    password: str
