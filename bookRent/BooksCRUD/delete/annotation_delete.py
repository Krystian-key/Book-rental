from fastapi import Depends
from sqlalchemy.orm import Session

from bookRent.BooksCRUD.tools import try_commit
from bookRent.db_config import get_db
from bookRent.models.annotation_model import Annotation


def delete_annotation(ann_id: int, db: Session = Depends(get_db())):
    db_ann = db.query(Annotation).filter_by(id=ann_id).first()
    if db_ann is None:
        return True

    db.delete(db_ann)
    try_commit(db, "An error has occurred during annotation deletion")
    return True


def delete_annotations_by_copy_id(copy_id: int, db: Session = Depends(get_db())):
    db_anns = db.query(Annotation).filter_by(copy_id=copy_id).all()
    for db_ann in db_anns:
        db.delete(db_ann)
    try_commit(db, "An error has occurred during annotations deletion")
    return True


def delete_annotations_by_ed_id(ed_id: int, db: Session = Depends(get_db())):
    db_anns = db.query(Annotation).filter_by(ed_id=ed_id).all()
    for db_ann in db_anns:
        db.delete(db_ann)
    try_commit(db, "An error has occurred during annotations deletion")
    return True


def delete_annotations_by_book_id(book_id: int, db: Session = Depends(get_db())):
    db_anns = db.query(Annotation).filter_by(book_id=book_id).all()
    for db_ann in db_anns:
        db.delete(db_ann)
    try_commit(db, "An error has occurred during annotations deletion")
    return True