from typing import Type, List

from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session

from bookRent.db_config import get_db
from bookRent.models.annotation_model import Annotation
from bookRent.models.copy_model import Copy
from bookRent.models.edition_model import EditionInfo
from bookRent.schematics import annotation_schemas


# === ANNOTATION ===

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
        #raise ValueError(f"Edition with id {ed_id} does not exist")

    result = get_annotations_by_edition_id(ed_id, db)
    result.extend(get_annotations_by_book_id(edition.book_id, db))
    return result

def get_all_annotations_for_copy(copy_id: int, db: Session = Depends(get_db())):
    copy = db.query(Copy).filter_by(id=copy_id).first()
    if not copy:
        return []
        #raise ValueError(f"Copy with id {copy_id} does not exist")

    result = get_annotations_by_copy_id(copy_id, db)
    result.extend(get_all_annotations_for_edition(copy.ed_id, db))
    return result


def model_to_schema(model: Type[Annotation] | None):
    if model is None:
        return None
        #raise HTTPException(status_code=404, detail="Annotation not found")

    return annotation_schemas.Annotation(
        id=model.id,
        book_id=model.book_id,
        ed_id=model.ed_id,
        copy_id=model.copy_id,
        content=model.content,
    )


def models_to_schemas(models: List[Type[Annotation]]):
    schemas = []
    for model in models:
        schema: annotation_schemas.Annotation = model_to_schema(model)
        schemas.append(schema)
    return schemas