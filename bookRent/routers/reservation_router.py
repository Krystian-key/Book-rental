from datetime import date

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from bookRent.BooksCRUD.add.reservation_add import create_reservation
import bookRent.BooksCRUD.get.reservation_get as rg
from bookRent.BooksCRUD.tools import try_perform
from bookRent.BooksCRUD.update.reservation_update import cancel_reservation, cancel_reservations_by_copy_id, \
    cancel_reservations_by_user_id, cancel_my_reservation
from bookRent.db_config import get_db
from bookRent.dependiencies import get_current_user, role_required
from bookRent.models.models import User
from bookRent.schematics.reservation_schemas import ReservationCreate, Reservation

router = APIRouter()

# User
@router.post("/add", status_code=201, response_model=Reservation | None)
def make_reservation(reservation: ReservationCreate, user: dict = Depends(get_current_user), role: str = Depends(role_required(['User', 'Worker', 'Admin'])), db: Session = Depends(get_db)):
    usr = db.query(User).filter_by(email=user["username"]).first()
    reservation.user_id = usr.id
    return try_perform(create_reservation, reservation, db=db)


# === GET ===
# === WORKER ===


@router.get("/get-all", response_model=list[Reservation] | None)
def get_all(role: str = Depends(role_required(['Worker', 'Admin'])), db: Session = Depends(get_db)):
    return try_perform(rg.get_all_reservations, db=db)


@router.get("/get-by-id", response_model=Reservation | None)
def get_by_id(id: int, role: str = Depends(role_required(['Worker', 'Admin'])), db: Session = Depends(get_db)):
    return try_perform(rg.get_reservation_by_id, id, db=db)


@router.get("/get-by-user-id", response_model=Reservation | list[Reservation] | None)
def get_by_user_id(id: int, role: str = Depends(role_required(['Worker', 'Admin'])), db: Session = Depends(get_db)):
    return try_perform(rg.get_reservations_by_user_id, id, db=db)


@router.get("/get-reserved-by-user-id", response_model=Reservation | list[Reservation] | None)
def get_by_user_id(id: int, role: str = Depends(role_required(['Worker', 'Admin'])), db: Session = Depends(get_db)):
    return try_perform(rg.get_reservations_by_user_id_reserved, id, db=db)


@router.get("/get-by-copy-id", response_model=Reservation | list[Reservation] | None)
def get_by_copy_id(id: int, role: str = Depends(role_required(['Worker', 'Admin'])), db: Session = Depends(get_db)):
    return try_perform(rg.get_reservations_by_copy_id, id, db=db)


@router.get("/get-by-reservation-date", response_model=Reservation | list[Reservation] | None)
def get_by_reservation_date(reservation_date: date, role: str = Depends(role_required(['Worker', 'Admin'])), db: Session = Depends(get_db)):
    return try_perform(rg.get_reservations_by_date, reservation_date, db=db)


@router.get("/get-by-due-date", response_model=Reservation | list[Reservation] | None)
def get_by_due_date(due_date: date, role: str = Depends(role_required(['Worker', 'Admin'])), db: Session = Depends(get_db)):
    return try_perform(rg.get_reservations_by_due_date, due_date, db=db)


@router.get("/get-by-status", response_model=Reservation | list[Reservation] | None)
def get_by_status(status: str, role: str = Depends(role_required(['Worker', 'Admin'])), db: Session = Depends(get_db)):
    return try_perform(rg.get_reservations_by_status, status, db=db)

# User
@router.get("/get-my", response_model=Reservation | list[Reservation] | None)
def get_my(user: dict = Depends(get_current_user), role: str = Depends(role_required(['User', 'Worker', 'Admin'])), db: Session = Depends(get_db)):
    usr = db.query(User).filter_by(email=user["username"]).first()
    return try_perform(rg.get_reservations_by_user_id, usr.id, db=db)

# User
@router.get("/get-my-reserved", response_model=Reservation | list[Reservation] | None)
def get_my(user: dict = Depends(get_current_user), role: str = Depends(role_required(['User', 'Worker', 'Admin'])), db: Session = Depends(get_db)):
    usr = db.query(User).filter_by(email=user["username"]).first()
    return try_perform(rg.get_reservations_by_user_id_reserved, usr.id, db=db)


# === UPDATE ===

# User
@router.put("/cancel-my", response_model=list[Reservation] | None)
def cancel_my(id: int, user: dict = Depends(get_current_user), role: str = Depends(role_required(['User', 'Worker', 'Admin'])), db: Session = Depends(get_db)):
    usr = db.query(User).filter_by(email=user["username"]).first()
    return try_perform(cancel_my_reservation, id, usr.id, db=db)

# Worker
@router.put("/cancel", response_model=list[Reservation] | None)
def cancel(id: int, role: str = Depends(role_required(['Worker', 'Admin'])), db: Session = Depends(get_db)):
    return try_perform(cancel_reservation, id, db=db)

# Admin
@router.put("/cancel-by-copy-id", response_model=list[Reservation] | None)
def cancel_by_copy_id(id: int, role: str = Depends(role_required(['Worker', 'Admin'])), db: Session = Depends(get_db)):
    return try_perform(cancel_reservations_by_copy_id, id, db=db)

# Admin
@router.put("/cancel-by-user-id", response_model=list[Reservation] | None)
def cancel_by_user_id(id: int, role: str = Depends(role_required(['Worker', 'Admin'])), db: Session = Depends(get_db)):
    return try_perform(cancel_reservations_by_user_id, id, db=db)