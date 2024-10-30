from pydantic import BaseModel

class ReaderCreate(BaseModel):
    username: str
    password: str
