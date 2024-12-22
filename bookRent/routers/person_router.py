from fastapi import APIRouter, HTTPException

from bookRent.BooksCRUD.add.person_add import create_person
from bookRent.BooksCRUD.get.copy_get import *
from bookRent.BooksCRUD.tools import get_results, try_perform
from bookRent.db_config import get_db
from bookRent.schematics.person_schemas import PersonCreate, Person
from bookRent.schematics.search_schemas import PersonSearch

router = APIRouter()

# Worker
@router.post("/add")
def add(person: PersonCreate, db: Session = Depends(get_db)):
    try:
        create_person(person, db)

    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/get-by-id", response_model=Person | None)
def get_by_id(person_id: int, db: Session = Depends(get_db)):
    return try_perform(get_person_by_id, person_id, db)


@router.get("/get-by-name", response_model=Person | list[Person] | None)
def get_by_name(name: str, db: Session = Depends(get_db)):
    return try_perform(get_persons_by_name, name, db)


@router.get("/get-by-surname", response_model=Person | list[Person] | None)
def get_by_surname(surname: str, db: Session = Depends(get_db)):
    return try_perform(get_persons_by_surname, surname, db)


@router.get("/get-by-birth-year", response_model=Person | list[Person] | None)
def get_by_birth_year(birth_year: int, db: Session = Depends(get_db)):
    return try_perform(get_persons_by_birth_year, birth_year, db)


@router.get("/get-by-death-year", response_model=Person | list[Person] | None)
def get_by_death_year(death_year: int, db: Session = Depends(get_db)):
    return try_perform(get_persons_by_death_year, death_year, db)