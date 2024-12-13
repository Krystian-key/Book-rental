from fastapi import Depends
from sqlalchemy.orm import Session

from bookRent.db_config import get_db
from bookRent.models.models import Person

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