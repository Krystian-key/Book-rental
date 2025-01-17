from typing import Optional

from pydantic import BaseModel, ConfigDict


class BookBase(BaseModel):
    title: str
    series: Optional[str] = None
    lang_id: int
    author_id: int


class BookCreate(BookBase):
    pass
        
        
class Book(BookBase):
    id: int
    model_config = ConfigDict(from_attributes=True)


class BookUpdate(BaseModel):
    id: int
    title: Optional[str] = None
    series: Optional[str] = None
    lang_id: Optional[int] = None
    author_id: Optional[int] = None