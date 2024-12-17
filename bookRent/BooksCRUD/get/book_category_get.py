from fastapi.params import Depends
from sqlalchemy.orm import Session

from bookRent.db_config import get_db
from bookRent.models.book_category_model import BookCategory


def get_book_categories_by_book_id(book_id: int, db: Session = Depends(get_db())):
    return db.query(BookCategory).filter_by(book_id=book_id).all()

def get_book_categories_by_category_id(category_id: int, db: Session = Depends(get_db())):
    return db.query(BookCategory).filter_by(category_id=category_id).all()