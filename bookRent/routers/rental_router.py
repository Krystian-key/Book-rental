from fastapi import APIRouter

from bookRent.BooksCRUD.add.rental_add import create_rental
from bookRent.BooksCRUD.get.rental_get import *
from bookRent.BooksCRUD.tools import try_perform
from bookRent.db_config import get_db
from bookRent.dependiencies import get_current_user
from bookRent.schematics.rental_schemas import RentalCreate, Rental

router = APIRouter()

# Worker
@router.post("/add")
def add(rental: RentalCreate, db: Session = Depends(get_db)):
    return try_perform(create_rental, rental, db=db)


# === GET ===
# === WORKER ===


@router.get("/get-all", response_model=list[Rental] | None)
def get_all(db: Session = Depends(get_db)):
    return try_perform(get_all_rentals, db=db)


@router.get("/get-by-id", response_model=Rental | None)
def get_by_id(rental_id: int, db: Session = Depends(get_db)):
    return try_perform(get_rental_by_id, rental_id, db=db)


@router.get("/get-by-user-id", response_model=Rental | list[Rental] | None)
def get_by_user_id(user_id: int, db: Session = Depends(get_db)):
    return try_perform(get_rentals_by_user_id, user_id, db=db)


@router.get("/get-by-copy-id", response_model=Rental | list[Rental] | None)
def get_by_copy_id(copy_id: int, db: Session = Depends(get_db)):
    return try_perform(get_rentals_by_copy_id, copy_id, db=db)


@router.get("/get-by-rental-date", response_model=Rental | list[Rental] | None)
def get_by_rental_date(rental_date: date, db: Session = Depends(get_db)):
    return try_perform(get_rentals_by_rental_date, rental_date, db=db)


@router.get("/get-by-due-date", response_model=Rental | list[Rental] | None)
def get_by_due_date(due_date: date, db: Session = Depends(get_db)):
    return try_perform(get_rentals_by_due_date, due_date, db=db)


@router.get("/get-by-return-date", response_model=Rental | list[Rental] | None)
def get_by_return_date(return_date: date, db: Session = Depends(get_db)):
    return try_perform(get_rentals_by_return_date, return_date, db=db)


@router.get("/get_past_due", response_model=Rental | list[Rental] | None)
def get_past_due(db: Session = Depends(get_db)):
    return try_perform(get_rentals_past_due, db=db)


@router.get("/get_not_returned", response_model=Rental | list[Rental] | None)
def get_not_returned(db: Session = Depends(get_db)):
    return try_perform(get_rentals_not_returned, db=db)

# User
@router.get("/get-my", response_model=Rental | list[Rental] | None)
def get_my(user: dict = Depends(get_current_user), db: Session = Depends(get_db)):
    usr = db.query(User).filter_by(email=user["email"]).first()

    return try_perform(get_rentals_by_user_id, usr.id, db=db)
