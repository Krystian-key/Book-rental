from fastapi import APIRouter, HTTPException

from bookRent.BooksCRUD.add.edition_add import create_edition
from bookRent.BooksCRUD.get.copy_get import *
from bookRent.BooksCRUD.tools import get_results
from bookRent.db_config import get_db
from bookRent.schematics.edition_schemas import EditionCreate

router = APIRouter()

# Worker
@router.post("/add")
def add(edition: EditionCreate, db: Session = Depends(get_db)):
    try:
        return create_edition(edition, db)

    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


# User
@router.get("/get")
def get(cond: dict, db: Session = Depends(get_db)):
    try:
        temp = []
        if cond["ed_id"]:
            temp.append(get_edition_by_id(cond["ed_id"], db))
        if cond["book_id"]:
            temp.append(get_editions_by_book_id(cond["book_id"], db))
        if cond["ed_title"]:
            temp.append(get_editions_by_edition_title(cond["ed_title"], db))
        if cond["or_title"]:
            temp.append(get_editions_by_original_title(cond["or_title"], db))
        if cond["title"]:
            temp.append(get_editions_by_title(cond["title"], db))
        if cond["ed_series"]:
            temp.append(get_editions_by_edition_series(cond["ed_series"], db))
        if cond["or_series"]:
            temp.append(get_editions_by_original_series(cond["or_series"], db))
        if cond["series"]:
            temp.append(get_editions_by_series(cond["series"], db))
        if cond["author_id"]:
            temp.append(get_editions_by_author_id(cond["author_id"], db))
        if cond["author_name"]:
            temp.append(get_editions_by_author_name(cond["author_name"], db))
        if cond["author_surname"]:
            temp.append(get_editions_by_author_surname(cond["author_surname"], db))
        if cond["author_birth"]:
            temp.append(get_editions_by_author_birth_year(cond["author_birth"], db))
        if cond["author_death"]:
            temp.append(get_editions_by_author_death_year(cond["author_death"], db))
        if cond["ill_id"]:
            temp.append(get_editions_by_illustrator_id(cond["ill_id"], db))
        if cond["ill_name"]:
            temp.append(get_editions_by_illustrator_name(cond["ill_name"], db))
        if cond["ill_surname"]:
            temp.append(get_editions_by_illustrator_surname(cond["ill_surname"], db))
        if cond["ill_birth"]:
            temp.append(get_editions_by_illustrator_birth_year(cond["ill_birth"], db))
        if cond["ill_death"]:
            temp.append(get_editions_by_illustrator_death_year(cond["ill_death"], db))
        if cond["tran_id"]:
            temp.append(get_editions_by_translator_id(cond["tran_id"], db))
        if cond["tran_name"]:
            temp.append(get_editions_by_translator_name(cond["tran_name"], db))
        if cond["tran_surname"]:
            temp.append(get_editions_by_translator_surname(cond["tran_surname"], db))
        if cond["tran_birth"]:
            temp.append(get_editions_by_translator_birth_year(cond["tran_birth"], db))
        if cond["tran_death"]:
            temp.append(get_editions_by_translator_death_year(cond["tran_death"], db))
        if cond["ed_lang"]:
            temp.append(get_editions_by_edition_language(cond["ed_lang"], db))
        if cond["ed_lang_id"]:
            temp.append(get_editions_by_edition_language_id(cond["ed_lang_id"], db))
        if cond["or_lang"]:
            temp.append(get_editions_by_original_language(cond["or_lang"], db))
        if cond["or_lang_id"]:
            temp.append(get_editions_by_original_language_id(cond["or_lang_id"], db))
        if cond["lang"]:
            temp.append(get_editions_by_language(cond["lang"], db))
        if cond["lang_id"]:
            temp.append(get_editions_by_language_id(cond["lang_id"], db))
        if cond["publ_id"]:
            temp.append(get_editions_by_publisher_id(cond["publ_id"], db))
        if cond["publ_name"]:
            temp.append(get_editions_by_publisher_name(cond["publ_name"], db))
        if cond["publ_city"]:
            temp.append(get_editions_by_publisher_city(cond["publ_city"], db))
        if cond["publ_year"]:
            temp.append(get_editions_by_publisher_foundation_year(cond["publ_year"], db))
        if cond["ed_num"]:
            temp.append(get_editions_by_edition_number(cond["ed_num"], db))
        if cond["ed_year"]:
            temp.append(get_editions_by_edition_year(cond["ed_year"], db))
        if cond["form"]:
            temp.append(get_editions_by_form(cond["form"], db))
        if cond["form_id"]:
            temp.append(get_editions_by_form_id(cond["form_id"], db))
        if cond["isbn"]:
            temp.append(get_edition_by_isbn(cond["isbn"], db))
        if cond["ukd"]:
            temp.append(get_edition_by_ukd(cond["ukd"], db))

        inter = False
        if cond["intersect"]:
            inter = True

        return get_results(temp, inter)

    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))