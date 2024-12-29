from pydantic import BaseModel, EmailStr
from typing import Optional

class ReaderCreate(BaseModel):
    email: EmailStr
    password: str
    name: str
    surname: str
    phone: Optional[str] = None

    class Config:
        orm_mode = True

class UserLogin(BaseModel):
    email: EmailStr
    password: str