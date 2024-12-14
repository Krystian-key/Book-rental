from typing import Optional

from pydantic import BaseModel

from bookRent.schematics.schematics import SearchModel


class PublisherCreate(BaseModel):
    name: str
    localization: str
    foundation_year: int

    class Config:
        orm_mode = True


class PublisherSearch(SearchModel):
    id: Optional[int] = None
    name: Optional[str] = None
    localization: Optional[str] = None
    foundation_year: Optional[int] = None