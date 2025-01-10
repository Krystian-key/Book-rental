from fastapi import Depends
from sqlalchemy.orm import Session

from bookRent.db_config import get_db
from bookRent.models.annotation_model import Annotation, models_to_schemas, model_to_schema
from bookRent.models.copy_model import Copy
from bookRent.models.edition_model import EditionInfo


# === ANNOTATION ===

def get_all_annotations(db:Session = Depends(get_db)):
    anns = db.query(Annotation).all()
    return models_to_schemas(anns)

def get_annotation_by_id(annotation_id: int, db: Session = Depends(get_db())):
    ann = db.query(Annotation).filter_by(id=annotation_id).first()
    return model_to_schema(ann)

def get_annotations_by_copy_id(copy_id: int, db: Session = Depends(get_db())):
    anns = db.query(Annotation).filter_by(copy_id=copy_id).all()
    return models_to_schemas(anns)

def get_annotations_by_edition_id(edition_id: int, db: Session = Depends(get_db())):
    anns = db.query(Annotation).filter_by(ed_id=edition_id).all()
    return models_to_schemas(anns)

def get_annotations_by_book_id(book_id: int, db: Session = Depends(get_db())):
    anns = db.query(Annotation).filter_by(book_id=book_id).all()
    return models_to_schemas(anns)

def get_all_annotations_for_edition(ed_id: int, db: Session = Depends(get_db())):
    edition = db.query(EditionInfo).filter_by(id=ed_id).first()
    if not edition:
        return []

    result = get_annotations_by_edition_id(ed_id, db)
    result.extend(get_annotations_by_book_id(edition.book_id, db))
    return result

def get_all_annotations_for_copy(copy_id: int, db: Session = Depends(get_db())):
    copy = db.query(Copy).filter_by(id=copy_id).first()
    if not copy:
        return []

    result = get_annotations_by_copy_id(copy_id, db)
    result.extend(get_all_annotations_for_edition(copy.ed_id, db))
    return result