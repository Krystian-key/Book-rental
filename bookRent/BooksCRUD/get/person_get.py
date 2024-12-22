from typing import Type, List

from fastapi import Depends
from sqlalchemy.orm import Session

from bookRent.db_config import get_db
from bookRent.models.person_model import Person
from bookRent.schematics import person_schemas


# === PERSON ===

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
    persons = db.query(Person).filter(Person.name.ilike(f"%{name}%") and Person.surname.ilike(f"%{surname}%")).all()
    return models_to_schemas(persons)

def get_persons_by_birth_year(birth_year: int, db: Session = Depends(get_db())):
    persons = db.query(Person).filter_by(birth_year=birth_year).all()
    return models_to_schemas(persons)

def get_persons_by_death_year(death_year: int, db: Session = Depends(get_db())):
    persons = db.query(Person).filter_by(death_year=death_year).all()
    return models_to_schemas(persons)


def model_to_schema(model: Type[Person] | None):
    if model is None:
        return None
        #raise HTTPException(status_code=404, detail="Person not found")

    return person_schemas.Person(
        id=model.id,
        name = model.name,
        surname = model.surname,
        birth_year=model.birth_year,
        death_year=model.death_year
    )


def models_to_schemas(models: List[Type[Person]]):
    schemas = []
    for model in models:
        schema: person_schemas.Person = model_to_schema(model)
        schemas.append(schema)
    return schemas