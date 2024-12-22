from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session

from bookRent.BooksCRUD.add.category_add import create_category
from bookRent.BooksCRUD.get.category_get import get_category_by_id, get_category_by_name, get_categories_by_name
from bookRent.BooksCRUD.tools import try_perform
from bookRent.db_config import get_db
from bookRent.schematics.category_schemas import CategoryCreate, Category

router = APIRouter()

# Worker
@router.post("/add")
def add(category: CategoryCreate, db: Session = Depends(get_db)):
    try:
        return create_category(category, db)

    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/get-by-id", response_model=Category | None)
def get_by_id(cat_id: int, db: Session = Depends(get_db)):
    return try_perform(get_category_by_id, cat_id, db)

@router.get("/get-by-name-prec", response_model=Category)
def get_by_name_prec(name: str, db: Session = Depends(get_db)):
    return try_perform(get_category_by_name, name, db)

@router.get("/get-by-name", response_model=Category)
def get_by_name(name: str, db: Session = Depends(get_db)):
    return try_perform(get_categories_by_name, name, db)