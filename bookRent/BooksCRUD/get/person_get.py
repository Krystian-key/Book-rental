from fastapi import Depends
from sqlalchemy import and_
from sqlalchemy.orm import Session

from bookRent.db_config import get_db
from bookRent.models.person_model import Person, models_to_schemas, model_to_schema


# === PERSON ===

def get_all_persons(db: Session = Depends(get_db)):
    persons = db.query(Person).all()
    return models_to_schemas(persons)

def get_person_by_id(person_id: int, db: Session = Depends(get_db())):
    person = db.query(Person).filter_by(id=person_id).first()
    return model_to_schema(person)


def get_persons_by_name(name: str, db: Session = Depends(get_db())):
    persons = db.query(Person).filter(Person.name.ilike(f"%{name}%")).all()
    return models_to_schemas(persons)

def get_persons_by_surname(surname: str, db: Session = Depends(get_db())):
    persons = db.query(Person).filter(Person.surname.ilike(f"%{surname}%")).all()
    return models_to_schemas(persons)

def get_persons_by_full_name(name: str, surname: str, db: Session = Depends(get_db())):
    persons = db.query(Person).filter(and_(Person.name.ilike(f"%{name}%"), Person.surname.ilike(f"%{surname}%"))).all()
    return models_to_schemas(persons)

def get_persons_by_birth_year(birth_year: int, db: Session = Depends(get_db())):
    persons = db.query(Person).filter_by(birth_year=birth_year).all()
    return models_to_schemas(persons)

def get_persons_by_death_year(death_year: int, db: Session = Depends(get_db())):
    persons = db.query(Person).filter_by(death_year=death_year).all()
    return models_to_schemas(persons)