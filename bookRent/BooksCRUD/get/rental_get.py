from datetime import date

from fastapi import Depends
from sqlalchemy.orm import Session

from bookRent.db_config import get_db
from bookRent.models.models import Rental

# === RENTAL ===

def get_rental_by_id(rent_id: int, db: Session = Depends(get_db())):
    return db.query(Rental).filter_by(id = rent_id).first()

def get_rentals_by_user_id(user_id: int, db: Session = Depends(get_db())):
    return db.query(Rental).filter_by(user_id = user_id).all()

def get_rentals_by_copy_id(copy_id: int, db: Session = Depends(get_db())):
    return db.query(Rental).filter_by(copy_id = copy_id).all()

def get_rentals_by_rental_date(rent_date: date, db: Session = Depends(get_db())):
    return db.query(Rental).filter_by(rental_date = rent_date).all()

def get_rentals_by_due_date(due_date: date, db: Session = Depends(get_db())):
    return db.query(Rental).filter_by(due_date=due_date).all()

def get_rentals_by_return_date(return_date: date, db: Session = Depends(get_db())):
    return db.query(Rental).filter_by(return_date=return_date).all()