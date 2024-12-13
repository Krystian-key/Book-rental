from fastapi import Depends
from sqlalchemy.orm import Session

from bookRent.db_config import get_db
from bookRent.models.models import Form

# === FORM ===

def get_form(form: str, db: Session = Depends(get_db())):
    return db.query(Form).filter_by(form=form).first()

def get_form_by_id(form_id: int, db: Session = Depends(get_db())):
    return db.query(Form).filter_by(id=form_id).first()