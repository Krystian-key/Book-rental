from passlib.context import CryptContext
from sqlalchemy.orm import Session
from bookRent.models.models import User, UserInfo

from fastapi import HTTPException



pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password):
    return pwd_context.hash(password)

def get_user_from_token(user: dict, db: Session):

    try:
        email = user['username']

        db_user = db.query(User).filter(User.email == email).first()

        user_info = db.query(UserInfo).filter(UserInfo.id == db_user.user_infos_id).first()


        return {
            "id": db_user.id,
            "email": db_user.email,
            "name": user_info.name,
            "surname": user_info.surname,
            "phone": user_info.phone,
            "card_number": user_info.card_num
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")



