from datetime import datetime
from typing import Optional

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from bookRent.models.models import Copy, Reservation, User, Rental
from bookRent.db_config import DATABASE_URL
from bookRent.BooksCRUD.tools import try_commit

def add_reservation(
        user_id: int, copy_id: int, reserved_at: datetime,
        reserved_due: Optional[datetime], status = "Reserved"):
    db_engine = create_engine(DATABASE_URL)
    Session = sessionmaker(bind=db_engine)

    with Session() as session:
        existing_reservation = session.query(Reservation).filter_by(
            user_id=user_id,
            copy_id=copy_id,
            reserved_at=reserved_at
        ).first()
        if existing_reservation:
            raise ValueError(f"Ta rezerwacja już istnieje")

        new_reservation = Reservation(
            user_id=user_id,
            copy_id=copy_id,
            reserved_at=reserved_at,
            reserved_due=reserved_due,
            status=status
        )
        session.add(new_reservation)
        return {"message": try_commit(
            session,
            f"Dodano nową rezerwację",
            "Wystąpił błąd podczas dodawania rezerwacji"
        )}


def add_rental(user_id: int, copy_id: int, rental_date: datetime,
               due_date: datetime, return_date: datetime):
    db_engine = create_engine(DATABASE_URL)
    Session = sessionmaker(bind=db_engine)
    with Session() as session:
        user = session.query(User).filter_by(id=user_id).first()
        if not user:
            raise ValueError(f"Użytkownik o id {user_id} nie istnieje")

        copy = session.query(Copy).filter_by(id=copy_id).first()
        if not copy:
            raise ValueError(f"Egzemplarz o id {copy_id} nie istnieje")

        existing_rental = session.query(Rental).filter_by(
            user_id=user_id,
            copy_id=copy_id,
            rental_date=rental_date
        ).first()
        if existing_rental:
            raise ValueError("Podane wypożyczenie już istnieje")

        new_rental = Rental(
            user_id=user_id,
            copy_id=copy_id,
            rental_date=rental_date,
            due_date=due_date,
            return_date=return_date
        )
        session.add(new_rental)
        return {"message": try_commit(
            session,
            f"Pomyślnie dodano wypożyczenie egzemplarza {copy_id} przez użytkownika {user_id}",
            "Wystąpił błąd podczas dodawania wypożyczenia"
        )}