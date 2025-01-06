from fastapi import APIRouter

from bookRent.BooksCRUD.add.rental_add import create_rental
from bookRent.BooksCRUD.get.rental_get import *
from bookRent.BooksCRUD.tools import try_perform
from bookRent.db_config import get_db
from bookRent.dependiencies import get_current_user, role_required
from bookRent.schematics.rental_schemas import RentalCreate, Rental

router = APIRouter()

# Worker
@router.post("/add")
def add(rental: RentalCreate, user: dict = Depends(get_current_user), role: str = Depends(role_required(['User', 'Worker', 'Admin'])), db: Session = Depends(get_db)):
    usr = db.query(User).filter_by(email=user["username"]).first()
    rental.user_id = usr.id
    return try_perform(create_rental, rental, db=db)


# === GET ===
# === WORKER ===


@router.get("/get-all", response_model=list[Rental] | None)
def get_all(role: str = Depends(role_required(['Worker', 'Admin'])), db: Session = Depends(get_db)):
    return try_perform(get_all_rentals, db=db)


@router.get("/get-by-id", response_model=Rental | None)
def get_by_id(id: int, role: str = Depends(role_required(['Worker', 'Admin'])), db: Session = Depends(get_db)):
    return try_perform(get_rental_by_id, id, db=db)


@router.get("/get-by-user-id", response_model=Rental | list[Rental] | None)
def get_by_user_id(id: int, role: str = Depends(role_required(['Worker', 'Admin'])), db: Session = Depends(get_db)):
    return try_perform(get_rentals_by_user_id, id, db=db)


@router.get("/get-rented-by-user-id", response_model=Rental | list[Rental] | None)
def get_by_user_id(id: int, role: str = Depends(role_required(['Worker', 'Admin'])), db: Session = Depends(get_db)):
    return try_perform(get_rentals_by_user_id_rented, id, db=db)


@router.get("/get-returned-by-user-id", response_model=Rental | list[Rental] | None)
def get_by_user_id(id: int, role: str = Depends(role_required(['Worker', 'Admin'])), db: Session = Depends(get_db)):
    return try_perform(get_rentals_by_user_id_returned, id, db=db)


@router.get("/get-by-copy-id", response_model=Rental | list[Rental] | None)
def get_by_copy_id(id: int, role: str = Depends(role_required(['Worker', 'Admin'])), db: Session = Depends(get_db)):
    return try_perform(get_rentals_by_copy_id, id, db=db)


@router.get("/get-by-rental-date", response_model=Rental | list[Rental] | None)
def get_by_rental_date(rental_date: date, role: str = Depends(role_required(['Worker', 'Admin'])), db: Session = Depends(get_db)):
    return try_perform(get_rentals_by_rental_date, rental_date, db=db)


@router.get("/get-by-due-date", response_model=Rental | list[Rental] | None)
def get_by_due_date(due_date: date, role: str = Depends(role_required(['Worker', 'Admin'])), db: Session = Depends(get_db)):
    return try_perform(get_rentals_by_due_date, due_date, db=db)


@router.get("/get-by-return-date", response_model=Rental | list[Rental] | None)
def get_by_return_date(return_date: date, role: str = Depends(role_required(['Worker', 'Admin'])), db: Session = Depends(get_db)):
    return try_perform(get_rentals_by_return_date, return_date, db=db)


@router.get("/get_past_due", response_model=Rental | list[Rental] | None)
def get_past_due(role: str = Depends(role_required(['Worker', 'Admin'])), db: Session = Depends(get_db)):
    return try_perform(get_rentals_past_due, db=db)


@router.get("/get_not_returned", response_model=Rental | list[Rental] | None)
def get_not_returned(role: str = Depends(role_required(['Worker', 'Admin'])), db: Session = Depends(get_db)):
    return try_perform(get_rentals_not_returned, db=db)

# User
@router.get("/get-my", response_model=Rental | list[Rental] | None)
def get_my(user: dict = Depends(get_current_user), role: str = Depends(role_required(['User', 'Worker', 'Admin'])), db: Session = Depends(get_db)):
    usr = db.query(User).filter_by(email=user["username"]).first()
    return try_perform(get_rentals_by_user_id, usr.id, db=db)

# User
@router.get("/get-my-rented", response_model=Rental | list[Rental] | None)
def get_my(user: dict = Depends(get_current_user), role: str = Depends(role_required(['User', 'Worker', 'Admin'])), db: Session = Depends(get_db)):
    usr = db.query(User).filter_by(email=user["username"]).first()
    return try_perform(get_rentals_by_user_id_rented, usr.id, db=db)

# User
@router.get("/get-my-returned", response_model=Rental | list[Rental] | None)
def get_my(user: dict = Depends(get_current_user), role: str = Depends(role_required(['User', 'Worker', 'Admin'])), db: Session = Depends(get_db)):
    usr = db.query(User).filter_by(email=user["username"]).first()
    return try_perform(get_rentals_by_user_id_returned, usr.id, db=db)
