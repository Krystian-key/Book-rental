from datetime import date

from fastapi import Depends
from sqlalchemy.orm import Session

from bookRent.db_config import get_db
from bookRent.models.models import Reservation

# === RESERVATION ===

def get_reservation_by_id(res_id: int, db: Session = Depends(get_db())):
    return db.query(Reservation).filter_by(id=res_id).first()

def get_reservations_by_user_id(user_id: int, db: Session = Depends(get_db())):
    return db.query(Reservation).filter_by(user_id=user_id).all()

def get_reservations_by_copy_id(copy_id: int, db: Session = Depends(get_db())):
    return db.query(Reservation).filter_by(copy_id=copy_id).all()

def get_reservations_by_date(reservation_date: date, db: Session = Depends(get_db())):
    return db.query(Reservation).filter_by(reservation_date=reservation_date).all()

def get_reservations_by_due_date(due_date: date, db: Session = Depends(get_db())):
    return db.query(Reservation).filter_by(reservation_due=due_date).all()

def get_reservations_by_status(status: str, db: Session = Depends(get_db())):
    return db.query(Reservation).filter_by(status=status).all()