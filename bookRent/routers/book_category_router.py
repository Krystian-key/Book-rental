from fastapi import APIRouter
from fastapi.params import Depends
from sqlalchemy.orm import Session

from bookRent.BooksCRUD.add.book_category_add import create_book_category
from bookRent.BooksCRUD.get.book_category_get import get_book_categories_by_category_id, get_book_categories_by_book_id, \
    get_all_book_categories
from bookRent.BooksCRUD.tools import try_perform
from bookRent.db_config import get_db
from bookRent.dependiencies import role_required
from bookRent.schematics.book_category_schemas import BookCategoryCreate, BookCategory

router = APIRouter()

# Worker
@router.post("/add")
def add(book_cat: BookCategoryCreate, role: str = Depends(role_required(['Worker', 'Admin'])), db: Session = Depends(get_db)):
    return try_perform(create_book_category, book_cat, db=db)

# Any
@router.get("/get-all", response_model=list[BookCategory] | None)
def get_all(db: Session = Depends(get_db)):
    return try_perform(get_all_book_categories, db=db)

# Any
@router.get("/get-by-book-id", response_model=BookCategory | list[BookCategory] | None)
def get_for_book(book_id: int, db: Session = Depends(get_db)):
    return try_perform(get_book_categories_by_book_id, book_id, db=db)

# Any
@router.get("/get-by-category-id", response_model=BookCategory | list[BookCategory] | None)
def get_for_category(category_id: int, db: Session = Depends(get_db)):
    return try_perform(get_book_categories_by_category_id, category_id, db=db)