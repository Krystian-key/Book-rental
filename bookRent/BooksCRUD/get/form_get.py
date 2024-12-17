from fastapi import Depends
from sqlalchemy.orm import Session

from bookRent.BooksCRUD.tools import get_result
from bookRent.db_config import get_db
from bookRent.models.form_model import Form
from bookRent.schematics.search_schemas import FormSearch


# === FORM ===

def get_form(form: str, db: Session = Depends(get_db())):
    return db.query(Form).filter_by(form=form.lower()).first()

def get_form_by_id(form_id: int, db: Session = Depends(get_db())):
    return db.query(Form).filter_by(id=form_id).first()

# SearchModel
def get_forms(form: FormSearch, db: Session = Depends(get_db())):
    result = []
    query = db.query(Form)
    intersect = form.intersect

    if form.id:
        get_result(result, query, intersect, id=form.id)
    if form.form:
        get_result(result, query, intersect, form=form.form.lower())

    if intersect:
        return query.all()
    return list(set(result))