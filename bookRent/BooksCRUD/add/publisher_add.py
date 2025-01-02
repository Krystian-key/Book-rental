from datetime import datetime

from fastapi.params import Depends
from sqlalchemy.orm import Session

from bookRent.BooksCRUD.tools import try_commit
from bookRent.db_config import get_db
from bookRent.models.publisher_model import Publisher
from bookRent.schematics.publisher_schemas import PublisherCreate


def create_publisher(publisher: PublisherCreate, db: Session = Depends(get_db())):
    if publisher.foundation_year > datetime.now().year:
        raise ValueError("Foundation year must not be greater than present year")

    existing_publisher = db.query(Publisher).filter_by(name=publisher.name).first()
    if existing_publisher:
        raise ValueError(f"Publisher \'{publisher.name}\' already exists")

    db_publisher = Publisher(
        name=publisher.name,
        localization=publisher.localization,
        foundation_year=publisher.foundation_year
    )

    db.add(db_publisher)
    return {"message": try_commit(
        db,
        f"Publisher \'{db_publisher.name}\' has been added",
        "An error has occurred during publisher adding"
    )}