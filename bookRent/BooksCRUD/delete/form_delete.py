from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session

from bookRent.BooksCRUD.tools import try_commit
from bookRent.db_config import get_db
from bookRent.models.edition_model import EditionInfo
from bookRent.models.form_model import Form


def delete_form(form_id: int, db: Session = Depends(get_db)):
    editions = db.query(EditionInfo).filter_by(form_id=form_id).all()
    if len(editions) > 0:
        print(editions)
        raise HTTPException(status_code=409, detail="Cannot delete form when any edition refers to it")

    db_form = db.query(Form).filter_by(id=form_id).first()
    if db_form is None:
        return True

    db.delete(db_form)
    try_commit(db, "An error has occurred during form deletion")
    return True