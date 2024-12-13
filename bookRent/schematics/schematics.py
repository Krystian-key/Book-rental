from datetime import date, datetime

from pydantic import BaseModel, constr, EmailStr
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