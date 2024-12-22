from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session

from bookRent.BooksCRUD.add.annotation_add import create_annotation
from bookRent.BooksCRUD.get.annotation_get import get_annotations_by_copy_id, get_annotation_by_id, \
    get_annotations_by_edition_id, get_annotations_by_book_id, \
    get_all_annotations_for_edition, get_all_annotations_for_copy
from bookRent.BooksCRUD.tools import try_perform
from bookRent.db_config import get_db
from bookRent.schematics.annotation_schemas import AnnotationCreate, Annotation

router = APIRouter()

# Worker
@router.post("/add")
async def add(annotation: AnnotationCreate, db: Session = Depends(get_db)):
    try:
        return create_annotation(annotation, db)

    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/get-by-id", response_model=Annotation)
def get_by_id(ann_id: int, db: Session = Depends(get_db)):
    return try_perform(get_annotation_by_id, ann_id, db)


# Any
@router.get("/get-by-book-id", response_model=Annotation)
def get_by_book_id(book_id: int, db: Session = Depends(get_db)):
    return try_perform(get_annotations_by_book_id, book_id, db)


@router.get("/get-by-edition-id", response_model=Annotation)
def get_by_edition_id(edition_id: int, db: Session = Depends(get_db)):
    return try_perform(get_annotations_by_edition_id, edition_id, db)


@router.get("/get-by-copy-id", response_model=Annotation)
def get_by_copy_id(copy_id: int, db: Session = Depends(get_db)):
    return try_perform(get_annotations_by_copy_id, copy_id, db)


# Any
@router.get("/get-all-for-edition", response_model=Annotation)
def get_all_for_edition(edition_id: int, db: Session = Depends(get_db)):
    return try_perform(get_all_annotations_for_edition, edition_id, db)


# Any
@router.get("/get-all-for-copy", response_model=Annotation)
def get_all_for_copy(copy_id: int, db: Session = Depends(get_db)):
    return try_perform(get_all_annotations_for_copy, copy_id, db)