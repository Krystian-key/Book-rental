from fastapi.params import Depends
from sqlalchemy.orm import Session

from bookRent.BooksCRUD.tools import try_commit
from bookRent.db_config import get_db
from bookRent.models.book_model import Book
from bookRent.models.language_model import Language
from bookRent.models.person_model import Person
from bookRent.schematics.book_schemas import BookCreate


def create_book(book: BookCreate, db: Session = Depends(get_db())):
    existing_author = db.query(Person).filter_by(id=book.author_id).first()
    if existing_author is None:
        raise ValueError(f"Autor o id {book.author_id} nie istnieje")

    existing_lang = db.query(Language).filter_by(id=book.lang_id).first()
    if existing_lang is None:
        raise ValueError(f"Język o id {book.lang_id} nie istnieje")

    existing_book = db.query(Book).filter_by(title=book.title, author_id=book.author_id).first()
    if existing_book:
        raise ValueError(f"Książka {book.title} autora {book.author_id} już istnieje")

    db_book = Book(
        title=book.title,
        author_id=book.author_id,
        lang_id=book.lang_id,
        series=book.series
    )
    db.add(db_book)
    return {"message": try_commit(
        db,
        f"Książka {db_book.title} została dodana",
        "Wystąpił błąd podczas dodawania książki"
    )}