from fastapi import HTTPException

from fastapi.params import Depends
from sqlalchemy.orm import Session

from bookRent.BooksCRUD.tools import try_commit
from bookRent.db_config import get_db
from bookRent.models.book_model import Book, model_to_schema
from bookRent.models.language_model import Language
from bookRent.models.person_model import Person
from bookRent.schematics.book_schemas import BookCreate


def create_book(book: BookCreate, db: Session = Depends(get_db())):
    existing_author = db.query(Person).filter_by(id=book.author_id).first()
    if existing_author is None:
        raise ValueError(f"Author with id {book.author_id} does not exist")

    existing_lang = db.query(Language).filter_by(id=book.lang_id).first()
    if existing_lang is None:
        raise ValueError(f"Language with id {book.lang_id} does not exist")

    existing_book = db.query(Book).filter(Book.title.ilike(book.title), Book.author_id==book.author_id).first()
    if existing_book:
        raise HTTPException(status_code=409, detail="Book \'{book.title}\' of author {book.author_id} already exists")

    db_book = Book(
        title=book.title,
        author_id=book.author_id,
        lang_id=book.lang_id,
        series=book.series
    )
    db.add(db_book)
    try_commit(db, "An error has occurred during book adding")
    return model_to_schema(db_book)