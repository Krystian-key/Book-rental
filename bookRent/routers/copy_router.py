from fastapi import APIRouter

from bookRent.BooksCRUD.add.copy_add import create_copy
from bookRent.BooksCRUD.get.copy_get import *
from bookRent.BooksCRUD.tools import try_perform
from bookRent.db_config import get_db
from bookRent.dependiencies import role_required
from bookRent.schematics.copy_schemas import CopyCreate, Copy

router = APIRouter()

# Worker
@router.post("/add")
def add(copy: CopyCreate, role: str = Depends(role_required(['Worker', 'Admin'])), db: Session = Depends(get_db)):#, role: str = Depends(role_required(['Worker']))):
    return try_perform(create_copy, copy, db=db)


# === GET ===
# === ANY ===


@router.get("/get-all", response_model=list[Copy] | None)
def get_all(db: Session = Depends(get_db)):
    return try_perform(get_all_copies, db=db)

@router.get("/get-by-id", response_model=Copy | None)
def get_by_id(copy_id: int, db: Session = Depends(get_db)):
    print(copy_id)
    copy = try_perform(get_copy_by_id, copy_id, db=db)
    print(copy)
    return copy


@router.get("/get-by-rented", response_model=Copy | list[Copy] | None)
def get_by_rented(rented: bool, db: Session = Depends(get_db)):
    return try_perform(get_copies_by_rented, rented, db=db)


@router.get("/get-by-edition-id", response_model=Copy | list[Copy] | None)
def get_by_edition_id(edition_id: int, db: Session = Depends(get_db)):
    return try_perform(get_copies_by_edition_id, edition_id, db=db)


@router.get("/get-by-book-id", response_model=Copy | list[Copy] | None)
def get_by_book_id(book_id: int, db: Session = Depends(get_db)):
    return try_perform(get_copies_by_book_id, book_id, db=db)


@router.get("/get-by-edition-number", response_model=Copy | list[Copy] | None)
def get_by_edition_num(num: int, db: Session = Depends(get_db)):
    return try_perform(get_copies_by_edition_number, num, db=db)


@router.get("/get-by-edition-year", response_model=Copy | list[Copy] | None)
def get_by_edition_year(year: int, db: Session = Depends(get_db)):
    return try_perform(get_copies_by_edition_year, year, db=db)


@router.get("/get-by-isbn", response_model=Copy | list[Copy] | None)
def get_by_isbn(isbn: int, db: Session = Depends(get_db)):
    return try_perform(get_copies_by_isbn, isbn, db=db)


@router.get("/get-by-ukd", response_model=Copy | list[Copy] | None)
def get_by_ukd(ukd: str, db: Session = Depends(get_db)):
    return try_perform(get_copies_by_ukd, ukd, db=db)


# === TITLE ===

@router.get("/get-by-original-title", response_model=Copy | list[Copy] | None)
def get_by_original_title(title: str, db: Session = Depends(get_db)):
    return try_perform(get_copies_by_original_title, title, db=db)


@router.get("/get-by-edition-title", response_model=Copy | list[Copy] | None)
def get_by_edition_title(title: str, db: Session = Depends(get_db)):
    return try_perform(get_copies_by_edition_title, title, db=db)


@router.get("/get-by-title", response_model=Copy | list[Copy] | None)
def get_by_title(title: str, db: Session = Depends(get_db)):
    return try_perform(get_copies_by_title, title, db=db)


# === SERIES ===

@router.get("/get-by-original-series", response_model=Copy | list[Copy] | None)
def get_by_original_series(series: str, db: Session = Depends(get_db)):
    return try_perform(get_copies_by_original_series, series, db=db)


@router.get("/get-by-edition-series", response_model=Copy | list[Copy] | None)
def get_by_edition_series(series: str, db: Session = Depends(get_db)):
    return try_perform(get_copies_by_edition_series, series, db=db)


@router.get("/get-by-series", response_model=Copy | list[Copy] | None)
def get_by_series(series: str, db: Session = Depends(get_db)):
    return try_perform(get_copies_by_series, series, db=db)


# === AUTHOR ===

@router.get("/get-by-author-id", response_model=Copy | list[Copy] | None)
def get_by_author_id(author_id: int, db: Session = Depends(get_db)):
    return try_perform(get_copies_by_author_id, author_id, db=db)


@router.get("/get-by-author-name", response_model=Copy | list[Copy] | None)
def get_by_author_name(name: str, db: Session = Depends(get_db)):
    return try_perform(get_copies_by_author_name, name, db=db)


@router.get("/get-by-author-surname", response_model=Copy | list[Copy] | None)
def get_by_author_surname(surname: str, db: Session = Depends(get_db)):
    return try_perform(get_copies_by_author_surname, surname, db=db)


@router.get("/get-by-author-birth-year", response_model=Copy | list[Copy] | None)
def get_by_author_birth_year(birth: int, db: Session = Depends(get_db)):
    return try_perform(get_copies_by_author_birth_year, birth, db=db)


@router.get("/get-by-author-death-year", response_model=Copy | list[Copy] | None)
def get_by_author_death_year(death: int, db: Session = Depends(get_db)):
    return try_perform(get_copies_by_author_death_year, death, db=db)


# === ILLUSTRATOR ===

