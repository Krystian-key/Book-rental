from fastapi import APIRouter, HTTPException
from tensorflow.python.ops.inplace_ops import empty

from bookRent.BooksCRUD.add.rental_add import create_rental
from bookRent.BooksCRUD.get.rental_get import *
from bookRent.BooksCRUD.tools import get_results, try_perform
from bookRent.db_config import get_db
from bookRent.dependiencies import get_current_user
from bookRent.schematics.rental_schemas import RentalCreate, Rental
from bookRent.schematics.search_schemas import RentalSearch

router = APIRouter()

# Worker
@router.post("/add")
async def add(rental: RentalCreate, db: Session = Depends(get_db)):
    try:
        return create_rental(rental, db)

    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

# Worker
@router.get("/get", response_model=Rental)
def get(rental: RentalSearch, db: Session = Depends(get_db)):
    try:
        temp = []

        if rental.rent_id is not None:
            temp.append(get_rental_by_id(rental.rent_id, db))
        if rental.user_id is not None:
            temp.append(get_rentals_by_user_id(rental.user_id, db))
        if rental.card_num is not None:
            temp.append(get_rentals_by_card_num(rental.card_num, db))
        if rental.copy_id is not None:
            temp.append(get_rentals_by_copy_id(rental.copy_id, db))
        if rental.rent_date is not None:
            temp.append(get_rentals_by_rental_date(rental.rent_date, db))
        if rental.rent_due is not None:
            temp.append(get_rentals_by_due_date(rental.rent_due, db))
        if rental.return_date is not None:
            temp.append(get_rentals_by_return_date(rental.return_date, db))

        inter = False
        if rental.intersect:
            inter = True

        return get_results(temp, inter)

    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

# Worker
@router.get("/get-by-id", response_model=Rental | None)
def get_by_id(rental_id: int, db: Session = Depends(get_db)):
    return try_perform(get_rental_by_id, rental_id, db)

# Worker
@router.get("/get-by-user-id", response_model=Rental | list[Rental] | None)
def get_by_user_id(user_id: int, db: Session = Depends(get_db)):
    return try_perform(get_rentals_by_user_id, user_id, db)

# Worker
@router.get("/get-by-copy-id", response_model=Rental | list[Rental] | None)
def get_by_copy_id(copy_id: int, db: Session = Depends(get_db)):
    return try_perform(get_rentals_by_copy_id, copy_id, db)

# Worker
@router.get("/get-by-rental-date", response_model=Rental | list[Rental] | None)
def get_by_rental_date(rental_date: date, db: Session = Depends(get_db)):
    return try_perform(get_rentals_by_rental_date, rental_date, db)

# Worker
@router.get("/get-by-due-date", response_model=Rental | list[Rental] | None)
def get_by_due_date(due_date: date, db: Session = Depends(get_db)):
    return try_perform(get_rentals_by_due_date, due_date, db)

# Worker
@router.get("/get-by-return-date", response_model=Rental | list[Rental] | None)
def get_by_return_date(return_date: date, db: Session = Depends(get_db)):
    return try_perform(get_rentals_by_return_date, return_date, db)

# Worker
@router.get("/get_past_due", response_model=Rental | list[Rental] | None)
def get_past_due(db: Session = Depends(get_db)):
    return get_rentals_past_due(db)

# Worker
@router.get("/get_not_returned", response_model=Rental | list[Rental] | None)
def get_not_returned(db: Session = Depends(get_db)):
    return get_rentals_not_returned(db)

# User
@router.get("/get-my", response_model=Rental | list[Rental] | None)
def get_my(user: dict = Depends(get_current_user), db: Session = Depends(get_db)):
    usr = db.query(User).filter_by(email=user["email"]).first()

    return try_perform(get_rentals_by_user_id, usr.id, db)
