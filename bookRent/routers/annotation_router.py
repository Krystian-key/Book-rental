from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session

from bookRent.BooksCRUD.add.book_add_old import add_annotation
from bookRent.BooksCRUD.get.annotation_get import get_annotations_by_copy_id, get_annotation_by_id, \
    get_annotations_by_edition_id, get_annotations_by_book_id, get_all_annotations_for_book, \
    get_all_annotations_for_edition, get_all_annotations_for_copy
from bookRent.BooksCRUD.tools import get_results
from bookRent.db_config import get_db
from bookRent.schematics.annotation_schemas import AnnotationCreate

router = APIRouter()

# Worker
@router.post("/add")
async def add(annotation: AnnotationCreate, db: Session = Depends(get_db())):
    try:
        result = add_annotation(
            book_id=annotation.book_id,
            edition_id=annotation.edition_id,
            copy_id=annotation.copy_id,
            content=annotation.content,
            db=db
        )
        return result

    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


# User
@router.get("/get")
def get(cond: dict, db: Session = Depends(get_db())):
    try:
        temp = []
        if cond["id"]:
            temp.append(get_annotation_by_id(cond["id"], db))
        if cond["copy_id"]:
            temp.append(get_annotations_by_copy_id(cond["copy_id"], db))
        if cond["ed_id"]:
            temp.append(get_annotations_by_edition_id(cond["ed_id"], db))
        if cond["book_id"]:
            temp.append(get_annotations_by_book_id(cond["book_id"], db))

        return get_results(temp, False)

    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


# User
@router.get("/get-all-for-book")
def get_all_for_book(book_id: int, db: Session = Depends(get_db())):
    return get_all_annotations_for_book(book_id, db)


# User
@router.get("/get-all-for-edition")
def get_all_for_edition(edition_id: int, db: Session = Depends(get_db())):
    return get_all_annotations_for_edition(edition_id, db)


# User
@router.get("/get-all-for-copy")
def get_all_for_copy(copy_id: int, db: Session = Depends(get_db())):
    return get_all_annotations_for_copy(copy_id, db)