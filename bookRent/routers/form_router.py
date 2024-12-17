from fastapi import APIRouter, HTTPException

from bookRent.BooksCRUD.add.form_add import create_form
from bookRent.BooksCRUD.get.copy_get import *
from bookRent.db_config import get_db
from bookRent.schematics.form_schemas import FormCreate

router = APIRouter()

# Worker
@router.post("/add")
def add(form: FormCreate, db: Session = Depends(get_db)):
    try:
        return create_form(form, db)

    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


# User
@router.get("/get")
def get(cond: dict, db: Session = Depends(get_db())):
    try:
        if cond["form"]:
            return get_form(cond["form"], db)
        if cond["form_id"]:
            return get_books_by_language_id(cond["form_id"], db)
        return None

    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))