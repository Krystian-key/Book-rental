from fastapi import Depends
from sqlalchemy import and_, not_
from sqlalchemy.orm import Session

from bookRent.BooksCRUD.tools import try_commit
from bookRent.db_config import get_db
from bookRent.models.category_model import Category, model_to_schema
from bookRent.schematics.category_schemas import CategoryUpdate


def update_category(cat: CategoryUpdate, db: Session = Depends(get_db)):
    db_cat = db.query(Category).filter(Category.id == cat.id).first()
    if db_cat is None:
        raise ValueError(f'Category with id {cat.id} does not exist')

    existing_cat = db.query(Category).filter(
        and_(
            Category.category.ilike(cat.category),
            not_(Category.id == cat.id)
        )
    ).first()
    if existing_cat is not None:
        raise ValueError(f'Category {cat.category} already exists and has id {existing_cat.id}')

    db_cat.category = cat.category
    try_commit(db, "An error has occurred during category update")
    return model_to_schema(db_cat)