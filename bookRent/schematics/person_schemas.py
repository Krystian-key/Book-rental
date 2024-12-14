from typing import Optional

from pydantic import BaseModel

from bookRent.schematics.schematics import SearchModel


class PersonCreate(BaseModel):
    name: str
    surname: str
    birth_year: Optional[int] = None
    death_year: Optional[int] = None

    class Config:
        orm_mode = True


class PersonSearch(SearchModel):
    id: Optional[int] = None
    name: Optional[str] = None
    surname: Optional[str] = None
    birth_year: Optional[int] = None
    death_year: Optional[int] = None