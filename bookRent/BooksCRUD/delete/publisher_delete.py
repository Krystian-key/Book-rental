from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session

from bookRent.BooksCRUD.tools import try_commit
from bookRent.db_config import get_db
from bookRent.models.edition_model import EditionInfo
from bookRent.models.publisher_model import Publisher


def delete_publisher(publisher_id: int, db: Session = Depends(get_db())):
    editions = db.query(EditionInfo).filter_by(publisher_id=publisher_id).all()
    if len(editions) > 0:
        print(editions)
        raise HTTPException(status_code=409, detail="Cannot delete publisher when any edition refers to it")

    db_publisher = db.query(Publisher).filter_by(id=publisher_id).one()
    if db_publisher is None:
        return True

    db.delete(db_publisher)
    try_commit(db, "An error has occurred during publisher deletion")
    return True