@router.get("/get-by-illustrator-id", response_model=Copy | list[Copy] | None)
def get_by_illustrator_id(illustrator_id: int, db: Session = Depends(get_db)):
    return try_perform(get_copies_by_illustrator_id, illustrator_id, db=db)


@router.get("/get-by-illustrator-name", response_model=Copy | list[Copy] | None)
def get_by_author_name(name: str, db: Session = Depends(get_db)):
    return try_perform(get_copies_by_illustrator_name, name, db=db)


@router.get("/get-by-illustrator-surname", response_model=Copy | list[Copy] | None)
def get_by_illustrator_surname(surname: str, db: Session = Depends(get_db)):
    return try_perform(get_copies_by_illustrator_surname, surname, db=db)


@router.get("/get-by-illustrator-birth-year", response_model=Copy | list[Copy] | None)
def get_by_illustrator_birth_year(birth: int, db: Session = Depends(get_db)):
    return try_perform(get_copies_by_illustrator_birth_year, birth, db=db)


@router.get("/get-by-illustrator-death-year", response_model=Copy | list[Copy] | None)
def get_by_illustrator_death_year(death: int, db: Session = Depends(get_db)):
    return try_perform(get_copies_by_illustrator_death_year, death, db=db)


# === TRANSLATOR ===

@router.get("/get-by-translator-id", response_model=Copy | list[Copy] | None)
def get_by_translator_id(translator_id: int, db: Session = Depends(get_db)):
    return try_perform(get_copies_by_translator_id, translator_id, db=db)


@router.get("/get-by-translator-name", response_model=Copy | list[Copy] | None)
def get_by_translator_name(name: str, db: Session = Depends(get_db)):
    return try_perform(get_copies_by_translator_name, name, db=db)


@router.get("/get-by-translator-surname", response_model=Copy | list[Copy] | None)
def get_by_translator_surname(surname: str, db: Session = Depends(get_db)):
    return try_perform(get_copies_by_translator_surname, surname, db=db)


@router.get("/get-by-translator-birth-year", response_model=Copy | list[Copy] | None)
def get_by_translator_birth_year(birth: int, db: Session = Depends(get_db)):
    return try_perform(get_copies_by_translator_birth_year, birth, db=db)


@router.get("/get-by-translator-death-year", response_model=Copy | list[Copy] | None)
def get_by_translator_death_year(death: int, db: Session = Depends(get_db)):
    return try_perform(get_copies_by_translator_death_year, death, db=db)


# === LANGUAGE ===

@router.get("/get-by-original-language-id", response_model=Copy | list[Copy] | None)
def get_by_original_language_id(lang_id: int, db: Session = Depends(get_db)):
    return try_perform(get_copies_by_original_language_id, lang_id, db=db)


@router.get("/get-by-original-language-name", response_model=Copy | list[Copy] | None)
def get_by_original_language_name(lang: str, db: Session = Depends(get_db)):
    return try_perform(get_copies_by_original_language, lang, db=db)


@router.get("/get-by-edition-language-id", response_model=Copy | list[Copy] | None)
def get_by_edition_language_id(lang_id: int, db: Session = Depends(get_db)):
    return try_perform(get_copies_by_edition_language_id, lang_id, db=db)


@router.get("/get-by-edition-language-name", response_model=Copy | list[Copy] | None)
def get_by_edition_language_name(lang: str, db: Session = Depends(get_db)):
    return try_perform(get_copies_by_edition_language, lang, db=db)


@router.get("/get-by-language-id", response_model=Copy | list[Copy] | None)
def get_by_language_id(lang_id: int, db: Session = Depends(get_db)):
    return try_perform(get_copies_by_language_id, lang_id, db=db)


@router.get("/get-by-language-name", response_model=Copy | list[Copy] | None)
def get_by_language_name(lang: str, db: Session = Depends(get_db)):
    return try_perform(get_copies_by_language, lang, db=db)


# === PUBLISHER ===

@router.get("/get-by-publisher-id", response_model=Copy | list[Copy] | None)
def get_by_publisher_id(publisher_id: int, db: Session = Depends(get_db)):
    return try_perform(get_copies_by_publisher_id, publisher_id, db=db)


@router.get("/get-by-publisher-name", response_model=Copy | list[Copy] | None)
def get_by_publisher_name(publisher_name: str, db: Session = Depends(get_db)):
    return try_perform(get_copies_by_publisher_name, publisher_name, db=db)


@router.get("/get-by-publisher-city", response_model=Copy | list[Copy] | None)
def get_by_publisher_city(city: str, db: Session = Depends(get_db)):
    return try_perform(get_copies_by_publisher_city, city, db=db)


@router.get("/get-by-publisher-foundation-year", response_model=Copy | list[Copy] | None)
def get_by_publisher_foundation_year(year: int, db: Session = Depends(get_db)):
    return try_perform(get_copies_by_publisher_foundation_year, year, db=db)


# === FORM ===

@router.get("get-by-form-id", response_model=Copy | list[Copy] | None)
def get_by_form_id(form_id: int, db: Session = Depends(get_db)):
    return try_perform(get_copies_by_form_id, form_id, db=db)


@router.get("/get-by-form-name", response_model=Copy | list[Copy] | None)
def get_by_form_name(form: str, db: Session = Depends(get_db)):
    return try_perform(get_copies_by_form, form, db=db)