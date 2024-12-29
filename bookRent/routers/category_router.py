from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from bookRent.BooksCRUD.add.category_add import create_category
from bookRent.BooksCRUD.get.category_get import get_category_by_id, get_category_by_name, get_categories_by_name, \
    get_all_categories
from bookRent.BooksCRUD.tools import try_perform
from bookRent.db_config import get_db
from bookRent.schematics.category_schemas import CategoryCreate, Category

router = APIRouter()

# Worker
@router.post("/add")
def add(category: CategoryCreate, db: Session = Depends(get_db)):
    return try_perform(create_category, category, db=db)


@router.get("/get-all", response_model=list[Category] | None)
def get_all(db: Session = Depends(get_db)):
    return try_perform(get_all_categories, db=db)


@router.get("/get-by-id", response_model=Category | None)
def get_by_id(cat_id: int, db: Session = Depends(get_db)):
    return try_perform(get_category_by_id, cat_id, db=db)

@router.get("/get-by-name-prec", response_model=Category | None)
def get_by_name_prec(name: str, db: Session = Depends(get_db)):
    return try_perform(get_category_by_name, name, db=db)

@router.get("/get-by-name", response_model=Category | list[Category] | None)
def get_by_name(name: str, db: Session = Depends(get_db)):
    return try_perform(get_categories_by_name, name, db=db)