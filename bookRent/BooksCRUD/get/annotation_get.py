from fastapi import Depends
from sqlalchemy.orm import Session

from bookRent.db_config import get_db
from bookRent.models.annotation_model import Annotation
from bookRent.models.copy_model import Copy
from bookRent.models.edition_model import EditionInfo


# === ANNOTATION ===

def get_annotation_by_id(annotation_id: int, db: Session = Depends(get_db())):
    return db.query(Annotation).filter_by(id=annotation_id).first()

def get_annotations_by_copy_id(copy_id: int, db: Session = Depends(get_db())):
    return db.query(Annotation).filter_by(copy_id=copy_id).all()

def get_annotations_by_edition_id(edition_id: int, db: Session = Depends(get_db())):
    return db.query(Annotation).filter_by(ed_id=edition_id).all()

def get_annotations_by_book_id(book_id: int, db: Session = Depends(get_db())):
    return db.query(Annotation).filter_by(book_id=book_id).all()

def get_all_annotations_for_book(book_id: int, db: Session = Depends(get_db())):
    return get_annotations_by_book_id(book_id, db)

def get_all_annotations_for_edition(ed_id: int, db: Session = Depends(get_db())):
    edition = db.query(EditionInfo).filter_by(id=ed_id).first()
    if not edition:
        raise ValueError(f"Wydanie o id {ed_id} nie istnieje")

    result = get_annotations_by_edition_id(ed_id, db)
    result.extend(get_annotations_by_book_id(edition.book_id, db))
    return result

def get_all_annotations_for_copy(copy_id: int, db: Session = Depends(get_db())):
    copy = db.query(Copy).filter_by(id=copy_id).first()
    if not copy:
        raise ValueError(f"Egzemplarz o id {copy_id} nie istnieje")

    result = get_annotations_by_copy_id(copy_id, db)
    result.extend(get_all_annotations_for_edition(copy.ed_id, db))
    return result