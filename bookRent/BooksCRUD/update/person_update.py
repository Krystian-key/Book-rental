from fastapi import Depends
from sqlalchemy.orm import Session

from bookRent.BooksCRUD.tools import try_commit
from bookRent.db_config import get_db
from bookRent.models.person_model import Person, model_to_schema
from bookRent.schematics.person_schemas import PersonUpdate


def update_person(person: PersonUpdate, db: Session = Depends(get_db())):
    db_person = db.query(Person).filter(Person.id == person.id).first()
    if db_person is None:
        raise ValueError(f"Person with id {person.id} does not exist")

    if person.name is not None:
        db_person.name = person.name

    if person.surname is not None:
        surname = person.surname
        if surname == "":
            surname = None
        db_person.surname = surname

    if person.birth_year is not None:
        year = person.birth_year
        if year == 0:
            year = None
        db_person.birth_year = year

    if person.death_year is not None:
        year = person.death_year
        if year == 0:
            year = None
        db_person.death_year = year

    try_commit(db, "An error has occurred during peron update")
    return model_to_schema(db_person)