from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session

from bookRent.BooksCRUD.add.category_add import create_category
from bookRent.BooksCRUD.get.category_get import get_category_by_id, get_category_by_name
from bookRent.db_config import get_db
from bookRent.schematics.category_schemas import CategoryCreate

router = APIRouter()

# Worker
@router.post("/add")
def add(category: CategoryCreate, db: Session = Depends(get_db())):
    try:
        return create_category(category, db)

    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


# User
@router.get("/get")
def get(cond: dict, db: Session = Depends(get_db())):
    try:
        if cond["category_id"] is not None:
            return get_category_by_id(cond["category_id"], db)
        if cond["category"] is not None:
            return get_category_by_name(cond["category"], db)

    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))