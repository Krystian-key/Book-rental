from fastapi import HTTPException
from fastapi.params import Depends
from sqlalchemy.orm import Session

from bookRent.BooksCRUD.tools import try_commit
from bookRent.db_config import get_db
from bookRent.models.book_category_model import BookCategory, model_to_schema
from bookRent.models.book_model import Book
from bookRent.models.category_model import Category
from bookRent.schematics.book_category_schemas import BookCategoryCreate


def create_book_category(book_cat: BookCategoryCreate, db: Session = Depends(get_db())):
    item = db.query(Book).filter_by(id=book_cat.book_id).first()
    if item is None:
        raise ValueError(f'Book {book_cat.book_id} does not exist')

    item = db.query(Category).filter_by(id=book_cat.category_id).first()
    if item is None:
        raise ValueError(f'Category {book_cat.category_id} does not exist')

    item = db.query(BookCategory).filter_by(book_id=book_cat.book_id, category_id=book_cat.category_id).first()
    if item is not None:
        raise HTTPException(status_code=409, detail=f'Book {book_cat.book_id} already has category {book_cat.category_id}')

    db_book_cat = BookCategory(
        book_id=book_cat.book_id,
        category_id=book_cat.category_id,
    )
    db.add(db_book_cat)
    try_commit(db, "An error has occurred during adding category to the book")
    return model_to_schema(db_book_cat)