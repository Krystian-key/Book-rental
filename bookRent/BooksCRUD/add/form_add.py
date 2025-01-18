from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session

from bookRent.BooksCRUD.tools import try_commit
from bookRent.db_config import get_db
from bookRent.models.form_model import Form, model_to_schema
from bookRent.schematics.form_schemas import FormCreate


def create_form(form: FormCreate,  db: Session = Depends(get_db())):
    db_form = Form(form=form.form)

    existing_form = db.query(Form).filter(Form.form.ilike(form.form)).first()
    if existing_form:
        raise HTTPException(status_code=409, detail=f"Form \'{db_form.form}\' already exists")

    db.add(db_form)
    try_commit(db, "An error has occurred during form adding")
    return model_to_schema(db_form)