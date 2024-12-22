from typing import Optional

from pydantic import BaseModel


class BookBase(BaseModel):
    title: str
    series: str
    lang_id: int
    author_id: int


class BookCreate(BookBase):
    pass
        
        
class Book(BookBase):
    id: int

    class Config:
        from_attributes = True