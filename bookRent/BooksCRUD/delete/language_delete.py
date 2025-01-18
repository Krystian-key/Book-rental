from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session

from bookRent.BooksCRUD.tools import try_commit
from bookRent.db_config import get_db
from bookRent.models.book_model import Book
from bookRent.models.edition_model import EditionInfo
from bookRent.models.language_model import Language


def delete_language(lang_id: int, db: Session = Depends(get_db())):
    books = db.query(Book).filter_by(lang_id=lang_id).all()
    editions = db.query(EditionInfo).filter_by(ed_lang_id=lang_id).all()
    if len(books) > 0 or len(editions) > 0:
        print(books, editions)
        raise HTTPException(status_code=409, detail="Cannot delete language when any book or edition refers to it")

    db_lang = db.query(Language).filter_by(id=lang_id).first()
    if db_lang is None:
        return True

    db.delete(db_lang)
    try_commit(db, "An error has occurred during language deletion")
    return True