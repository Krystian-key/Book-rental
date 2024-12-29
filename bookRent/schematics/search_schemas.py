from datetime import date, datetime
from typing import Optional, List

from pydantic import BaseModel


class SearchModel(BaseModel):
    intersect: bool = False


class AnnotationSearch(SearchModel):
    ann_id: Optional[int] = None
    copy_id: Optional[int] = None
    ed_id: Optional[int] = None
    book_id: Optional[int] = None


class CategorySearch(SearchModel):
    cat_id: Optional[int] = None
    cat: Optional[str] = None


class BookCategorySearch(SearchModel):
    book_id: Optional[int] = None
    cat_id: Optional[int] = None


class BookSearch(SearchModel):
    book_id: Optional[int] = None
    title: Optional[str] = None
    or_title: Optional[str] = None
    lang_id: Optional[int] = None
    lang: Optional[str] = None
    or_lang_id: Optional[int] = None
    or_lang: Optional[str] = None
    series: Optional[str] = None
    or_series: Optional[str] = None
    author_id: Optional[int] = None
    author_name: Optional[str] = None
    author_surname: Optional[str] = None
    author_birth: Optional[int] = None
    author_death: Optional[int] = None
    categories: Optional[List[str]] = None


class EditionSearch(BookSearch):
    ed_id: Optional[int] = None
    ed_title: Optional[str] = None
    ed_series: Optional[str] = None
    ill_id: Optional[int] = None
    ill_name: Optional[str] = None
    ill_surname: Optional[str] = None
    ill_birth: Optional[int] = None
    ill_death: Optional[int] = None
    tran_id: Optional[int] = None
    tran_name: Optional[str] = None
    tran_surname: Optional[str] = None
    tran_birth: Optional[int] = None
    tran_death: Optional[int] = None
    ed_lang_id: Optional[int] = None
    ed_lang: Optional[str] = None
    publ_id: Optional[int] = None
    publ_name: Optional[str] = None
    publ_city: Optional[str] = None
    publ_year: Optional[int] = None
    ed_num: Optional[int] = None
    ed_year: Optional[int] = None
    form_id: Optional[int] = None
    form: Optional[str] = None
    isbn: Optional[int] = None
    ukd: Optional[str] = None


class CopySearch(EditionSearch):
    copy_id: Optional[int] = None
    rented: Optional[bool] = None


class FormSearch(SearchModel):
    form_id: Optional[int] = None
    form: Optional[str] = None


class LanguageSearch(SearchModel):
    lang_id: Optional[int] = None
    lang: Optional[str] = None


class PersonSearch(SearchModel):
    id: Optional[int] = None
    name: Optional[str] = None
    surname: Optional[str] = None
    birth_year: Optional[int] = None
    death_year: Optional[int] = None


class PublisherSearch(SearchModel):
    publ_id: Optional[int] = None
    publ_name: Optional[str] = None
    publ_city: Optional[str] = None
    publ_year: Optional[int] = None


class RentalSearch(SearchModel):
    rent_id: Optional[int] = None
    user_id: Optional[int] = None
    card_num: Optional[int] = None
    copy_id: Optional[int] = None
    rent_date: Optional[date] = None
    rent_due: Optional[date] = None
    return_date: Optional[date] = None


class ReservationSearch(SearchModel):
    res_id: Optional[int] = None
    user_id: Optional[int] = None
    card_num: Optional[int] = None
    copy_id: Optional[int] = None
    res_date: Optional[datetime] = None
    res_due: Optional[datetime] = None
    res_status: Optional[str] = None