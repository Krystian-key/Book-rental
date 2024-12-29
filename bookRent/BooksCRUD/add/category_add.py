from fastapi import Depends
from sqlalchemy.orm import Session

from bookRent.BooksCRUD.tools import try_commit
from bookRent.db_config import get_db
from bookRent.models.category_model import Category
from bookRent.schematics.category_schemas import CategoryCreate


def create_category(category: CategoryCreate, db: Session = Depends(get_db())):
    if category.category == "":
        raise ValueError(f"Category must not be empty")

    db_category = Category(category=category.category.lower())
    item = db.query(Category).filter_by(category=db_category.category).first()
    if item:
        raise ValueError(f"Category \'{db_category.category}\' already exists")

    db.add(db_category)
    return {"message": try_commit(
        db,
        f"Category \'{db_category.category}\' has been added",
        "An error has occurred during category adding"
    )}