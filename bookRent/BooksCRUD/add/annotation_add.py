from fastapi import Depends
from sqlalchemy.orm import Session

from bookRent.BooksCRUD.tools import try_commit
from bookRent.db_config import get_db
from bookRent.models.annotation_model import Annotation
from bookRent.models.book_model import Book
from bookRent.models.copy_model import Copy
from bookRent.models.edition_model import EditionInfo
from bookRent.schematics.annotation_schemas import AnnotationCreate


def create_annotation(ann: AnnotationCreate, db: Session = Depends(get_db())):
    if not (ann.book_id or ann.ed_id or ann.copy_id):
        raise ValueError("Nie ma obiektu, do którego należy przypisać adnotację")

    if ann.content == "":
        raise ValueError("Adnotacja nie może być pusta")

    if ann.book_id:
        if ann.ed_id or ann.copy_id:
            raise ValueError("Adnotacja może zostać przypisana tylko do jednego obiektu")

        book = db.query(Book).filter_by(id = ann.book_id).first()
        if not book:
            raise ValueError(f"Książka o id {ann.book_id} nie istnieje")

    if ann.ed_id:
        if ann.book_id or ann.copy_id:
            raise ValueError("Adnotacja może zostać przypisana tylko do jednego obiektu")

        ed = db.query(EditionInfo).filter_by(id=ann.ed_id).first()
        if not ed:
            raise ValueError(f"Wydanie o id {ann.ed_id} nie istnieje")

    if ann.copy_id:
        if ann.ed_id or ann.book_id:
            raise ValueError("Adnotacja może zostać przypisana tylko do jednego obiektu")

        copy = db.query(Copy).filter_by(id=ann.copy_id).first()
        if not copy:
            raise ValueError(f"Egzemplarz o id {ann.copy_id} nie istnieje")

    db_ann = Annotation(
        book_id = ann.book_id,
        ed_id = ann.ed_id,
        copy_id = ann.copy_id,
        content = ann.content
    )
    db.add(db_ann)
    return {"message": try_commit(
        db,
        f"Adnotacja została dodana",
        "Wystąpił błąd podczas dodawania książki"
    )}