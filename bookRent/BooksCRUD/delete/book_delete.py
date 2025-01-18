from fastapi import Depends
from sqlalchemy.orm import Session

from bookRent.BooksCRUD.delete.annotation_delete import delete_annotations_by_book_id
from bookRent.BooksCRUD.delete.edition_delete import delete_editions_by_book_id
from bookRent.BooksCRUD.tools import try_commit
from bookRent.db_config import get_db
from bookRent.models.book_model import Book


def delete_book(book_id: int, db: Session = Depends(get_db())):
    db_book = db.query(Book).filter_by(id=book_id).first()
    if db_book is None:
        return True
    #if delete_annotations_by_book_id(book_id, db):
    #    print("Book annotations deleted")

    delete_editions_by_book_id(book_id, db)
    print("Editions deleted")

    db.delete(db_book)
    try_commit(db, "An error occurred during book deletion")
    return True