from fastapi import Depends
from sqlalchemy import and_, not_
from sqlalchemy.orm import Session

from bookRent.BooksCRUD.tools import try_commit
from bookRent.db_config import get_db
from bookRent.models.language_model import Language, model_to_schema
from bookRent.schematics.language_schemas import LanguageUpdate


def update_lang(lang: LanguageUpdate, db: Session = Depends(get_db)):
    db_lang = db.query(Language).filter(Language.id == lang.id).first()
    if db_lang is None:
        raise ValueError(f'Language with id {lang.id} does not exist')

    existing_lang = db.query(Language).filter(
        and_(
            Language.lang.ilike(lang.lang),
            not_(Language.id == lang.id)
        )
    ).first()
    if existing_lang is not None:
        raise ValueError(f'Language {lang.lang} already exists and has id {existing_lang.id}')

    db_lang.lang = lang.lang
    try_commit(db, "An error has occurred during language update")
    return model_to_schema(db_lang)