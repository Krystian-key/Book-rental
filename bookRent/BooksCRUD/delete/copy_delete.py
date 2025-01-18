from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session

from bookRent.BooksCRUD.delete.annotation_delete import delete_annotations_by_copy_id
from bookRent.BooksCRUD.tools import try_commit
from bookRent.BooksCRUD.update.reservation_update import cancel_reservations_by_copy_id
from bookRent.db_config import get_db
from bookRent.models.copy_model import Copy


def delete_copy(copy_id: int, db: Session = Depends(get_db())):
    db_copy = db.query(Copy).filter_by(id = copy_id).first()
    if db_copy is None:
        return True

    if db_copy.rented:
        raise HTTPException(status_code=409, detail="Cannot delete rented copy")

    #if delete_annotations_by_copy_id(copy_id, db):
    #    print("copy annotations deleted")
    if cancel_reservations_by_copy_id(copy_id, db):
        print("Reservations cancelled")

    db.delete(db_copy)
    try_commit(db, "An error has occurred during copy deletion")
    return True


def delete_copies_by_ed_id(ed_id: int, db: Session = Depends(get_db())):
    db_copies = db.query(Copy).filter_by(ed_id = ed_id).all()
    print(db_copies)
    for copy in db_copies:
        delete_copy(copy.id, db)
    return True