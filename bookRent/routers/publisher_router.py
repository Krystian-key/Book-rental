from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session

from bookRent.BooksCRUD.add.book_add_old import add_publisher
from bookRent.BooksCRUD.get.publisher_get import get_publisher_by_id, get_publisher_by_name, get_publishers_by_city, \
    get_publishers_by_foundation_year
from bookRent.BooksCRUD.tools import get_results
from bookRent.db_config import get_db
from bookRent.schematics.publisher_schemas import PublisherCreate

router = APIRouter()

# Worker
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

# User
@router.get("/get")
def get(cond: dict, db: Session = Depends(get_db())):
    try:
        temp = []
        if cond["publ_id"]:
            temp.append(get_publisher_by_id(cond["publ_id"], db))
        if cond["publ_name"]:
            temp.append(get_publisher_by_name(cond["publ_name"], db))
        if cond["publ_city"]:
            temp.append(get_publishers_by_city(cond["publ_city"], db))
        if cond["publ_year"]:
            temp.append(get_publishers_by_foundation_year(cond["publ_year"], db))

        inter = False
        if cond["intersect"]:
            inter = True

        return get_results(temp, inter)

    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))