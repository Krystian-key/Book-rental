from datetime import date

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from bookRent.BooksCRUD.add.rental_add import create_rental
import bookRent.BooksCRUD.get.rental_get as rg
from bookRent.BooksCRUD.tools import try_perform
from bookRent.BooksCRUD.update.rental_update import return_copy, return_my_copy
from bookRent.db_config import get_db
from bookRent.dependiencies import get_current_user, role_required
from bookRent.models.models import User
from bookRent.schematics.rental_schemas import RentalCreate, Rental

router = APIRouter()

# Worker
@router.post("/add", status_code=201, response_model=Rental | None)
def add(rental: RentalCreate, user: dict = Depends(get_current_user), role: str = Depends(role_required(['User', 'Worker', 'Admin'])), db: Session = Depends(get_db)):
    usr = db.query(User).filter_by(email=user["username"]).first()
    rental.user_id = usr.id
    return try_perform(create_rental, rental, db=db)


# === GET ===
# === WORKER ===


@router.get("/get-all", response_model=list[Rental] | None)
def get_all(role: str = Depends(role_required(['Worker', 'Admin'])), db: Session = Depends(get_db)):
    return try_perform(rg.get_all_rentals, db=db)


@router.get("/get-by-id", response_model=Rental | None)
def get_by_id(id: int, role: str = Depends(role_required(['Worker', 'Admin'])), db: Session = Depends(get_db)):
    return try_perform(rg.get_rental_by_id, id, db=db)


@router.get("/get-by-user-id", response_model=Rental | list[Rental] | None)
def get_by_user_id(id: int, role: str = Depends(role_required(['Worker', 'Admin'])), db: Session = Depends(get_db)):
    return try_perform(rg.get_rentals_by_user_id, id, db=db)


@router.get("/get-rented-by-user-id", response_model=Rental | list[Rental] | None)
def get_by_user_id(id: int, role: str = Depends(role_required(['Worker', 'Admin'])), db: Session = Depends(get_db)):
    return try_perform(rg.get_rentals_by_user_id_rented, id, db=db)


@router.get("/get-returned-by-user-id", response_model=Rental | list[Rental] | None)
def get_by_user_id(id: int, role: str = Depends(role_required(['Worker', 'Admin'])), db: Session = Depends(get_db)):
    return try_perform(rg.get_rentals_by_user_id_returned, id, db=db)


@router.get("/get-by-copy-id", response_model=Rental | list[Rental] | None)
def get_by_copy_id(id: int, role: str = Depends(role_required(['Worker', 'Admin'])), db: Session = Depends(get_db)):
    return try_perform(rg.get_rentals_by_copy_id, id, db=db)


@router.get("/get-by-rental-date", response_model=Rental | list[Rental] | None)
def get_by_rental_date(rental_date: date, role: str = Depends(role_required(['Worker', 'Admin'])), db: Session = Depends(get_db)):
    return try_perform(rg.get_rentals_by_rental_date, rental_date, db=db)


@router.get("/get-by-due-date", response_model=Rental | list[Rental] | None)
def get_by_due_date(due_date: date, role: str = Depends(role_required(['Worker', 'Admin'])), db: Session = Depends(get_db)):
    return try_perform(rg.get_rentals_by_due_date, due_date, db=db)


@router.get("/get-by-return-date", response_model=Rental | list[Rental] | None)
def get_by_return_date(return_date: date, role: str = Depends(role_required(['Worker', 'Admin'])), db: Session = Depends(get_db)):
    return try_perform(rg.get_rentals_by_return_date, return_date, db=db)


@router.get("/get_past_due", response_model=Rental | list[Rental] | None)
def get_past_due(role: str = Depends(role_required(['Worker', 'Admin'])), db: Session = Depends(get_db)):
    return try_perform(rg.get_rentals_past_due, db=db)


@router.get("/get_not_returned", response_model=Rental | list[Rental] | None)
def get_not_returned(role: str = Depends(role_required(['Worker', 'Admin'])), db: Session = Depends(get_db)):
    return try_perform(rg.get_rentals_not_returned, db=db)

# User
@router.get("/get-my", response_model=Rental | list[Rental] | None)
def get_my(user: dict = Depends(get_current_user), role: str = Depends(role_required(['User', 'Worker', 'Admin'])), db: Session = Depends(get_db)):
    usr = db.query(User).filter_by(email=user["username"]).first()
    return try_perform(rg.get_rentals_by_user_id, usr.id, db=db)

# User
@router.get("/get-my-rented", response_model=Rental | list[Rental] | None)
def get_my(user: dict = Depends(get_current_user), role: str = Depends(role_required(['User', 'Worker', 'Admin'])), db: Session = Depends(get_db)):
    usr = db.query(User).filter_by(email=user["username"]).first()
    return try_perform(rg.get_rentals_by_user_id_rented, usr.id, db=db)

# User
@router.get("/get-my-returned", response_model=Rental | list[Rental] | None)
def get_my(user: dict = Depends(get_current_user), role: str = Depends(role_required(['User', 'Worker', 'Admin'])), db: Session = Depends(get_db)):
    usr = db.query(User).filter_by(email=user["username"]).first()
    return try_perform(rg.get_rentals_by_user_id_returned, usr.id, db=db)


# === UPDATE ===


@router.put("/return-my", response_model=Rental | None)
def return_my(id: int, user: dict = Depends(get_current_user), role: str = Depends(role_required(['User', 'Worker', 'Admin'])), db: Session = Depends(get_db)):
    usr = db.query(User).filter_by(email=user["username"]).first()
    return try_perform(return_my_copy, id, usr.id, db=db)


@router.put("/return", response_model=Rental | None)
def return_rental(id: int, role: str = Depends(role_required(['Worker', 'Admin'])), db: Session = Depends(get_db)):
    return try_perform(return_copy, id, db=db)