from typing import Optional

from pydantic import BaseModel


class EditionBase(BaseModel):
    book_id: int
    ed_title: Optional[str] = None
    ed_series: Optional[str] = None
    illustrator_id: Optional[int] = None
    translator_id: Optional[int] = None
    ed_lang_id: Optional[int] = None
    publisher_id: int
    ed_num: int
    ed_year: int
    form_id: int
    isbn: int
    ukd: str


class EditionCreate(EditionBase):
    pass


class Edition(EditionBase):
    id: int

    class Config:
        orm_mode = True