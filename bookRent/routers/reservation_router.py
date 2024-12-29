from fastapi import APIRouter

from bookRent.BooksCRUD.add.reservation_add import create_reservation
from bookRent.BooksCRUD.get.reservation_get import *
from bookRent.BooksCRUD.tools import try_perform
from bookRent.db_config import get_db
from bookRent.dependiencies import get_current_user
from bookRent.schematics.reservation_schemas import ReservationCreate, Reservation

router = APIRouter()

# User
@router.post("/add")
def make_reservation(reservation: ReservationCreate, db: Session = Depends(get_db)):
    return try_perform(create_reservation, reservation, db=db)


# === GET ===
# === WORKER ===


@router.get("/get-all", response_model=list[Reservation] | None)
def get_all(db: Session = Depends(get_db)):
    return try_perform(get_all_reservations, db=db)


@router.get("/get-by-id", response_model=Reservation | None)
def get_by_id(reservation_id: int, db: Session = Depends(get_db)):
    return try_perform(get_reservation_by_id, reservation_id, db=db)


@router.get("/get-by-user-id", response_model=Reservation | list[Reservation] | None)
def get_by_user_id(user_id: int, db: Session = Depends(get_db)):
    return try_perform(get_reservations_by_user_id, user_id, db=db)


@router.get("/get-by-copy-id", response_model=Reservation | list[Reservation] | None)
def get_by_copy_id(copy_id: int, db: Session = Depends(get_db)):
    return try_perform(get_reservations_by_copy_id, copy_id, db=db)


@router.get("/get-by-reservation-date", response_model=Reservation | list[Reservation] | None)
def get_by_reservation_date(reservation_date: date, db: Session = Depends(get_db)):
    return try_perform(get_reservations_by_date, reservation_date, db=db)


@router.get("/get-by-due-date", response_model=Reservation | list[Reservation] | None)
def get_by_due_date(due_date: date, db: Session = Depends(get_db)):
    return try_perform(get_reservations_by_due_date, due_date, db=db)


@router.get("/get-by-status", response_model=Reservation | list[Reservation] | None)
def get_by_status(status: str, db: Session = Depends(get_db)):
    return try_perform(get_reservations_by_status, status, db=db)

# User
@router.get("/get-my", response_model=Reservation | list[Reservation] | None)
def get_my(user: dict = Depends(get_current_user), db: Session = Depends(get_db)):
    usr = db.query(User).filter_by(email=user["email"]).first()

    return try_perform(get_reservations_by_user_id, usr.id, db=db)