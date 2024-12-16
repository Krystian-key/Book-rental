from fastapi import Depends
from sqlalchemy.orm import Session

from bookRent.BooksCRUD.tools import get_result
from bookRent.db_config import get_db
from bookRent.models.language_model import Language
from bookRent.schematics.search_schemas import LanguageSearch


# === LANGUAGE ===

def get_language(language: str, db: Session = Depends(get_db())):
    return db.query(Language).filter_by(language=language).first()

def get_language_by_id(lang_id: int, db: Session = Depends(get_db())):
    return db.query(Language).filter_by(id=lang_id).first()

# SearchModel
def get_languages(language: LanguageSearch, db: Session = Depends(get_db())):
    result = []
    query = db.query(Language)
    intersect = language.intersect

    if language.id:
        get_result(result, query, intersect, id=language.id)

    if language.language:
        get_result(result, query, intersect, lang=language.language)

    if intersect:
        return query.all()
    return list(set(result))

