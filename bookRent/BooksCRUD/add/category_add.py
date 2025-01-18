from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session

from bookRent.BooksCRUD.tools import try_commit
from bookRent.db_config import get_db
from bookRent.models.category_model import Category, model_to_schema
from bookRent.schematics.category_schemas import CategoryCreate


def create_category(category: CategoryCreate, db: Session = Depends(get_db())):
    if category.category == "":
        raise ValueError(f"Category must not be empty")

    db_category = Category(category=category.category)
    item = db.query(Category).filter(Category.category.ilike(db_category.category)).first()
    if item:
        raise HTTPException(status_code=409, detail=f"Category \'{db_category.category}\' already exists")

    db.add(db_category)
    try_commit(db, "An error has occurred during category adding")
    return model_to_schema(db_category)