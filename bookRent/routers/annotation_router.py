from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session

from bookRent.BooksCRUD.add.book_add_old import add_annotation
from bookRent.db_config import get_db
from bookRent.schematics.annotation_schemas import AnnotationCreate

router = APIRouter()

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