from datetime import datetime

from fastapi.params import Depends
from sqlalchemy.orm import Session

from bookRent.BooksCRUD.tools import try_commit
from bookRent.db_config import get_db
from bookRent.models.publisher_model import Publisher
from bookRent.schematics.publisher_schemas import PublisherCreate


def create_publisher(publisher: PublisherCreate, db: Session = Depends(get_db())):
    if publisher.foundation_year > datetime.now().year:
        raise ValueError("Rok założenia wydawnictwa nie może być większy od obecnego roku")

    existing_publisher = db.query(Publisher).filter_by(name=publisher.name).first()
    if existing_publisher:
        raise ValueError(f"Wydawnictwo {publisher.name} już istnieje")

    db_publisher = Publisher(
        name=publisher.name,
        localization=publisher.localization,
        foundation_year=publisher.foundation_year
    )

    db.add(db_publisher)
    return {"message": try_commit(
        db,
        f"Wydawnictwo {db_publisher.name} zostało dodane",
        "Wystąpił błąd podczas dodawania wydawnictwa"
    )}