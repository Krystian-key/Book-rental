from fastapi import Depends
from sqlalchemy.orm import Session

from bookRent.db_config import get_db
from bookRent.models.models import Publisher

# === PUBLISHER ===

def get_publisher_by_id(publisher_id: int, db: Session = Depends(get_db())):
    return db.query(Publisher).filter_by(id=publisher_id).first()

def get_publisher_by_name(name: str, db: Session = Depends(get_db())):
    return db.query(Publisher).filter_by(name=name).first()

def get_publishers_by_city(city: str, db: Session = Depends(get_db())):
    return db.query(Publisher).filter_by(localization=city).all()

def get_publishers_by_foundation_year(year: int, db: Session = Depends(get_db())):
    return db.query(Publisher).filter_by(foundation_year=year).all()