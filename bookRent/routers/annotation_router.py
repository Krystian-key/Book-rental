from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from bookRent.BooksCRUD.add.annotation_add import create_annotation
import bookRent.BooksCRUD.get.annotation_get as ag
from bookRent.BooksCRUD.delete.annotation_delete import delete_annotation
from bookRent.BooksCRUD.tools import try_perform
from bookRent.db_config import get_db
from bookRent.dependiencies import role_required
from bookRent.schematics.annotation_schemas import AnnotationCreate, Annotation

router = APIRouter()

# Worker
@router.post("/add", status_code=201, response_model=Annotation | None)
def add(annotation: AnnotationCreate, role: str = Depends(role_required(['Worker', 'Admin'])), db: Session = Depends(get_db)):
    return try_perform(create_annotation, annotation, db=db)

# Any
@router.get("/get-all", response_model=list[Annotation] | None)
def get_all(db: Session = Depends(get_db)):
    return try_perform(ag.get_all_annotations, db=db)

# Any
@router.get("/get-by-id", response_model=Annotation | None)
def get_by_id(id: int, db: Session = Depends(get_db)):
    return try_perform(ag.get_annotation_by_id, id, db=db)

# Any
@router.get("/get-by-book-id", response_model=Annotation | list[Annotation] | None)
def get_by_book_id(id: int, db: Session = Depends(get_db)):
    return try_perform(ag.get_annotations_by_book_id, id, db=db)

# Any
@router.get("/get-by-edition-id", response_model=Annotation | list[Annotation] | None)
def get_by_edition_id(id: int, db: Session = Depends(get_db)):
    return try_perform(ag.get_annotations_by_edition_id, id, db=db)

# Any
@router.get("/get-by-copy-id", response_model=Annotation | list[Annotation] | None)
def get_by_copy_id(id: int, db: Session = Depends(get_db)):
    return try_perform(ag.get_annotations_by_copy_id, id, db=db)

# Any
@router.get("/get-all-for-edition", response_model=Annotation | list[Annotation] | None)
def get_all_for_edition(id: int, db: Session = Depends(get_db)):
    return try_perform(ag.get_all_annotations_for_edition, id, db=db)

# Any
@router.get("/get-all-for-copy", response_model=Annotation | list[Annotation] | None)
def get_all_for_copy(id: int, db: Session = Depends(get_db)):
    return try_perform(ag.get_all_annotations_for_copy, id, db=db)


# === DELETE ===


# Worker
@router.delete("/delete")
def delete(id: int, role: str = Depends(role_required(['Worker', 'Admin'])), db: Session = Depends(get_db)):
    return try_perform(delete_annotation, id, db=db)