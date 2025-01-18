from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from bookRent.BooksCRUD.add.person_add import create_person
import bookRent.BooksCRUD.get.person_get as pg
from bookRent.BooksCRUD.delete.person_delete import delete_person
from bookRent.BooksCRUD.tools import try_perform
from bookRent.BooksCRUD.update.person_update import update_person
from bookRent.db_config import get_db
from bookRent.dependiencies import role_required
from bookRent.schematics.person_schemas import PersonCreate, Person, PersonUpdate

router = APIRouter()

# Worker
@router.post("/add", status_code=201, response_model=Person | None)
def add(person: PersonCreate, role: str = Depends(role_required(['Worker', 'Admin'])), db: Session = Depends(get_db)):
    return try_perform(create_person, person, db=db)


# === GET ===
# === ANY ===


@router.get("/get-all", response_model=list[Person] | None)
def get_all(db: Session = Depends(get_db)):
    return try_perform(pg.get_all_persons, db=db)


@router.get("/get-by-id", response_model=Person | None)
def get_by_id(id: int, db: Session = Depends(get_db)):
    return try_perform(pg.get_person_by_id, id, db=db)


@router.get("/get-by-name", response_model=Person | list[Person] | None)
def get_by_name(name: str, db: Session = Depends(get_db)):
    return try_perform(pg.get_persons_by_name, name, db=db)


@router.get("/get-by-surname", response_model=Person | list[Person] | None)
def get_by_surname(surname: str, db: Session = Depends(get_db)):
    return try_perform(pg.get_persons_by_surname, surname, db=db)


@router.get("/get-by-birth-year", response_model=Person | list[Person] | None)
def get_by_birth_year(birth: int, db: Session = Depends(get_db)):
    return try_perform(pg.get_persons_by_birth_year, birth, db=db)


@router.get("/get-by-death-year", response_model=Person | list[Person] | None)
def get_by_death_year(death: int, db: Session = Depends(get_db)):
    return try_perform(pg.get_persons_by_death_year, death, db=db)


# === UPDATE ===

# Worker
@router.patch("/update", response_model=Person | None)
def update(person: PersonUpdate, role: str = Depends(role_required(['Worker', 'Admin'])), db: Session = Depends(get_db)):
    return try_perform(update_person, person, db=db)


# === DELETE ===


# Worker
@router.delete("/delete")
def delete(id: int, role: str = Depends(role_required(['Worker', 'Admin'])), db: Session = Depends(get_db)):
    return try_perform(delete_person, id, db=db)