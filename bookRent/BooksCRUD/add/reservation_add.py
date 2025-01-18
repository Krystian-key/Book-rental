from datetime import datetime, timedelta

from fastapi import HTTPException
from fastapi.params import Depends
from sqlalchemy import or_
from sqlalchemy.orm import Session

from bookRent.BooksCRUD.tools import try_commit
from bookRent.constants import RESERVATION_DAYS
from bookRent.db_config import get_db
from bookRent.models.copy_model import Copy
from bookRent.models.models import User
from bookRent.models.rental_model import Rental
from bookRent.models.reservation_model import Reservation, model_to_schema
from bookRent.schematics.reservation_schemas import ReservationCreate

def create_reservation(res: ReservationCreate, db: Session = Depends(get_db())):
    user = db.query(User).filter_by(id=res.user_id).first()
    if not user:
        raise ValueError(f"User with id {res.user_id} does not exist")

    copy = db.query(Copy).filter_by(id=res.copy_id).first()
    if not copy:
        raise ValueError(f"Copy with id {res.copy_id} does not exist")

    if copy.rented:
        rental = db.query(Rental).filter(Rental.copy_id==copy.id).first()
        if rental.user_id == user.id:
            raise HTTPException(status_code=409, detail=f"User with id {user.id} has this copy already rented")

    reservations = (db.query(Reservation).filter_by(copy_id=copy.id)
                    .filter(or_(Reservation.status == "Reserved",  Reservation.status == "Awaiting"))
                    .all())

    for reservation in reservations:
        if reservation.user_id == res.user_id and reservation.copy_id == res.copy_id:
            raise HTTPException(status_code=409, detail=f"User with id {res.user_id} has already reserved this copy")

    status = "Reserved"
    res_date = datetime.now()
    due_date = None
    if not reservations and not copy.rented:
        status = "Awaiting"
        due_date = res_date + timedelta(days=RESERVATION_DAYS)
        due_date.replace(hour=23, minute=59, second=59)

    db_res = Reservation(
        user_id=res.user_id,
        copy_id=res.copy_id,
        reserved_at=res_date,
        reserved_due=due_date,
        status=status
    )
    db.add(db_res)
    try_commit(db, "An error has occurred during reservation adding")
    return model_to_schema(db_res)