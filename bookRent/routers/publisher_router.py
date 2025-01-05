from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from bookRent.BooksCRUD.add.publisher_add import create_publisher
from bookRent.BooksCRUD.get.publisher_get import get_publisher_by_id, get_publisher_by_name, get_publishers_by_city, \
    get_publishers_by_foundation_year, get_publishers_by_name, get_all_publishers
from bookRent.BooksCRUD.tools import try_perform
from bookRent.db_config import get_db
from bookRent.dependiencies import role_required
from bookRent.schematics.publisher_schemas import PublisherCreate, Publisher

router = APIRouter()

# Worker
@router.post("/add")
def add(publisher: PublisherCreate, role: str = Depends(role_required(['Worker', 'Admin'])), db: Session = Depends(get_db)):
    return try_perform(create_publisher, publisher, db=db)


# === GET ===
# === ANY ===


@router.get("/get-all", response_model=list[Publisher] | None)
def get_all(db: Session = Depends(get_db)):
    return try_perform(get_all_publishers, db=db)


@router.get("/get-by-id", response_model=Publisher | None)
def get_by_id(id: int, db: Session = Depends(get_db)):
    return try_perform(get_publisher_by_id, id, db=db)


@router.get("/get-by-name-prec", response_model=Publisher | None)
def get_by_name_prec(name: str, db: Session = Depends(get_db)):
    return try_perform(get_publisher_by_name, name, db=db)


@router.get("/get-by-name", response_model=Publisher | list[Publisher] | None)
def get_by_name(name: str, db: Session = Depends(get_db)):
    return try_perform(get_publishers_by_name, name, db=db)


@router.get("/get-by-city", response_model=Publisher | list[Publisher] | None)
def get_by_city(city: str, db: Session = Depends(get_db)):
    return try_perform(get_publishers_by_city, city, db=db)


@router.get("/get-by-foundation-year", response_model=Publisher | list[Publisher] | None)
def get_by_foundation_year(year: str, db: Session = Depends(get_db)):
    return try_perform(get_publishers_by_foundation_year, year, db=db)