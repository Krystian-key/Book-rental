from datetime import datetime

from fastapi import HTTPException
from fastapi.params import Depends
from sqlalchemy.orm import Session

from bookRent.BooksCRUD.tools import try_commit
from bookRent.db_config import get_db
from bookRent.models.publisher_model import Publisher, model_to_schema
from bookRent.schematics.publisher_schemas import PublisherCreate


def create_publisher(publisher: PublisherCreate, db: Session = Depends(get_db())):
    if publisher.foundation_year > datetime.now().year:
        raise ValueError("Foundation year must not be greater than present year")

    existing_publisher = db.query(Publisher).filter(
        Publisher.name.ilike(publisher.name),
        Publisher.localization.ilike(publisher.localization)
    ).first()
    if existing_publisher:
        raise HTTPException(status_code=409, detail=f"Publisher \'{publisher.name}\' from {publisher.localization} already exists")

    db_publisher = Publisher(
        name=publisher.name,
        localization=publisher.localization,
        foundation_year=publisher.foundation_year
    )

    db.add(db_publisher)
    try_commit(db, "An error has occurred during publisher adding")
    return model_to_schema(db_publisher)