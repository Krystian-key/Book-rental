from typing import Type, List

from fastapi import Depends
from sqlalchemy.orm import Session

from bookRent.db_config import get_db
from bookRent.models.language_model import Language
from bookRent.schematics import language_schemas


# === LANGUAGE ===

def get_all_languages(db: Session = Depends(get_db)):
    langs = db.query(Language).all()
    return models_to_schemas(langs)

def get_language(language: str, db: Session = Depends(get_db())):
    lang = db.query(Language).filter(Language.lang.ilike(language)).first()
    return model_to_schema(lang)


def get_languages(language: str, db: Session = Depends(get_db())):
    langs = db.query(Language).filter(Language.lang.ilike(f"%{language}%")).all()
    return models_to_schemas(langs)


def get_language_by_id(lang_id: int, db: Session = Depends(get_db())):
    lang = db.query(Language).filter_by(id=lang_id).first()
    return model_to_schema(lang)


def model_to_schema(model: Type[Language] | None):
    if model is None:
        return None
        #raise HTTPException(status_code=404, detail="Language not found")

    return language_schemas.Language(
        id=model.id,
        lang=model.lang
    )


def models_to_schemas(models: List[Type[Language]]):
    schemas = []
    for model in models:
        schema: language_schemas.Language = model_to_schema(model)
        schemas.append(schema)
    return schemas