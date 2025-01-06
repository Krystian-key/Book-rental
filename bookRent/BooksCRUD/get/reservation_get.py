from datetime import date
from typing import Type, List

from fastapi import Depends
from sqlalchemy.orm import Session

from bookRent.db_config import get_db
from bookRent.models.models import UserInfo, User
from bookRent.models.reservation_model import Reservation
from bookRent.schematics import reservation_schemas


# === RESERVATION ===

def get_all_reservations(db: Session = Depends(get_db)):
    reservations = db.query(Reservation).all()
    return models_to_schemas(reservations)

def get_reservation_by_id(res_id: int, db: Session = Depends(get_db())):
    reservation = db.query(Reservation).filter_by(id=res_id).first()
    return model_to_schema(reservation)

def get_reservations_by_user_id(user_id: int, db: Session = Depends(get_db())):
    reservations = db.query(Reservation).filter_by(user_id=user_id).all()
    return models_to_schemas(reservations)

def get_reservations_by_card_num(card_num: int, db: Session = Depends(get_db())):
    user_info = db.query(UserInfo).filter_by(card_num = card_num).first()
    if user_info is None:
        raise ValueError(f"User with card number {card_num} does not exist")
    user = db.query(User).filter_by(user_infos_id=user_info.id).first()
    reservations = db.query(Reservation).filter_by(user_id=user.id).all()
    return models_to_schemas(reservations)

def get_reservations_by_copy_id(copy_id: int, db: Session = Depends(get_db())):
    reservations = db.query(Reservation).filter_by(copy_id=copy_id).all()
    return models_to_schemas(reservations)

def get_reservations_by_date(reservation_date: date, db: Session = Depends(get_db())):
    reservations = db.query(Reservation).filter_by(reservation_date=reservation_date).all()
    return models_to_schemas(reservations)

def get_reservations_by_due_date(due_date: date, db: Session = Depends(get_db())):
    reservations = db.query(Reservation).filter_by(reservation_due=due_date).all()
    return models_to_schemas(reservations)

def get_reservations_by_status(status: str, db: Session = Depends(get_db())):
    reservations = db.query(Reservation).filter_by(status=status).all()
    return models_to_schemas(reservations)


def model_to_schema(model: Type[Reservation] | None):
    if model is None:
        return None
        #raise HTTPException(status_code=404, detail="Reservation not found")

    return reservation_schemas.Reservation(
        id=model.id,
        user_id=model.user_id,
        copy_id=model.copy_id,
        reserved_at=model.reserved_at,
        reserved_due=model.reserved_due,
        status=model.status
    )


def models_to_schemas(models: List[Type[Reservation]]):
    schemas = []
    for model in models:
        schema: reservation_schemas.Reservation = model_to_schema(model)
        schemas.append(schema)
    return schemas