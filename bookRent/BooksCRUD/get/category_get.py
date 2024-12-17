from fastapi import Depends
from sqlalchemy.orm import Session

from bookRent.db_config import get_db
from bookRent.models.category_model import Category


def get_category_by_id(cat_id: int, db: Session = Depends(get_db())):
    return db.query(Category).filter_by(id = cat_id).first()

def get_category_by_name(name: str, db: Session = Depends(get_db())):
    return db.query(Category).filter_by(category = name.lower()).first()