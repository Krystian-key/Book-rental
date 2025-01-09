from fastapi import APIRouter

from bookRent.BooksCRUD.add.book_add import create_book
from bookRent.BooksCRUD.get.copy_get import *
from bookRent.BooksCRUD.tools import try_perform
from bookRent.db_config import get_db
from bookRent.dependiencies import role_required
from bookRent.schematics.book_schemas import BookCreate, Book

router = APIRouter()

# Worker
@router.post("/add")
def add(book: BookCreate, role: str = Depends(role_required(['Worker', 'Admin'])), db: Session = Depends(get_db)):
    return try_perform(create_book, book, db=db)

# Any
@router.get("/get-all", response_model=list[Book] | None)
def get_all(db: Session = Depends(get_db)):
    return try_perform(get_all_books, db=db)

# Any
@router.get("/get-by-id", response_model=Book | None)
def get_by_id(id: int, db: Session = Depends(get_db)):
    return try_perform(get_book_by_id, id, db=db)

# Any
@router.get("/get-by-copy-id", response_model=Book | None)
def get_by_copy_id(id: int, db: Session = Depends(get_db)):
    return try_perform(get_book_by_copy_id, id, db=db)

# Any
@router.get("/get-by-title", response_model=Book | list[Book] | None)
def get_by_title(title: str, db: Session = Depends(get_db)):
    return try_perform(get_books_by_title, title, db=db)

# Any
@router.get("/get-by-series", response_model=Book | list[Book] | None)
def get_by_series(series: str, db: Session = Depends(get_db)):
    return try_perform(get_books_by_series, series, db=db)

# Any
@router.get("/get-by-author-id", response_model=Book | list[Book] | None)
def get_by_author_id(id: int, db: Session = Depends(get_db)):
    return try_perform(get_books_by_author_id, id, db=db)

# Any
@router.get("/get-by-author-name", response_model=Book | list[Book] | None)
def get_by_author_name(name: str, db: Session = Depends(get_db)):
    return try_perform(get_books_by_author_name, name, db=db)

# Any
@router.get("/get-by-author-surname", response_model=Book | list[Book] | None)
def get_by_author_surname(surname: str, db: Session = Depends(get_db)):
    return try_perform(get_books_by_author_surname, surname, db=db)

# Any
@router.get("/get-by-author-birth-year", response_model=Book | list[Book] | None)
def get_by_author_birth_year(birth: str, db: Session = Depends(get_db)):
    return try_perform(get_books_by_author_birth_year, birth, db=db)

# Any
@router.get("/get-by-author-death-year", response_model=Book | list[Book] | None)
def get_by_author_death_year(death: str, db: Session = Depends(get_db)):
    return try_perform(get_books_by_author_death_year, death, db=db)

# Any
@router.get("/get-by-language-id", response_model=Book | list[Book] | None)
def get_by_lang_id(id: int, db: Session = Depends(get_db)):
    return try_perform(get_books_by_language_id, id, db=db)

# Any
@router.get("/get-by-language-name", response_model=Book | list[Book] | None)
def get_by_lang(name: str, db: Session = Depends(get_db)):
    return try_perform(get_books_by_language, name, db=db)