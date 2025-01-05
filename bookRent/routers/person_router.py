from fastapi import APIRouter

from bookRent.BooksCRUD.add.person_add import create_person
from bookRent.BooksCRUD.get.copy_get import *
from bookRent.BooksCRUD.tools import try_perform
from bookRent.db_config import get_db
from bookRent.dependiencies import role_required
from bookRent.schematics.person_schemas import PersonCreate, Person

router = APIRouter()

# Worker
@router.post("/add")
def add(person: PersonCreate, role: str = Depends(role_required(['Worker', 'Admin'])), db: Session = Depends(get_db)):
    return try_perform(create_person, person, db=db)


# === GET ===
# === ANY ===


@router.get("/get-all", response_model=list[Person] | None)
def get_all(db: Session = Depends(get_db)):
    return try_perform(get_all_persons, db=db)


@router.get("/get-by-id", response_model=Person | None)
def get_by_id(person_id: int, db: Session = Depends(get_db)):
    return try_perform(get_person_by_id, person_id, db=db)


@router.get("/get-by-name", response_model=Person | list[Person] | None)
def get_by_name(name: str, db: Session = Depends(get_db)):
    return try_perform(get_persons_by_name, name, db=db)


@router.get("/get-by-surname", response_model=Person | list[Person] | None)
def get_by_surname(surname: str, db: Session = Depends(get_db)):
    return try_perform(get_persons_by_surname, surname, db=db)


@router.get("/get-by-birth-year", response_model=Person | list[Person] | None)
def get_by_birth_year(birth_year: int, db: Session = Depends(get_db)):
    return try_perform(get_persons_by_birth_year, birth_year, db=db)


@router.get("/get-by-death-year", response_model=Person | list[Person] | None)
def get_by_death_year(death_year: int, db: Session = Depends(get_db)):
    return try_perform(get_persons_by_death_year, death_year, db=db)