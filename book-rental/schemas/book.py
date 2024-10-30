from typing import Optional

from pydantic import BaseModel
from person import Person
from publisher import Publisher


class Book(BaseModel):
    title: str
    series: Optional[str] = None
    author: Person
    language: str
    year: int
    categories: list[str]
    annotations: list[str]


class BookEdition(Book):
    ed_title: str
    ed_series: Optional[str] = None
    ed_language: str
    ed_number: int
    ed_year: int
    publisher: Publisher
    illustrator: Optional[Person] = None
    translator: Optional[Person] = None
    form: str
    isbn: int
    ukd: str


class BookCopy(BookEdition):
    id: int
    rented: bool