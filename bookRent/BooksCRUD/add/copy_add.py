from fastapi.params import Depends
from sqlalchemy.orm import Session

from bookRent.BooksCRUD.tools import try_commit
from bookRent.db_config import get_db
from bookRent.models.copy_model import Copy, model_to_schema
from bookRent.models.edition_model import EditionInfo
from bookRent.schematics.copy_schemas import CopyCreate


def create_copy(copy: CopyCreate, db: Session = Depends(get_db())):
    item = db.query(EditionInfo).filter_by(id=copy.ed_id).first()
    if not item:
        raise ValueError(f"Edition with id {copy.ed_id} does not exist")

    db_copy = Copy(
        ed_id=copy.ed_id,
        rented=False
    )
    db.add(db_copy)
    try_commit(db, "An error has occurred during the copy adding")
    return model_to_schema(db_copy)