from datetime import datetime

from fastapi import Depends
from sqlalchemy.orm import Session

from bookRent.BooksCRUD.tools import try_commit
from bookRent.BooksCRUD.update.reservation_update import update_reservations_by_copy_id
from bookRent.db_config import get_db
from bookRent.models.copy_model import Copy
from bookRent.models.rental_model import Rental, model_to_schema


def return_copy(rental_id: int, db: Session = Depends(get_db)):
    rental = db.query(Rental).filter(Rental.id == rental_id).first()
    if not rental:
        raise ValueError(f"Rental with id {rental_id} does not exist")

    if rental.return_date is not None:
        raise ValueError(f"Rental with id {rental_id} has already been returned")

    copy = db.query(Copy).filter_by(id=rental.copy_id).first()
    if not copy:
        raise ValueError(f"Copy with id {rental_id} does not exist")

    rental.return_date = datetime.today()
    copy.rented = False

    try_commit(db, "An error has occurred during copy returning")

    update_reservations_by_copy_id(copy.id, db)
    
    return model_to_schema(rental)


def return_my_copy(rental_id: int, user_id: int, db: Session = Depends(get_db)):
    rental = db.query(Rental).filter_by(id=rental_id).first()

    if rental is None:
        raise ValueError(f"Rental with id {id} does not exist")

    if not rental.user_id == user_id:
        raise ValueError("This is not your rental")

    return return_copy(rental_id, db)