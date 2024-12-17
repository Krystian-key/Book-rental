from fastapi import APIRouter, HTTPException
from fastapi.params import Depends
from sqlalchemy.orm import Session

from bookRent.BooksCRUD.add.book_category_add import create_book_category
from bookRent.BooksCRUD.get.book_category_get import get_book_categories_by_category_id, get_book_categories_by_book_id
from bookRent.BooksCRUD.tools import get_results
from bookRent.db_config import get_db
from bookRent.schematics.book_category_schemas import BookCategoryCreate

router = APIRouter()


# Worker
@router.post("/add")
def add(book_cat: BookCategoryCreate, db: Session = Depends(get_db())):
    return create_book_category(book_cat, db)


# User
@router.post("/get")
def get(cond: dict, db: Session = Depends(get_db())):
    try:
        temp = []

        if cond["book_id"] is not None:
            temp.append(get_book_categories_by_book_id(cond["book_id"], db))
        if cond["category_id"] is not None:
            temp.append(get_book_categories_by_category_id(cond["category_id"], db))

        inter = False
        if cond["intersect"]:
            inter = True

        return get_results(temp, inter)

    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


# User
@router.get("/get-all-for-book")
def get_for_book(book_id: int, db: Session = Depends(get_db())):
    return get_book_categories_by_book_id(book_id, db)

# User
@router.get("/get-all-for-category")
def get_for_category(category_id: int, db: Session = Depends(get_db())):
    return get_book_categories_by_category_id(category_id, db)