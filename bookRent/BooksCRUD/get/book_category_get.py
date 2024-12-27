from typing import Type, List

from fastapi.params import Depends
from sqlalchemy.orm import Session

from bookRent.db_config import get_db
from bookRent.models.book_category_model import BookCategory
from bookRent.schematics import book_category_schemas


def get_all_book_categories(db: Session = Depends(get_db)):
    bcs = db.query(BookCategory).all()
    return models_to_schemas(bcs)

def get_book_categories_by_book_id(book_id: int, db: Session = Depends(get_db())):
    bcs = db.query(BookCategory).filter_by(book_id=book_id).all()
    return models_to_schemas(bcs)

def get_book_categories_by_category_id(category_id: int, db: Session = Depends(get_db())):
    bcs = db.query(BookCategory).filter_by(category_id=category_id).all()
    return models_to_schemas(bcs)


def model_to_schema(model: Type[BookCategory] | None):
    if model is None:
        return None
        #raise HTTPException(status_code=404, detail="Annotation not found")

    return book_category_schemas.BookCategory(
        book_id=model.book_id,
        category_id=model.category_id
    )


def models_to_schemas(models: List[Type[BookCategory]]):
    schemas = []
    for model in models:
        schema: book_category_schemas.BookCategory = model_to_schema(model)
        schemas.append(schema)
    return schemas