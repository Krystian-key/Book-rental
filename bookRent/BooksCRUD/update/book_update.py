from fastapi import Depends
from sqlalchemy.orm import Session

from bookRent.BooksCRUD.tools import try_commit
from bookRent.db_config import get_db
from bookRent.models.book_model import Book, model_to_schema
from bookRent.models.language_model import Language
from bookRent.models.person_model import Person
from bookRent.schematics.book_schemas import BookUpdate


def update_book(book: BookUpdate, db: Session = Depends(get_db)):
    db_book = db.query(Book).filter(Book.id == book.id).first()
    if db_book is None:
        raise ValueError(f"Book with id {book.id} does not exist")

    if book.title is not None:
        db_book.title = book.title

    if book.series is not None:
        db_book.series = book.series

    if book.author_id is not None:
        author = db.query(Person).filter(Person.id == book.author_id).first()
        if author is None:
            raise ValueError(f"Author with id {book.author_id} does not exist")
        db_book.author_id = book.author_id

    if book.lang_id is not None:
        lang = db.query(Language).filter(Language.id == book.lang_id).first()
        if lang is None:
            raise ValueError(f"Language with id {book.lang_id} does not exist")
        db_book.lang_id = book.lang_id

    try_commit(db, "An error has occurred during book update")
    return model_to_schema(db_book)