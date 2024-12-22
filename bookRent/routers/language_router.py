from fastapi import APIRouter, HTTPException

from bookRent.BooksCRUD.add.language_add import create_language
from bookRent.BooksCRUD.get.copy_get import *
from bookRent.BooksCRUD.tools import try_perform
from bookRent.db_config import get_db
from bookRent.schematics.language_schemas import LanguageCreate, Language
from bookRent.schematics.search_schemas import LanguageSearch

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


@router.get("/get-by-id", response_model=Language)
def get_by_id(lang_id: int, db: Session = Depends(get_db)):
    return try_perform(get_language_by_id, lang_id, db)


@router.get("/get-by-name-prec", response_model=Language)
def get_by_name_prec(name: str, db: Session = Depends(get_db)):
    return try_perform(get_language, name, db)


@router.get("/get-by-name", response_model=Language)
def get_by_name(name: str, db: Session = Depends(get_db)):
    return try_perform(get_languages, name, db)