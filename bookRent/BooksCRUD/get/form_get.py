from fastapi import Depends
from sqlalchemy.orm import Session

from bookRent.db_config import get_db
from bookRent.models.form_model import Form, models_to_schemas, model_to_schema


# === FORM ===

def get_all_forms(db: Session = Depends(get_db)):
    fs = db.query(Form).all()
    return models_to_schemas(fs)

def get_form(form: str, db: Session = Depends(get_db())):
    f = db.query(Form).filter(Form.form.ilike(form)).first()
    return model_to_schema(f)


def get_forms(form: str, db: Session = Depends(get_db())):
    fs = db.query(Form).filter(Form.form.ilike(f"%{form}%")).all()
    return models_to_schemas(fs)


def get_form_by_id(form_id: int, db: Session = Depends(get_db())):
    f = db.query(Form).filter_by(id=form_id).first()
    return model_to_schema(f)