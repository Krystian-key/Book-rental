from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session

from bookRent.BooksCRUD.add.book_add import add_publisher
from bookRent.db_config import get_db
from bookRent.schematics.schematics import PublisherCreate

router = APIRouter()

@router.post("/add")
async def add(publisher: PublisherCreate, db: Session = Depends(get_db())):
    try:
        result = add_publisher(
            name=publisher.name,
            localization=publisher.localization,
            foundation_year=publisher.foundation_year,
            db=db
        )
        return result

    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))