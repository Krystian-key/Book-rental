from fastapi import Depends, HTTPException
from sqlalchemy import or_
from sqlalchemy.orm import Session

from bookRent.BooksCRUD.tools import try_commit
from bookRent.db_config import get_db
from bookRent.models.book_model import Book
from bookRent.models.edition_model import EditionInfo
from bookRent.models.person_model import Person


def delete_person(person_id: int, db: Session = Depends(get_db())):
    books = db.query(Book).filter_by(author_id=person_id).all()
    editions = db.query(EditionInfo).filter(
        or_(
            EditionInfo.illustrator_id==person_id,
            EditionInfo.translator_id==person_id
        )
    ).all()
    if len(books) > 0 or len(editions) > 0:
        print(books, editions)
        raise HTTPException(status_code=409, detail="Cannot delete person when any book or edition refers to them")

    db_person = db.query(Person).filter_by(id=person_id).first()
    if db_person is None:
        return True

    db.delete(db_person)
    try_commit(db, "An error has occurred during person deletion")
    return True