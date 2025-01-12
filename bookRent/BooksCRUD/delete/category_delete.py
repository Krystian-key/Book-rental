from fastapi import Depends
from sqlalchemy.orm import Session

from bookRent.BooksCRUD.delete.book_category_delete import delete_book_categories_by_cat_id
from bookRent.BooksCRUD.tools import try_commit
from bookRent.db_config import get_db
from bookRent.models.category_model import Category


def delete_category(cat_id: int, db: Session = Depends(get_db())):
    db_cat = db.query(Category).filter_by(id = cat_id).first()
    if db_cat is None:
        return True

    #delete_book_categories_by_cat_id(cat_id, db)

    db.delete(db_cat)
    try_commit(db, "An error has occurred during category deletion")
    return True