from datetime import timedelta, datetime

from fastapi.params import Depends
from sqlalchemy.orm import Session

from bookRent.BooksCRUD.tools import try_commit
from bookRent.db_config import get_db
from bookRent.models.copy_model import Copy
from bookRent.models.models import User
from bookRent.models.rental_model import Rental
from bookRent.models.reservation_model import Reservation
from bookRent.schematics.rental_schemas import RentalCreate

RENTAL_DAYS = 28


def create_rental(rent: RentalCreate, db: Session = Depends(get_db())):
    user = db.query(User).filter_by(id = rent.user_id).first()
    if not user:
        raise ValueError(f"User with id {rent.user_id} does not exist")

    copy = db.query(Copy).filter_by(id=rent.copy_id).first()
    if not copy:
        raise ValueError(f"Copy with id {rent.copy_id} does not exist")

    if copy.rented:
        raise ValueError(f"Copy with id {rent.copy_id} is rented")

    reservation = (db.query(Reservation).filter_by(copy_id=copy.id)
                    .filter(Reservation.status == "Reserved" or Reservation.status == "Awaiting")
                    .order_by(Reservation.reserved_at).first())
    if reservation :
        if reservation.user_id != user.id:
            raise ValueError(f"Copy with id {rent.copy_id} is reserved for another user")
        # Zmienić status na "Succeeded"

    # Zmienić rented na True

    rental_date = datetime.today()
    due_date = rental_date + timedelta(days=RENTAL_DAYS)

    db_rental = Rental(
        user_id=rent.user_id,
        copy_id=rent.copy_id,
        rental_date=rental_date,
        due_date=due_date
    )
    db.add(db_rental)
    return {"message": try_commit(
        db,
        f"Copy {db_rental.copy_id} has been rented by user {db_rental.user_id}",
        "An error has occurred during rental"
    )}