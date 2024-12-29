from datetime import date, datetime
from typing import Type, List

from fastapi import Depends
from sqlalchemy.orm import Session

from bookRent.db_config import get_db
from bookRent.models.models import UserInfo, User
from bookRent.models.rental_model import Rental
from bookRent.schematics import rental_schemas


# === RENTAL ===

def get_all_rentals(db: Session = Depends(get_db)):
    rentals = db.query(Rental).all()
    return models_to_schemas(rentals)

def get_rental_by_id(rent_id: int, db: Session = Depends(get_db())):
    rental = db.query(Rental).filter_by(id = rent_id).first()
    return model_to_schema(rental)

def get_rentals_by_user_id(user_id: int, db: Session = Depends(get_db())):
    rentals = db.query(Rental).filter_by(user_id = user_id).all()
    return models_to_schemas(rentals)

def get_rentals_by_card_num(card_num: int, db: Session = Depends(get_db())):
    user_info = db.query(UserInfo).filter_by(card_num = card_num).first()
    user = db.query(User).filter_by(user_infos_id=user_info.id).first()
    rentals = db.query(Rental).filter_by(user_id = user.id).all()
    return models_to_schemas(rentals)

def get_rentals_by_copy_id(copy_id: int, db: Session = Depends(get_db())):
    rentals = db.query(Rental).filter_by(copy_id = copy_id).all()
    return models_to_schemas(rentals)

def get_rentals_by_rental_date(rent_date: date, db: Session = Depends(get_db())):
    rentals = db.query(Rental).filter_by(rental_date = rent_date).all()
    return models_to_schemas(rentals)

def get_rentals_by_due_date(due_date: date, db: Session = Depends(get_db())):
    rentals = db.query(Rental).filter_by(due_date=due_date).all()
    return models_to_schemas(rentals)

def get_rentals_by_return_date(return_date: date, db: Session = Depends(get_db())):
    rentals = db.query(Rental).filter_by(return_date=return_date).all()
    return models_to_schemas(rentals)

def get_rentals_not_returned(db: Session = Depends(get_db())):
    rentals = db.query(Rental).filter_by(return_date=None).all()
    return models_to_schemas(rentals)

def get_rentals_past_due(db: Session = Depends(get_db())):
    rentals = db.query(Rental).filter(Rental.due_date < datetime.today()).filter_by(return_date=None).all()
    return models_to_schemas(rentals)


def model_to_schema(model: Type[Rental] | None):
    if model is None:
        return None
        #raise HTTPException(status_code=404, detail="Rental not found")

    return rental_schemas.Rental(
        id=model.id,
        user_id=model.user_id,
        copy_id=model.copy_id,
        rental_date=model.rental_date,
        due_date=model.due_date,
        return_date=model.return_date
    )


def models_to_schemas(models: List[Type[Rental]]):
    schemas = []
    for model in models:
        schema: rental_schemas.Rental = model_to_schema(model)
        schemas.append(schema)
    return schemas