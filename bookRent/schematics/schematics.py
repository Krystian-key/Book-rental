from pydantic import BaseModel, EmailStr
from typing import Optional, List

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

class SearchModel(BaseModel):
    intersect: bool = False