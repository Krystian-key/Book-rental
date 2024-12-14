from typing import Optional

from bookRent.schematics.book_schemas import BookCreate, BookSearch
from bookRent.schematics.form_schemas import FormSearch
from bookRent.schematics.language_schemas import LanguageSearch
from bookRent.schematics.person_schemas import PersonCreate, PersonSearch
from bookRent.schematics.publisher_schemas import PublisherSearch
from bookRent.schematics.schematics import SearchModel


class EditionCreate(BookCreate):
    edition_title: Optional[str]
    edition_language: Optional[str]
    edition_series: Optional[str]
    illustrator: Optional[PersonCreate]
    translator: Optional[PersonCreate]
    publisher_name: str
    edition_number: int
    edition_year: int
    form: str
    isbn: int
    ukd: str


class EditionSearch(SearchModel):
    id: Optional[int] = None
    book: Optional[BookSearch] = None
    edition_title: Optional[str] = None
    edition_series: Optional[str] = None
    illustrator: Optional[PersonSearch] = None
    translator: Optional[PersonSearch] = None
    edition_language: Optional[LanguageSearch] = None
    publisher: Optional[PublisherSearch] = None
    edition_number: Optional[int] = None
    edition_year: Optional[int] = None
    form: Optional[FormSearch] = None
    isbn: Optional[int] = None
    ukd: Optional[str] = None