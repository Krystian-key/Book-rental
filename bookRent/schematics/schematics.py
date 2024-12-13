from pydantic import BaseModel, EmailStr
from typing import Optional, List

class ReaderCreate(BaseModel):
    email: EmailStr
    password: str
    name: str
    surname: str
    phone: Optional[str] = None

    class Config:
        orm_mode = True

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class PersonCreate(BaseModel):
    name: str
    surname: str
    birth_year: Optional[int] = None
    death_year: Optional[int] = None

    class Config:
        orm_mode = True

class BookCreate(BaseModel):
    original_title: str
    original_language: str
    original_series: Optional[str]
    author: PersonCreate
    categories: List[str]

    class Config:
        orm_mode = True

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

class CopyCreate(EditionCreate):
    rented: bool = False

class PublisherCreate(BaseModel):
    name: str
    localization: str
    foundation_year: int

    class Config:
        orm_mode = True

class AnnotationCreate(BaseModel):
    content: str
    book_id: Optional[int] = None
    edition_id: Optional[int] = None
    copy_id: Optional[int] = None

    class Config:
        orm_mode = True

class ReservationCreate(BaseModel):
    user_id: int
    copy_id: int

    class Config:
        orm_mode = True

class RentalCreate(BaseModel):
    user_id: int
    copy_id: int

    class Config:
        orm_mode = True

"""
class PersonSearch(BaseModel):
    id: Optional[int] = None
    name: Optional[str] = None
    surname: Optional[str] = None
    birth_year: Optional[int] = None
    death_year: Optional[int] = None

class PublisherSearch(BaseModel):
    id: Optional[int] = None
    name: Optional[str] = None
    localization: Optional[str] = None
    foundation_year: Optional[int] = None

class LanguageSearch(BaseModel):
    id: Optional[int] = None
    language: Optional[str] = None

class FormSearch(BaseModel):
    id: Optional[int] = None
    form: Optional[str] = None

class BookSearch(BaseModel):
    id: Optional[int] = None
    original_title: Optional[str] = None
    original_language: Optional[LanguageSearch] = None
    original_series: Optional[str] = None
    author: Optional[PersonSearch] = None
    categories: Optional[List[str]] = None

class EditionSearch(BaseModel):
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

class CopySearch(BaseModel):
    id: Optional[int] = None
    edition: Optional[EditionSearch] = None
"""