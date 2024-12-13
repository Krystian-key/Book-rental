from fastapi import Depends
from sqlalchemy.orm import Session

from bookRent.db_config import get_db
from bookRent.models.models import Language

# === LANGUAGE ===

def get_language(language: str, db: Session = Depends(get_db())):
    return db.query(Language).filter_by(language=language).first()

def get_language_by_id(lang_id: int, db: Session = Depends(get_db())):
    return db.query(Language).filter_by(id=lang_id).first()