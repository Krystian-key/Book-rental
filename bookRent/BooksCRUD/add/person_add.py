from fastapi import HTTPException
from fastapi.params import Depends
from sqlalchemy.orm import Session

from bookRent.BooksCRUD.tools import try_commit
from bookRent.db_config import get_db
from bookRent.models.person_model import Person, model_to_schema
from bookRent.schematics.person_schemas import PersonCreate


def create_person(person: PersonCreate, db: Session = Depends(get_db())):

    if person.death_year is not None and person.birth_year is not None and person.death_year <= person.birth_year:
        raise ValueError("Death year must be greater than birth year")

    p = Person(
        name=person.name,
        surname=person.surname,
        birth_year=person.birth_year,
        death_year=person.death_year
    )

    existing_person = db.query(Person).filter(
        Person.name.ilike(p.name),
        Person.surname.ilike(p.surname),
        Person.birth_year==p.birth_year,
        Person.death_year==p.death_year
    ).first()

    if existing_person:
        raise HTTPException(status_code=409, detail=f"Person {p.name} {p.surname} ({p.birth_year}-{p.death_year}) already exists")

    db.add(p)
    try_commit(db, "An error has occurred during person adding")
    return model_to_schema(p)