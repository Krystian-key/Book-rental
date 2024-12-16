from datetime import datetime, timedelta

from fastapi.params import Depends
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
        raise ValueError(f"Użytkownik o id {res.user_id} nie istnieje")

    copy = db.query(Copy).filter_by(id=res.copy_id).first()
    if not copy:
        raise ValueError(f"Egzemplarz o id {res.copy_id} nie istnieje")

    reservations = db.query(Reservation).filter_by(copy_id=copy.id).filter(
        Reservation.status == "Reserved" or Reservation.status == "Awaiting"
    ).all()

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
        f"Rezerwacja użytkownika {db_res.user_id} na książkę {db_res.copy_id} została złożona",
        "Wystąpił błąd podczas składania rezerwacji"
    )}