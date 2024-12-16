from fastapi import APIRouter, HTTPException

from bookRent.BooksCRUD.get.copy_get import *
from bookRent.BooksCRUD.tools import get_results
from bookRent.db_config import get_db

router = APIRouter()

# User
@router.get("/get")
def get(cond: dict, db: Session = Depends(get_db())):
    try:
        temp = []
        if cond["book_id"]:
            temp.append(get_book_by_id(cond["book_id"], db))
        if cond["or_title"]:
            temp.append(get_books_by_title(cond["or_title"], db))
        if cond["title"]:
            temp.append(get_books_by_title(cond["title"], db))
        if cond["or_series"]:
            temp.append(get_books_by_series(cond["or_series"], db))
        if cond["series"]:
            temp.append(get_books_by_series(cond["series"], db))
        if cond["author_id"]:
            temp.append(get_books_by_author_id(cond["author_id"], db))
        if cond["author_name"]:
            temp.append(get_books_by_author_name(cond["author_name"], db))
        if cond["author_surname"]:
            temp.append(get_books_by_author_surname(cond["author_surname"], db))
        if cond["author_birth"]:
            temp.append(get_books_by_author_birth_year(cond["author_birth"], db))
        if cond["author_death"]:
            temp.append(get_books_by_author_death_year(cond["author_death"], db))
        if cond["or_lang"]:
            temp.append(get_books_by_language(cond["lang"], db))
        if cond["or_lang_id"]:
            temp.append(get_books_by_language_id(cond["lang_id"], db))
        if cond["lang"]:
            temp.append(get_books_by_language(cond["lang"], db))
        if cond["lang_id"]:
            temp.append(get_books_by_language_id(cond["lang_id"], db))

        inter = False
        if cond["intersect"]:
            inter = True

        return get_results(temp, inter)

    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))