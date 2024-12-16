from fastapi import APIRouter, HTTPException

from bookRent.BooksCRUD.add.rental_add_old import add_reservation
from bookRent.BooksCRUD.get.reservation_get import *
from bookRent.BooksCRUD.tools import get_results
from bookRent.db_config import get_db
from bookRent.dependiencies import get_current_user
from bookRent.schematics.reservation_schemas import ReservationCreate

router = APIRouter()

# User
@router.post("/add")
async def make_reservation(reservation: ReservationCreate, db: Session = Depends(get_db())):
    try:
        result = add_reservation(
            user_id=reservation.user_id,
            copy_id=reservation.copy_id,
            db=db
        )
        return result

    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


# Worker
@router.get("/get")
def get(cond: dict, db: Session = Depends(get_db())):
    try:
        temp = []

        if cond["res_id"]:
            temp.append(get_reservation_by_id(cond["res_id"], db))
        if cond["user_id"]:
            temp.append(get_reservations_by_user_id(cond["user_id"], db))
        if cond["card_num"]:
            temp.append(get_reservations_by_card_num(cond["user_id"], db))
        if cond["copy_id"]:
            temp.append(get_reservations_by_copy_id(cond["copy_id"], db))
        if cond["res_date"]:
            temp.append(get_reservations_by_date(cond["res_date"], db))
        if cond["res_due"]:
            temp.append(get_reservations_by_due_date(cond["res_due"], db))
        if cond["res_status"]:
            temp.append(get_reservations_by_status(cond["res_status"], db))

        inter = False
        if cond["intersect"]:
            inter = True

        return get_results(temp, inter)

    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


# User
@router.get("/get-my")
def get_my(user: dict = Depends(get_current_user), db: Session = Depends(get_db())):
    return get_reservations_by_user_id(user["id"], db)