from fastapi import APIRouter, HTTPException

from bookRent.BooksCRUD.add.reservation_add import create_reservation
from bookRent.BooksCRUD.get.reservation_get import *
from bookRent.BooksCRUD.tools import get_results, try_perform
from bookRent.db_config import get_db
from bookRent.dependiencies import get_current_user
from bookRent.schematics.reservation_schemas import ReservationCreate, Reservation
from bookRent.schematics.search_schemas import ReservationSearch

router = APIRouter()

# User
@router.post("/add")
async def make_reservation(reservation: ReservationCreate, db: Session = Depends(get_db)):
    try:
        return create_reservation(reservation, db)

    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


# Worker
@router.get("/get", response_model=Reservation)
def get(reservation: ReservationSearch, db: Session = Depends(get_db)):
    try:
        temp = []

        if reservation.res_id is not None:
            temp.append(get_reservation_by_id(reservation.res_id, db))
        if reservation.user_id is not None:
            temp.append(get_reservations_by_user_id(reservation.user_id, db))
        if reservation.card_num is not None:
            temp.append(get_reservations_by_card_num(reservation.card_num, db))
        if reservation.copy_id is not None:
            temp.append(get_reservations_by_copy_id(reservation.copy_id, db))
        if reservation.res_date is not None:
            temp.append(get_reservations_by_date(reservation.res_date, db))
        if reservation.res_due is not None:
            temp.append(get_reservations_by_due_date(reservation.res_due, db))
        if reservation.res_status is not None:
            temp.append(get_reservations_by_status(reservation.res_status, db))

        inter = False
        if reservation.intersect:
            inter = True

        return get_results(temp, inter)

    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

# Worker
@router.get("/get-by-id", response_model=Reservation | None)
def get_by_id(reservation_id: int, db: Session = Depends(get_db)):
    return try_perform(get_reservation_by_id, reservation_id, db)

# Worker
@router.get("/get-by-user-id", response_model=Reservation | list[Reservation] | None)
def get_by_user_id(user_id: int, db: Session = Depends(get_db)):
    return try_perform(get_reservations_by_user_id, user_id, db)

# Worker
@router.get("/get-by-copy-id", response_model=Reservation | list[Reservation] | None)
def get_by_copy_id(copy_id: int, db: Session = Depends(get_db)):
    return try_perform(get_reservations_by_copy_id, copy_id, db)

# Worker
@router.get("/get-by-reservation-date", response_model=Reservation | list[Reservation] | None)
def get_by_reservation_date(reservation_date: date, db: Session = Depends(get_db)):
    return try_perform(get_reservations_by_date, reservation_date, db)

# Worker
@router.get("/get-by-due-date", response_model=Reservation | list[Reservation] | None)
def get_by_due_date(due_date: date, db: Session = Depends(get_db)):
    return try_perform(get_reservations_by_due_date, due_date, db)

# Worker
@router.get("/get-by-status", response_model=Reservation | list[Reservation] | None)
def get_by_status(status: str, db: Session = Depends(get_db)):
    return try_perform(get_reservations_by_status, status, db)

# User
@router.get("/get-my", response_model=Reservation | list[Reservation] | None)
def get_my(user: dict = Depends(get_current_user), db: Session = Depends(get_db)):
    usr = db.query(User).filter_by(email=user["email"]).first()

    return get_reservations_by_user_id(usr.id, db)