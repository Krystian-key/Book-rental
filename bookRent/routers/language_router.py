from fastapi import APIRouter, HTTPException

from bookRent.BooksCRUD.add.language_add import create_language
from bookRent.BooksCRUD.get.copy_get import *
from bookRent.db_config import get_db
from bookRent.schematics.language_schemas import LanguageCreate

router = APIRouter()

# Worker
@router.post("/add")
def add(language: LanguageCreate, db: Session = Depends(get_db)):
    try:
        create_language(language, db)

    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


# User
@router.get("/get")
def get(cond: dict, db: Session = Depends(get_db)):
    try:
        if cond["lang"]:
            return get_language(cond["lang"], db)
        if cond["lang_id"]:
            return get_books_by_language_id(cond["lang_id"], db)
        return None

    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))