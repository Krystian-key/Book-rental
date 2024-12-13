from fastapi import APIRouter, HTTPException

from bookRent.BooksCRUD.add.book_add import add_annotation
from bookRent.schematics.schematics import AnnotationCreate

router = APIRouter()

@router.post("/add")
async def add(annotation: AnnotationCreate):
    try:
        result = add_annotation(
            book_id=annotation.book_id,
            edition_id=annotation.edition_id,
            copy_id=annotation.copy_id,
            content=annotation.content
        )
        return result

    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))