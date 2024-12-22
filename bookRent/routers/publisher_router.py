from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session

from bookRent.BooksCRUD.add.publisher_add import create_publisher
from bookRent.BooksCRUD.get.publisher_get import get_publisher_by_id, get_publisher_by_name, get_publishers_by_city, \
    get_publishers_by_foundation_year, get_publishers_by_name
from bookRent.BooksCRUD.tools import get_results, try_perform
from bookRent.db_config import get_db
from bookRent.schematics.publisher_schemas import PublisherCreate, Publisher
from bookRent.schematics.search_schemas import PublisherSearch

router = APIRouter()

# Worker
@router.post("/add")
async def add(publisher: PublisherCreate, db: Session = Depends(get_db)):
    try:
        return create_publisher(publisher, db)

    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/get-by-id", response_model=Publisher | None)
def get_by_id(publ_id: int, db: Session = Depends(get_db)):
    return try_perform(get_publisher_by_id, publ_id, db)


@router.get("/get-by-name-prec", response_model=Publisher | None)
def get_by_name_prec(name: str, db: Session = Depends(get_db)):
    return try_perform(get_publisher_by_name, name, db)


@router.get("/get-by-name", response_model=Publisher | list[Publisher] | None)
def get_by_name(name: str, db: Session = Depends(get_db)):
    return try_perform(get_publishers_by_name, name, db)


@router.get("/get-by-city", response_model=Publisher | list[Publisher] | None)
def get_by_city(city: str, db: Session = Depends(get_db)):
    return try_perform(get_publishers_by_city, city, db)


@router.get("/get-by-foundation-year", response_model=Publisher | list[Publisher] | None)
def get_by_foundation_year(year: str, db: Session = Depends(get_db)):
    return try_perform(get_publishers_by_foundation_year, year, db)