from fastapi import Depends
from sqlalchemy.orm import Session

from bookRent.BooksCRUD.tools import get_result
from bookRent.db_config import get_db
from bookRent.models.models import Publisher
from bookRent.schematics.schematics import PublisherSearch


# === PUBLISHER ===

def get_publisher_by_id(publisher_id: int, db: Session = Depends(get_db())):
    return db.query(Publisher).filter_by(id=publisher_id).first()

def get_publisher_by_name(name: str, db: Session = Depends(get_db())):
    return db.query(Publisher).filter_by(name=name).first()

def get_publishers_by_city(city: str, db: Session = Depends(get_db())):
    return db.query(Publisher).filter_by(localization=city).all()

def get_publishers_by_foundation_year(year: int, db: Session = Depends(get_db())):
    return db.query(Publisher).filter_by(foundation_year=year).all()

# SearchModel
def get_publishers(publisher: PublisherSearch, db: Session = Depends(get_db())):
    result = []
    query = db.query(Publisher)
    intersect = publisher.intersect

    if publisher.id:
        get_result(result, query, intersect, id=publisher.id)
    if publisher.name:
        get_result(result, query, intersect, name=publisher.name)
    if publisher.localization:
        get_result(result, query, intersect, localization=publisher.localization)
    if publisher.foundation_year:
        get_result(result, query, intersect, foundation_year=publisher.foundation_year)

    if intersect:
        return query.all()
    return list(set(result))