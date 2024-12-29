from typing import Type, List

from fastapi import Depends
from sqlalchemy.orm import Session

from bookRent.db_config import get_db
from bookRent.models.form_model import Form
from bookRent.schematics import form_schemas


# === FORM ===

def get_all_forms(db: Session = Depends(get_db)):
    fs = db.query(Form).all()
    return models_to_schemas(fs)

def get_form(form: str, db: Session = Depends(get_db())):
    f = db.query(Form).filter_by(form=form.lower()).first()
    return model_to_schema(f)


def get_forms(form: str, db: Session = Depends(get_db())):
    fs = db.query(Form).filter(Form.form.ilike(f"%{form}%")).all()
    return models_to_schemas(fs)


def get_form_by_id(form_id: int, db: Session = Depends(get_db())):
    f = db.query(Form).filter_by(id=form_id).first()
    return model_to_schema(f)


def model_to_schema(model: Type[Form] | None):
    if model is None:
        return None
        #raise HTTPException(status_code=404, detail="Form not found")

    return form_schemas.Form(
        id=model.id,
        form=model.form
    )


def models_to_schemas(models: List[Type[Form]]):
    schemas = []
    for model in models:
        schema: form_schemas.Form = model_to_schema(model)
        schemas.append(schema)
    return schemas