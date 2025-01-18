from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from bookRent.BooksCRUD.add.language_add import create_language
from bookRent.BooksCRUD.delete.language_delete import delete_language
from bookRent.BooksCRUD.get.language_get import get_all_languages, get_language_by_id, get_language, get_languages
from bookRent.BooksCRUD.tools import try_perform
from bookRent.BooksCRUD.update.language_update import update_lang
from bookRent.db_config import get_db
from bookRent.dependiencies import role_required
from bookRent.schematics.language_schemas import LanguageCreate, Language, LanguageUpdate

router = APIRouter()

# Worker
@router.post("/add", status_code=201, response_model=Language | None)
def add(language: LanguageCreate, role: str = Depends(role_required(['Worker', 'Admin'])), db: Session = Depends(get_db)):
    return try_perform(create_language, language, db=db)


# === GET ===
# === ANY ===


@router.get("/get-all", response_model=list[Language] | None)
def get_all(db: Session = Depends(get_db)):
    return try_perform(get_all_languages, db=db)


@router.get("/get-by-id", response_model=Language | None)
def get_by_id(id: int, db: Session = Depends(get_db)):
    return try_perform(get_language_by_id, id, db=db)


@router.get("/get-by-name-prec", response_model=Language | None)
def get_by_name_prec(name: str, db: Session = Depends(get_db)):
    return try_perform(get_language, name, db=db)


@router.get("/get-by-name", response_model=Language | list[Language] | None)
def get_by_name(name: str, db: Session = Depends(get_db)):
    return try_perform(get_languages, name, db=db)


# === UPDATE ===

# Worker
@router.patch("/update", response_model=Language | None)
def update(language: LanguageUpdate, role: str = Depends(role_required(['Worker', 'Admin'])), db: Session = Depends(get_db)):
    return try_perform(update_lang, language, db=db)


# === DELETE ===


# Worker
@router.delete("/delete")
def delete(id: int, role: str = Depends(role_required(['Worker', 'Admin'])), db: Session = Depends(get_db)):
    return try_perform(delete_language, id, db=db)