from typing import Type, List

from fastapi import Depends
from sqlalchemy.orm import Session

from bookRent.db_config import get_db
from bookRent.models.category_model import Category
from bookRent.schematics import category_schemas


def get_all_categories(db: Session = Depends(get_db)):
    cats = db.query(Category).all()
    return models_to_schemas(cats)


def get_category_by_id(cat_id: int, db: Session = Depends(get_db())):
    cat = db.query(Category).filter_by(id = cat_id).first()
    return model_to_schema(cat)


def get_category_by_name(name: str, db: Session = Depends(get_db())):
    cat = db.query(Category).filter(Category.category.ilike(name)).first()
    return model_to_schema(cat)


def get_categories_by_name(name: str, db: Session = Depends(get_db())):
    cats = db.query(Category).filter(Category.category.ilike(f"%{name}%")).all()
    return models_to_schemas(cats)


def model_to_schema(model: Type[Category] | None):
    if model is None:
        return None
        #raise HTTPException(status_code=404, detail="Category not found")

    return category_schemas.Category(
        id = model.id,
        category = model.category,
    )


def models_to_schemas(models: List[Type[Category]]):
    schemas = []
    for model in models:
        schema: category_schemas.Category = model_to_schema(model)
        schemas.append(schema)
    return schemas