from fastapi import Depends
from sqlalchemy.orm import Session

from bookRent.BooksCRUD.tools import try_commit
from bookRent.db_config import get_db
from bookRent.models.book_category_model import BookCategory


def delete_book_category(book_id: int, cat_id: int, db: Session = Depends(get_db())):
    db_bc = db.query(BookCategory).filter_by(book_id=book_id, cat_id=cat_id).first()
    if db_bc is None:
        return True

    db.delete(db_bc)
    try_commit(db, "An error occurred while deleting book category")
    return True


def delete_book_categories_by_book_id(book_id: int, db: Session = Depends(get_db())):
    db_bcs = db.query(BookCategory).filter_by(book_id=book_id).all()
    for db_bc in db_bcs:
        db.delete(db_bc)
    try_commit(db, "An error occurred while deleting book categories")
    return True


def delete_book_categories_by_cat_id(cat_id: int, db: Session = Depends(get_db())):
    db_bcs = db.query(BookCategory).filter_by(cat_id=cat_id).all()
    for db_bc in db_bcs:
        db.delete(db_bc)
    try_commit(db, "An error occurred while deleting book categories")
    return True