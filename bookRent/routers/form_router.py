from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from bookRent.BooksCRUD.add.form_add import create_form
from bookRent.BooksCRUD.get.form_get import get_all_forms, get_form_by_id, get_form, get_forms
from bookRent.BooksCRUD.tools import try_perform
from bookRent.db_config import get_db
from bookRent.dependiencies import role_required
from bookRent.schematics.form_schemas import FormCreate, Form

router = APIRouter()

# Worker
@router.post("/add", response_model=Form | None)
def add(form: FormCreate, role: str = Depends(role_required(['Worker', 'Admin'])), db: Session = Depends(get_db)):
    return try_perform(create_form, form, db=db)


# === GET ===
# === ANY ===


@router.get("/get-all", response_model=list[Form] | None)
def get_all(db: Session = Depends(get_db)):
    return try_perform(get_all_forms, db=db)


@router.get("/get-by-id", response_model=Form | None)
def get_by_id(id: int, db: Session = Depends(get_db)):
    return try_perform(get_form_by_id, id, db=db)


@router.get("/get-by-name-prec", response_model=Form | None)
def get_by_name_prec(name: str, db: Session = Depends(get_db)):
    return try_perform(get_form, name, db=db)


@router.get("/get-by-name", response_model=Form | list[Form] | None)
def get_by_name(name: str, db: Session = Depends(get_db)):
    return try_perform(get_forms, name, db=db)