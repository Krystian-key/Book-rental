from typing import Optional

from pydantic import BaseModel, ConfigDict


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
    model_config = ConfigDict(from_attributes=True)


class EditionUpdate(BaseModel):
    id: int
    book_id: Optional[int] = None
    ed_title: Optional[str] = None
    ed_series: Optional[str] = None
    illustrator_id: Optional[int] = None
    translator_id: Optional[int] = None
    ed_lang_id: Optional[int] = None
    publisher_id: Optional[int] = None
    ed_num: Optional[int] = None
    ed_year: Optional[int] = None
    form_id: Optional[int] = None
    isbn: Optional[int] = None
    ukd: Optional[str] = None