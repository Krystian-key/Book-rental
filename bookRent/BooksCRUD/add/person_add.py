from fastapi.params import Depends
from sqlalchemy.orm import Session

from bookRent.BooksCRUD.tools import try_commit
from bookRent.db_config import get_db
from bookRent.models.person_model import Person
from bookRent.schematics.person_schemas import PersonCreate


def create_person(person: PersonCreate, db: Session = Depends(get_db())):

    if person.death_year <= person.birth_year:
        raise ValueError("Rok śmierci musi być większy niż rok urodzenia")

    p = Person(
        name=person.name.capitalize(),
        surname=person.surname.capitalize(),
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
        raise ValueError(f"Osoba {p.name} {p.surname} ({p.birth_year}-{p.death_year}) już istnieje")

    db.add(p)
    return {"message": try_commit(
        db,
        f"Dodano osobę {p.name} {p.surname} ({p.birth_year}-{p.death_year}) do bazy",
        "Wystąpił błąd podczas dodawania osoby do bazy"
    )}