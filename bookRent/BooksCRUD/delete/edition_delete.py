from fastapi import Depends
from sqlalchemy.orm import Session

from bookRent.BooksCRUD.delete.annotation_delete import delete_annotations_by_ed_id
from bookRent.BooksCRUD.delete.copy_delete import delete_copies_by_ed_id
from bookRent.BooksCRUD.tools import try_commit
from bookRent.db_config import get_db
from bookRent.models.edition_model import EditionInfo


def delete_edition(ed_id: int, db: Session = Depends(get_db())):
    db_edition = db.query(EditionInfo).filter_by(id=ed_id).first()
    if db_edition is None:
        return True

    #if delete_annotations_by_ed_id(ed_id, db):
    #    print("Ed annotations deleted")
    delete_copies_by_ed_id(ed_id, db)
    print("Copies deleted")

    db.delete(db_edition)
    try_commit(db, "An error has occurred during edition deletion")
    return True


def delete_editions_by_book_id(book_id: int, db: Session = Depends(get_db())):
    db_editions = db.query(EditionInfo).filter_by(book_id=book_id).all()
    print(db_editions)
    for ed in db_editions:
        delete_edition(ed.id, db)
    return True