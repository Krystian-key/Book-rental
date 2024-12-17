from fastapi import Depends
from sqlalchemy.orm import Session

from bookRent.BooksCRUD.tools import try_commit
from bookRent.db_config import get_db
from bookRent.models.form_model import Form
from bookRent.schematics.form_schemas import FormCreate


def create_form(form: FormCreate,  db: Session = Depends(get_db())):
    db_form = Form(form=form.form.lower())

    existing_form = db.query(Form).filter_by(form=db_form.form).first()
    if existing_form:
        raise ValueError(f"Form \'{db_form.form}\' already exists")

    db.add(db_form)
    return {"message": try_commit(
        db,
        f"Form \'{db_form.form}\' has been added",
        "An error has occurred during form adding"
    )}