from fastapi import Depends
from sqlalchemy.orm import Session

from bookRent.BooksCRUD.tools import get_result
from bookRent.db_config import get_db
from bookRent.models.models import Person
from bookRent.schematics.schematics import PersonSearch


# === PERSON ===

def get_person_by_id(person_id: int, db: Session = Depends(get_db())):
    return db.query(Person).filter_by(id=person_id).first()

def get_persons_by_name(name: str, db: Session = Depends(get_db())):
    return db.query(Person).filter_by(name=name).all()

def get_persons_by_surname(surname: str, db: Session = Depends(get_db())):
    return db.query(Person).filter_by(surname=surname).all()

def get_persons_by_full_name(name: str, surname: str, db: Session = Depends(get_db())):
    return db.query(Person).filter_by(name=name, surname=surname).all()

def get_persons_by_birth_year(birth_year: int, db: Session = Depends(get_db())):
    return db.query(Person).filter_by(birth_year=birth_year).all()

def get_persons_by_death_year(death_year: int, db: Session = Depends(get_db())):
    return db.query(Person).filter_by(death_year=death_year).all()

# SearchModel
def get_persons(person: PersonSearch, db: Session = Depends(get_db())):
    result = []
    query = db.query(Person)
    intersect = person.intersect

    if person.id:
        get_result(result, query, intersect, id=person.id)
    if person.name:
        get_result(result, query, intersect, name=person.name)
    if person.surname:
        get_result(result, query, intersect, surname=person.surname)
    if person.birth_year:
        get_result(result, query, intersect, birth_year=person.birth_year)
    if person.death_year:
        get_result(result, query, intersect, death_year=person.death_year)

    if intersect:
        return query.all()
    return list(set(result))