from typing import Optional, List

from pydantic import BaseModel

from bookRent.schematics.language_schemas import LanguageSearch
from bookRent.schematics.person_schemas import PersonCreate, PersonSearch
from bookRent.schematics.schematics import SearchModel


class BookCreate(BaseModel):
    original_title: str
    original_language: str
    original_series: Optional[str]
    author: PersonCreate
    categories: List[str]

    class Config:
        orm_mode = True


class BookSearch(SearchModel):
    id: Optional[int] = None
    original_title: Optional[str] = None
    original_language: Optional[LanguageSearch] = None
    original_series: Optional[str] = None
    author: Optional[PersonSearch] = None
    categories: Optional[List[str]] = None