from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from bookRent.BooksCRUD.add.annotation_add import create_annotation
from bookRent.BooksCRUD.get.annotation_get import get_annotations_by_copy_id, get_annotation_by_id, \
    get_annotations_by_edition_id, get_annotations_by_book_id, \
    get_all_annotations_for_edition, get_all_annotations_for_copy, get_all_annotations
from bookRent.BooksCRUD.tools import try_perform
from bookRent.db_config import get_db
from bookRent.dependiencies import role_required
from bookRent.schematics.annotation_schemas import AnnotationCreate, Annotation

router = APIRouter()

# Worker
@router.post("/add", response_model=Annotation | None)
def add(annotation: AnnotationCreate, role: str = Depends(role_required(['Worker', 'Admin'])), db: Session = Depends(get_db)):
    return try_perform(create_annotation, annotation, db=db)

# Any
@router.get("/get-all", response_model=list[Annotation] | None)
def get_all(db: Session = Depends(get_db)):
    return try_perform(get_all_annotations, db=db)

# Any
@router.get("/get-by-id", response_model=Annotation | None)
def get_by_id(id: int, db: Session = Depends(get_db)):
    return try_perform(get_annotation_by_id, id, db=db)

# Any
@router.get("/get-by-book-id", response_model=Annotation | list[Annotation] | None)
def get_by_book_id(id: int, db: Session = Depends(get_db)):
    return try_perform(get_annotations_by_book_id, id, db=db)

# Any
@router.get("/get-by-edition-id", response_model=Annotation | list[Annotation] | None)
def get_by_edition_id(id: int, db: Session = Depends(get_db)):
    return try_perform(get_annotations_by_edition_id, id, db=db)

# Any
@router.get("/get-by-copy-id", response_model=Annotation | list[Annotation] | None)
def get_by_copy_id(id: int, db: Session = Depends(get_db)):
    return try_perform(get_annotations_by_copy_id, id, db=db)

# Any
@router.get("/get-all-for-edition", response_model=Annotation | list[Annotation] | None)
def get_all_for_edition(id: int, db: Session = Depends(get_db)):
    return try_perform(get_all_annotations_for_edition, id, db=db)

# Any
@router.get("/get-all-for-copy", response_model=Annotation | list[Annotation] | None)
def get_all_for_copy(id: int, db: Session = Depends(get_db)):
    return try_perform(get_all_annotations_for_copy, id, db=db)