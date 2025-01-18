from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from bookRent.BooksCRUD.add.publisher_add import create_publisher
import bookRent.BooksCRUD.get.publisher_get as pg
from bookRent.BooksCRUD.delete.publisher_delete import delete_publisher
from bookRent.BooksCRUD.tools import try_perform
from bookRent.BooksCRUD.update.publisher_update import update_publisher
from bookRent.db_config import get_db
from bookRent.dependiencies import role_required
from bookRent.schematics.publisher_schemas import PublisherCreate, Publisher, PublisherUpdate

router = APIRouter()

# Worker
@router.post("/add", status_code=201, response_model=Publisher | None)
def add(publisher: PublisherCreate, role: str = Depends(role_required(['Worker', 'Admin'])), db: Session = Depends(get_db)):
    return try_perform(create_publisher, publisher, db=db)


# === GET ===
# === ANY ===


@router.get("/get-all", response_model=list[Publisher] | None)
def get_all(db: Session = Depends(get_db)):
    return try_perform(pg.get_all_publishers, db=db)


@router.get("/get-by-id", response_model=Publisher | None)
def get_by_id(id: int, db: Session = Depends(get_db)):
    return try_perform(pg.get_publisher_by_id, id, db=db)


@router.get("/get-by-name-prec", response_model=Publisher | None)
def get_by_name_prec(name: str, db: Session = Depends(get_db)):
    return try_perform(pg.get_publisher_by_name, name, db=db)


@router.get("/get-by-name", response_model=Publisher | list[Publisher] | None)
def get_by_name(name: str, db: Session = Depends(get_db)):
    return try_perform(pg.get_publishers_by_name, name, db=db)


@router.get("/get-by-city", response_model=Publisher | list[Publisher] | None)
def get_by_city(city: str, db: Session = Depends(get_db)):
    return try_perform(pg.get_publishers_by_city, city, db=db)


@router.get("/get-by-foundation-year", response_model=Publisher | list[Publisher] | None)
def get_by_foundation_year(year: str, db: Session = Depends(get_db)):
    return try_perform(pg.get_publishers_by_foundation_year, year, db=db)


# === UPDATE ===

# Worker
@router.patch("/update", response_model=Publisher | None)
def update(publisher: PublisherUpdate, role: str = Depends(role_required(['Worker', 'Admin'])), db: Session = Depends(get_db)):
    return try_perform(update_publisher, publisher, db=db)


# === DELETE ===


# Worker
@router.delete("/delete")
def delete(id: int, role: str = Depends(role_required(['Worker', 'Admin'])), db: Session = Depends(get_db)):
    return try_perform(delete_publisher, id, db=db)