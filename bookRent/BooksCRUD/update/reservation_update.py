from datetime import datetime, timedelta

from fastapi import Depends
from sqlalchemy import and_, or_
from sqlalchemy.orm import Session

from bookRent.BooksCRUD.tools import try_commit
from bookRent.constants import RESERVATION_DAYS
from bookRent.db_config import get_db
from bookRent.models.reservation_model import Reservation, models_to_schemas, model_to_schema


def update_reservations_by_copy_id(copy_id: int, db: Session = Depends(get_db)):
    reservations = db.query(Reservation).filter(
        and_(
            Reservation.copy_id == copy_id,
            or_(
                Reservation.status == "Reserved",
                Reservation.status == "Awaiting"
            )
        )
    ).order_by(Reservation.reserved_at).limit(2).all()

    for reservation in reservations:
        if reservation.status == "Awaiting":
            if reservation.reserved_due < datetime.now():
                reservation.status = "PastDue"
                continue
            break

        reservation.status = "Awaiting"
        res_due = datetime.now() + timedelta(days=RESERVATION_DAYS)
        res_due.replace(hour=23, minute=59, second=59)
        reservation.reserved_due = res_due
        break

    try_commit(db, "An error has occurred during reservations updating")
    return models_to_schemas(reservations)


def update_all_reservations(db: Session = Depends(get_db)):
    copy_ids = db.query(Reservation.copy_id).group_by(Reservation.copy_id).all()
    results = []
    for copy_id in copy_ids:
        results.extend(update_reservations_by_copy_id(copy_id, db))

    return results


def cancel_reservation(res_id: int, db: Session = Depends(get_db)):
    reservation = db.query(Reservation).filter(
        Reservation.id == res_id,
        or_(
            Reservation.status == "Reserved",
            Reservation.status == "Awaiting"
        )
    ).first()

    if reservation is None:
        raise ValueError(f"Reservation with id {res_id} does not exist or is not active")

    reservation.status = "Cancelled"
    try_commit(db, "An error has occurred during reservation cancelling")
    results = [model_to_schema(reservation)]
    results.extend(update_reservations_by_copy_id(reservation.copy_id, db))
    return results


def cancel_my_reservation(res_id: int, user_id: int, db: Session = Depends(get_db)):
    res = db.query(Reservation).filter(Reservation.id == res_id).first()

    if not res.user_id == user_id:
        raise ValueError("This is not your reservation")

    return cancel_reservation(res_id, db)


def cancel_reservations_by_copy_id(copy_id: int, db: Session = Depends(get_db)):
    reservations = db.query(Reservation).filter(
        and_(
            Reservation.copy_id == copy_id,
            or_(
                Reservation.status == "Reserved",
                Reservation.status == "Awaiting"
            )
        )
    ).all()

    for reservation in reservations:
        reservation.status = "Cancelled"

    try_commit(db, "An error has occurred during reservations cancelling")
    return models_to_schemas(reservations)


def cancel_reservations_by_user_id(user_id: int, db: Session = Depends(get_db)):
    reservations = db.query(Reservation).filter(
        and_(
            Reservation.user_id == user_id,
            or_(
                Reservation.status == "Reserved",
                Reservation.status == "Awaiting"
            )
        )
    ).all()

    results = []

    for reservation in reservations:
        reservation.status = "Cancelled"
        try_commit(db, "An error has occurred during reservations cancelling")
        results.append(model_to_schema(reservation))
        results.extend(update_reservations_by_copy_id(reservation.copy_id, db))

    return results