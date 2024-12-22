from fastapi import APIRouter

from bookRent.BooksCRUD.add.book_add import create_book
from bookRent.BooksCRUD.get.copy_get import *
from bookRent.BooksCRUD.tools import try_perform
from bookRent.db_config import get_db
from bookRent.schematics.book_schemas import BookCreate, Book

router = APIRouter()

# Worker
@router.post("/add")
def add(book: BookCreate, db: Session = Depends(get_db)):
    try:
        return create_book(book, db)

    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


"""
# Any
@router.post("/get", response_model=Book|list[Book])
def get(book: BookSearch, db: Session = Depends(get_db)):
    try:
        temp: list[list[Book]] = []
        if book.book_id is not None:
            temp.append([get_book_by_id(book.book_id, db)])
        if book.or_title is not None:
            temp.append(get_books_by_title(book.or_title, db))
        if book.title is not None:
            temp.append(get_books_by_title(book.title, db))
        if book.or_series is not None:
            temp.append(get_books_by_series(book.or_series, db))
        if book.series is not None:
            temp.append(get_books_by_series(book.series, db))
        if book.author_id is not None:
            temp.append(get_books_by_author_id(book.author_id, db))
        if book.author_name is not None:
            temp.append(get_books_by_author_name(book.author_name, db))
        if book.author_surname is not None:
            temp.append(get_books_by_author_surname(book.author_surname, db))
        if book.author_birth is not None:
            temp.append(get_books_by_author_birth_year(book.author_birth, db))
        if book.author_death is not None:
            temp.append(get_books_by_author_death_year(book.author_death, db))
        if book.or_lang is not None:
            temp.append(get_books_by_language(book.or_lang, db))
        if book.or_lang_id is not None:
            temp.append(get_books_by_language_id(book.or_lang_id, db))
        if book.lang is not None:
            temp.append(get_books_by_language(book.lang, db))
        if book.lang_id is not None:
            temp.append(get_books_by_language_id(book.lang_id, db))

        inter = False
        if book.intersect:
            inter = True

        return get_results(temp, inter)[0]

    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


# Any
@router.post("/alt-get", response_model=Book)
def alt_get(cond: dict, db: Session = Depends(get_db)):
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
"""


# Any
@router.get("/get-by-id", response_model=Book|None)
def get_by_id(book_id: int, db: Session = Depends(get_db)):
    return try_perform(get_book_by_id, book_id, db)

# Any
@router.get("/get-by-title", response_model=Book | list[Book] | None)
def get_by_title(title: str, db: Session = Depends(get_db)):
    return try_perform(get_books_by_title, title, db)

# Any
@router.get("/get-by-series", response_model=Book | list[Book] | None)
def get_by_series(series: str, db: Session = Depends(get_db)):
    return try_perform(get_books_by_series, series, db)

# Any
@router.get("/get-by-author-id", response_model=Book | list[Book] | None)
def get_by_author_id(author_id: int, db: Session = Depends(get_db)):
    return try_perform(get_books_by_author_id, author_id, db)

# Any
@router.get("/get-by-author-name", response_model=Book | list[Book] | None)
def get_by_author_name(author_name: str, db: Session = Depends(get_db)):
    return try_perform(get_books_by_author_name, author_name, db)

# Any
@router.get("/get-by-author-surname", response_model=Book | list[Book] | None)
def get_by_author_surname(author_surname: str, db: Session = Depends(get_db)):
    return try_perform(get_books_by_author_surname, author_surname, db)

# Any
@router.get("/get-by-author-birth-year", response_model=Book | list[Book] | None)
def get_by_author_birth_year(author_birth_year: str, db: Session = Depends(get_db)):
    return try_perform(get_books_by_author_birth_year, author_birth_year, db)

# Any
@router.get("/get-by-author-death-year", response_model=Book | list[Book] | None)
def get_by_author_death_year(author_death_year: str, db: Session = Depends(get_db)):
    return try_perform(get_books_by_author_death_year, author_death_year, db)

# Any
@router.get("/get-by-lang-id", response_model=Book | list[Book] | None)
def get_by_lang_id(lang_id: int, db: Session = Depends(get_db)):
    return try_perform(get_books_by_language_id, lang_id, db)

# Any
@router.get("/get-by-lang", response_model=Book | list[Book] | None)
def get_by_lang(lang: str, db: Session = Depends(get_db)):
    return try_perform(get_books_by_language, lang, db)