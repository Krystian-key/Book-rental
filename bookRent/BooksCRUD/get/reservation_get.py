from datetime import date

from fastapi import Depends
from sqlalchemy import and_, or_
from sqlalchemy.orm import Session

from bookRent.db_config import get_db
from bookRent.models.models import UserInfo, User
from bookRent.models.reservation_model import Reservation, models_to_schemas, model_to_schema


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

def get_reservations_by_user_id_reserved(user_id: int, db: Session = Depends(get_db())):
    reservations = db.query(Reservation).filter(
        and_(
            Reservation.user_id==user_id, or_(
                Reservation.status=="Awaiting",
                Reservation.status=="Reserved")
        )
    ).all()
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