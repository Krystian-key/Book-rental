from fastapi.params import Depends
from sqlalchemy.orm import Session

from bookRent.BooksCRUD.tools import try_commit
from bookRent.db_config import get_db
from bookRent.models.person_model import Person
from bookRent.schematics.person_schemas import PersonCreate


def create_person(person: PersonCreate, db: Session = Depends(get_db())):

    if person.death_year is not None and person.death_year <= person.birth_year:
        raise ValueError("Death year must be greater than birth year")

    p = Person(
        name=person.name,
        surname=person.surname,
        birth_year=person.birth_year,
        death_year=person.death_year
    )

    existing_person = db.query(Person).filter_by(
        name=p.name,
        surname=p.surname,
        birth_year=p.birth_year,
        death_year=p.death_year
    ).first()

    if existing_person:
        raise ValueError(f"Person {p.name} {p.surname} ({p.birth_year}-{p.death_year}) already exists")

    db.add(p)
    return {"message": try_commit(
        db,
        f"Person {p.name} {p.surname} ({p.birth_year}-{p.death_year}) has been added",
        "An error has occurred during person adding"
    )}