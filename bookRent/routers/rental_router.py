from fastapi import APIRouter, HTTPException

from bookRent.BooksCRUD.add.rental_add import create_rental
from bookRent.BooksCRUD.get.rental_get import *
from bookRent.BooksCRUD.tools import get_results
from bookRent.db_config import get_db
from bookRent.dependiencies import get_current_user
from bookRent.schematics.rental_schemas import RentalCreate

router = APIRouter()

# Worker
@router.post("/add")
async def add(rental: RentalCreate, db: Session = Depends(get_db())):
    try:
        return create_rental(rental, db)

    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

# Worker
@router.get("/get")
def get(cond: dict, db: Session = Depends(get_db())):
    try:
        temp = []

        if cond["rent_id"]:
            temp.append(get_rental_by_id(cond["rent_id"], db))
        if cond["user_id"]:
            temp.append(get_rentals_by_user_id(cond["user_id"], db))
        if cond["card_num"]:
            temp.append(get_rentals_by_card_num(cond["card_num"], db))
        if cond["copy_id"]:
            temp.append(get_rentals_by_copy_id(cond["copy_id"], db))
        if cond["rent_date"]:
            temp.append(get_rentals_by_rental_date(cond["rent_date"], db))
        if cond["rent_due"]:
            temp.append(get_rentals_by_due_date(cond["rent_due"], db))
        if cond["return_date"]:
            temp.append(get_rentals_by_return_date(cond["return_date"], db))

        inter = False
        if cond["intersect"]:
            inter = True

        return get_results(temp, inter)

    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


# Worker
@router.get("/get_past_due")
def get_past_due(db: Session = Depends(get_db())):
    return get_rentals_past_due(db)


# Worker
@router.get("/get_not_returned")
def get_not_returned(db: Session = Depends(get_db())):
    return get_rentals_not_returned(db)


# User
@router.get("/get-my")
def get_my(user: dict = Depends(get_current_user), db: Session = Depends(get_db())):
    return get_rentals_by_user_id(user["id"], db)