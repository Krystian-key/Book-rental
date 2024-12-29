from fastapi import APIRouter

from bookRent.BooksCRUD.add.form_add import create_form
from bookRent.BooksCRUD.get.copy_get import *
from bookRent.BooksCRUD.tools import try_perform
from bookRent.db_config import get_db
from bookRent.schematics.form_schemas import FormCreate, Form

router = APIRouter()

# Worker
@router.post("/add")
def add(form: FormCreate, db: Session = Depends(get_db)):
    return try_perform(create_form, form, db=db)


# === GET ===
# === ANY ===


@router.get("/get-all", response_model=list[Form] | None)
def get_all(db: Session = Depends(get_db)):
    return try_perform(get_all_forms, db=db)


@router.get("/get-by-id", response_model=Form | None)
def get_by_id(form_id: int, db: Session = Depends(get_db)):
    return try_perform(get_form_by_id, form_id, db=db)


@router.get("/get-by-name-prec", response_model=Form | None)
def get_by_name_prec(name: str, db: Session = Depends(get_db)):
    return try_perform(get_form, name, db=db)


@router.get("/get-by-name", response_model=Form | list[Form] | None)
def get_by_name(name: str, db: Session = Depends(get_db)):
    return try_perform(get_forms, name, db=db)