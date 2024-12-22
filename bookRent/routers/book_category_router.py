from fastapi import APIRouter, HTTPException
from fastapi.params import Depends
from sqlalchemy.orm import Session

from bookRent.BooksCRUD.add.book_category_add import create_book_category
from bookRent.BooksCRUD.get.book_category_get import get_book_categories_by_category_id, get_book_categories_by_book_id
from bookRent.BooksCRUD.tools import try_perform
from bookRent.db_config import get_db
from bookRent.schematics.book_category_schemas import BookCategoryCreate, BookCategory

router = APIRouter()

# Worker
@router.post("/add")
def add(book_cat: BookCategoryCreate, db: Session = Depends(get_db)):
    try:
        return create_book_category(book_cat, db)

    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

# Any
@router.get("/get-by-book-id", response_model=BookCategory)
def get_for_book(book_id: int, db: Session = Depends(get_db)):
    return try_perform(get_book_categories_by_book_id, book_id, db)

# Any
@router.get("/get-by-category-id", response_model=BookCategory)
def get_for_category(category_id: int, db: Session = Depends(get_db)):
    return try_perform(get_book_categories_by_category_id, category_id, db)