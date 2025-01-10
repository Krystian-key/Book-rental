from fastapi import Depends
from sqlalchemy.orm import Session

from bookRent.BooksCRUD.tools import try_commit
from bookRent.db_config import get_db
from bookRent.models.publisher_model import Publisher, model_to_schema
from bookRent.schematics.publisher_schemas import PublisherUpdate


def update_publisher(publ: PublisherUpdate, db: Session = Depends(get_db)):
    db_publisher = db.query(Publisher).filter(Publisher.id == publ.id).first()
    if db_publisher is None:
        raise ValueError(f"Publisher with id {publ.id} does not exist")

    if publ.name is not None:
        if publ.name == "":
            raise ValueError(f"Publisher name cannot be empty")
        db_publisher.name = publ.name

    if publ.localization is not None:
        db_publisher.localization = publ.localization

    if publ.foundation_year is not None:
        db_publisher.foundation_year = publ.foundation_year

    try_commit(db, "An error has occurred during publisher update")
    return model_to_schema(db_publisher)