from fastapi import Depends
from sqlalchemy import and_, not_
from sqlalchemy.orm import Session

from bookRent.BooksCRUD.tools import try_commit
from bookRent.db_config import get_db
from bookRent.models.form_model import Form, model_to_schema
from bookRent.schematics.form_schemas import FormUpdate


def update_form(form: FormUpdate, db: Session = Depends(get_db)):
    db_form = db.query(Form).filter(Form.id == form.id).first()
    if db_form is None:
        raise ValueError(f"Form with id {form.id} does not exist")

    existing_form = db.query(Form).filter(
        and_(
            Form.form.ilike(form.form),
            not_(Form.id == form.id)
        )
    ).first()
    if existing_form is not None:
        raise ValueError(f'Form {form.form} already exists and has id {existing_form.id}')

    db_form.form = form.form
    try_commit(db, "An error has occurred during form update")
    return model_to_schema(db_form)