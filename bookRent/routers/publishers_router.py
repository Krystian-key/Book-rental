from fastapi import APIRouter, HTTPException

from bookRent.BooksCRUD.book_add import add_publisher
from bookRent.schematics.schematics import PublisherCreate

router = APIRouter()

@router.post("/add")
async def add(publisher: PublisherCreate):
    try:
        result = add_publisher(
            name=publisher.name,
            localization=publisher.localization,
            foundation_year=publisher.foundation_year
        )
        return result

    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))