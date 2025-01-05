from fastapi import Depends
from sqlalchemy.orm import Session

from bookRent.BooksCRUD.tools import try_commit
from bookRent.db_config import get_db
from bookRent.models.language_model import Language
from bookRent.schematics.language_schemas import LanguageCreate


def create_language(language: LanguageCreate, db: Session = Depends(get_db())):
    db_lang = Language(lang=language.lang)

    existing_lang = db.query(Language).filter(Language.lang.ilike(db_lang.lang)).first()

    if existing_lang:
        raise ValueError(f"Language \'{db_lang.lang}\' already exists")

    db.add(db_lang)
    return {"message":try_commit(
        db,
        f"Language \'{db_lang.lang}\' has been added",
        "An error has occurred during language adding"
    )}