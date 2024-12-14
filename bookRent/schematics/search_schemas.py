from typing import Optional, List

from pydantic import BaseModel


class SearchModel(BaseModel):
    intersect: bool = False


class PublisherSearch(SearchModel):
    id: Optional[int] = None
    name: Optional[str] = None
    localization: Optional[str] = None
    foundation_year: Optional[int] = None


class PersonSearch(SearchModel):
    id: Optional[int] = None
    name: Optional[str] = None
    surname: Optional[str] = None
    birth_year: Optional[int] = None
    death_year: Optional[int] = None


class LanguageSearch(SearchModel):
    id: Optional[int] = None
    language: Optional[str] = None


class FormSearch(SearchModel):
    id: Optional[int] = None
    form: Optional[str] = None


class BookSearch(SearchModel):
    id: Optional[int] = None
    original_title: Optional[str] = None
    original_language: Optional[LanguageSearch] = None
    original_series: Optional[str] = None
    author: Optional[PersonSearch] = None
    categories: Optional[List[str]] = None


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


class CopySearch(SearchModel):
    id: Optional[int] = None
    edition: Optional[EditionSearch] = None
    rented: Optional[bool] = None