from fastapi import Depends
from sqlalchemy.orm import Session

from bookRent.BooksCRUD.tools import try_commit
from bookRent.db_config import get_db
from bookRent.models.annotation_model import Annotation, model_to_schema
from bookRent.models.book_model import Book
from bookRent.models.copy_model import Copy
from bookRent.models.edition_model import EditionInfo
from bookRent.schematics.annotation_schemas import AnnotationCreate


def create_annotation(ann: AnnotationCreate, db: Session = Depends(get_db())):
    if not (ann.book_id or ann.ed_id or ann.copy_id):
        raise ValueError("No object to assign an annotation")

    if ann.content == "":
        raise ValueError("Annotation content is empty")

    if ann.book_id:
        if ann.ed_id or ann.copy_id:
            raise ValueError("An annotation may be assigned to one object only")

        ann.ed_id = None
        ann.copy_id = None

        book = db.query(Book).filter_by(id = ann.book_id).first()
        print(book)
        if not book:
            raise ValueError(f"Book with id {ann.book_id} does not exist")

    if ann.ed_id:
        if ann.book_id or ann.copy_id:
            raise ValueError("An annotation may be assigned to one object only")

        ann.book_id = None
        ann.copy_id = None

        ed = db.query(EditionInfo).filter_by(id=ann.ed_id).first()
        if not ed:
            raise ValueError(f"Edition with id {ann.ed_id} does not exist")

    if ann.copy_id:
        if ann.ed_id or ann.book_id:
            raise ValueError("An annotation may be assigned to one object only")

        ann.ed_id = None
        ann.book_id = None

        copy = db.query(Copy).filter_by(id=ann.copy_id).first()
        if not copy:
            raise ValueError(f"Copy with id {ann.copy_id} does not exist")

    db_ann = Annotation(
        book_id = ann.book_id,
        ed_id = ann.ed_id,
        copy_id = ann.copy_id,
        content = ann.content
    )
    print(f"{db_ann.book_id} - {db_ann.ed_id} - {db_ann.copy_id} - {db_ann.content}")
    db.add(db_ann)
    try_commit(db, "An error has occurred during annotation adding")
    return model_to_schema(db_ann)