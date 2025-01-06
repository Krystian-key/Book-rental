from datetime import datetime, timedelta

from fastapi.params import Depends
from sqlalchemy import or_
from sqlalchemy.orm import Session

from bookRent.BooksCRUD.tools import try_commit
from bookRent.db_config import get_db
from bookRent.models.copy_model import Copy
from bookRent.models.models import User
from bookRent.models.reservation_model import Reservation
from bookRent.schematics.reservation_schemas import ReservationCreate

RESERVATION_DAYS = 7

def create_reservation(res: ReservationCreate, db: Session = Depends(get_db())):
    user = db.query(User).filter_by(id=res.user_id).first()
    if not user:
        raise ValueError(f"User with id {res.user_id} does not exist")

    copy = db.query(Copy).filter_by(id=res.copy_id).first()
    if not copy:
        raise ValueError(f"Copy with id {res.copy_id} does not exist")

    reservations = (db.query(Reservation).filter_by(copy_id=copy.id)
                    .filter(or_(Reservation.status == "Reserved",  Reservation.status == "Awaiting"))
                    .all())

    for reservation in reservations:
        if reservation.user_id == res.user_id and reservation.copy_id == res.copy_id:
            raise ValueError(f"User with id {res.user_id} has already reserved this copy")

    status = "Reserved"
    res_date = datetime.now()
    due_date = None
    if not reservations and not copy.rented:
        status = "Awaiting"
        due_date = res_date + timedelta(days=RESERVATION_DAYS)

    db_res = Reservation(
        user_id=res.user_id,
        copy_id=res.copy_id,
        reserved_at=res_date,
        reserved_due=due_date,
        status=status
    )
    db.add(db_res)
    return {"message": try_commit(
        db,
        f"User {db_res.user_id} has reserved the copy {db_res.copy_id}",
        "An error has occurred during reservation adding",
    )}