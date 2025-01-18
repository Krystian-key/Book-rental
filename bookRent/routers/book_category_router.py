from fastapi import APIRouter
from fastapi.params import Depends
from sqlalchemy.orm import Session

from bookRent.BooksCRUD.add.book_category_add import create_book_category
from bookRent.BooksCRUD.delete.book_category_delete import delete_book_category, delete_book_categories_by_book_id
from bookRent.BooksCRUD.get.book_category_get import get_book_categories_by_category_id, get_book_categories_by_book_id, \
    get_all_book_categories
from bookRent.BooksCRUD.tools import try_perform
from bookRent.db_config import get_db
from bookRent.dependiencies import role_required
from bookRent.schematics.book_category_schemas import BookCategoryCreate, BookCategory

router = APIRouter()

# Worker
@router.post("/add", status_code=201, response_model=BookCategory | None)
def add(book_cat: BookCategoryCreate, role: str = Depends(role_required(['Worker', 'Admin'])), db: Session = Depends(get_db)):
    return try_perform(create_book_category, book_cat, db=db)

# Any
@router.get("/get-all", response_model=list[BookCategory] | None)
def get_all(db: Session = Depends(get_db)):
    return try_perform(get_all_book_categories, db=db)

# Any
@router.get("/get-by-book-id", response_model=BookCategory | list[BookCategory] | None)
def get_for_book(id: int, db: Session = Depends(get_db)):
    return try_perform(get_book_categories_by_book_id, id, db=db)

# Any
@router.get("/get-by-category-id", response_model=BookCategory | list[BookCategory] | None)
def get_for_category(id: int, db: Session = Depends(get_db)):
    return try_perform(get_book_categories_by_category_id, id, db=db)


# === DELETE ===


# Worker
@router.delete("/delete")
def delete(book_id: int, cat_id: int, role: str = Depends(role_required(['Worker', 'Admin'])), db: Session = Depends(get_db)):
    return try_perform(delete_book_category, book_id, cat_id, db=db)


@router.delete("/delete-by-category-id")
def delete_all_for_category(cat_id: int, role: str = Depends(role_required(['Worker', 'Admin'])), db: Session = Depends(get_db)):
    return try_perform(delete_book_category, cat_id, db=db)


@router.delete("/delete-by-book-id")
def delete_all_for_book(book_id: int, role: str = Depends(role_required(['Worker', 'Admin'])), db: Session = Depends(get_db)):
    return try_perform(delete_book_categories_by_book_id, book_id, db=db)