from typing import Optional

from pydantic import BaseModel


class BookBase(BaseModel):
    title: str
    series: Optional[str] = None
    lang_id: int
    author_id: int


class BookCreate(BookBase):
    pass
        
        
class Book(BookBase):
    id: int

    class Config:
        orm_mode = True