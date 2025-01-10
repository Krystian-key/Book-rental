from fastapi import Depends
from sqlalchemy.orm import Session

from bookRent.db_config import get_db
from bookRent.models.publisher_model import Publisher, models_to_schemas, model_to_schema


# === PUBLISHER ===

def get_all_publishers(db: Session = Depends(get_db)):
    publishers = db.query(Publisher).all()
    return models_to_schemas(publishers)

def get_publisher_by_id(publisher_id: int, db: Session = Depends(get_db())):
    publisher = db.query(Publisher).filter_by(id=publisher_id).first()
    return model_to_schema(publisher)

def get_publisher_by_name(name: str, db: Session = Depends(get_db())):
    publisher = db.query(Publisher).filter_by(name=name).first()
    return model_to_schema(publisher)

def get_publishers_by_name(name: str, db: Session = Depends(get_db())):
    publishers = db.query(Publisher).filter(Publisher.name.ilike(f"%{name}%")).all()
    return models_to_schemas(publishers)

def get_publishers_by_city(city: str, db: Session = Depends(get_db())):
    publishers = db.query(Publisher).filter(Publisher.localization.ilike(f"%{city}%")).all()
    return models_to_schemas(publishers)

def get_publishers_by_foundation_year(year: int, db: Session = Depends(get_db())):
    publishers = db.query(Publisher).filter_by(foundation_year=year).all()
    return models_to_schemas(publishers)