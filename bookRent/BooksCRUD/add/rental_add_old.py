from datetime import datetime, timedelta
from typing import Optional

from fastapi.params import Depends
from sqlalchemy.orm import Session
from bookRent.db_config import get_db
from bookRent.BooksCRUD.tools import try_commit
from bookRent.models.copy_model import Copy
from bookRent.models.models import User
from bookRent.models.rental_model import Rental
from bookRent.models.reservation_model import Reservation


def add_reservation(user_id: int, copy_id: int, db: Session = Depends(get_db())):
    check_existence(db, user_id, copy_id)

    existing_reservation = db.query(Reservation).filter(
        Reservation.user_id == user_id,
        Reservation.copy_id == copy_id,
        Reservation.status == "Reserved" or Reservation.status == "Awaiting"
    ).first()
    if existing_reservation:
        raise ValueError(f"Ta rezerwacja już istnieje")

    reserved_at = datetime.now()
    reserved_due: Optional[datetime] = None
    status = "Reserved"

    copy = db.query(Copy).filter_by(id=copy_id).first()
    if not copy.rented:
        first_reservation = db.query(Reservation).filter(
            Reservation.copy_id == copy_id,
            Reservation.status == "Reserved" or Reservation.status == "Awaiting"
        ).first()
        if not first_reservation:
            status = "Awaiting"
            reserved_due = datetime.today() + timedelta(days=1, seconds=-1)

    new_reservation = Reservation(
        user_id=user_id,
        copy_id=copy_id,
        reserved_at=reserved_at,
        reserved_due=reserved_due,
        status=status
    )
    db.add(new_reservation)
    return {"message": try_commit(
        db,
        f"Dodano nową rezerwację",
        "Wystąpił błąd podczas dodawania rezerwacji"
    )}


def add_rental(user_id: int, copy_id: int, db: Session = Depends(get_db())):
    check_existence(db, user_id, copy_id)

    copy = db.query(Copy).filter_by(id=copy_id).first()
    if copy.rented:
        raise ValueError("Podany egzemplarz jest już wypożyczony")

    existing_rental = db.query(Rental).filter_by(
        user_id=user_id,
        copy_id=copy_id,
        return_date=None
    ).first()
    if existing_rental:
        raise ValueError("Podane wypożyczenie już istnieje")

    rental_date = datetime.now()
    due_date = datetime.today() + timedelta(days=1, seconds=-1)

    new_rental = Rental(
        user_id=user_id,
        copy_id=copy_id,
        rental_date=rental_date,
        due_date=due_date,
        return_date=None
    )
    db.add(new_rental)
    return {"message": try_commit(
        db,
        f"Pomyślnie dodano wypożyczenie egzemplarza {copy_id} przez użytkownika {user_id}",
        "Wystąpił błąd podczas dodawania wypożyczenia"
    )}


def check_existence(session, user_id: int, copy_id: int):
    user = session.query(User).filter_by(id=user_id).first()
    if not user:
        raise ValueError(f"Użytkownik o id {user_id} nie istnieje")

    copy = session.query(Copy).filter_by(id=copy_id).first()
    if not copy:
        raise ValueError(f"Egzemplarz o id {copy_id} nie istnieje")

    return True