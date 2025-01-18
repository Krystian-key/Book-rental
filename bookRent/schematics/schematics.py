from pydantic import BaseModel, EmailStr, ConfigDict
from typing import Optional

class ReaderCreate(BaseModel):
    email: EmailStr
    password: str
    name: str
    surname: str
    phone: Optional[str] = None
    model_config = ConfigDict(from_attributes=True)

class UserLogin(BaseModel):
    email: EmailStr
    password: str