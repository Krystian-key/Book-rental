from fastapi.params import Depends
from sqlalchemy.orm import Session

from bookRent.db_config import get_db
from bookRent.models.book_category_model import BookCategory, models_to_schemas


def get_all_book_categories(db: Session = Depends(get_db)):
    bcs = db.query(BookCategory).all()
    return models_to_schemas(bcs)

def get_book_categories_by_book_id(book_id: int, db: Session = Depends(get_db())):
    bcs = db.query(BookCategory).filter_by(book_id=book_id).all()
    return models_to_schemas(bcs)

def get_book_categories_by_category_id(category_id: int, db: Session = Depends(get_db())):
    bcs = db.query(BookCategory).filter_by(category_id=category_id).all()
    return models_to_schemas(bcs)