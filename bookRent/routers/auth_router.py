from datetime import timedelta

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

import bookRent
from bookRent.auth import ACCESS_TOKEN_EXPIRE_MINUTES, create_access_token
from bookRent.db_config import get_db
from bookRent.models.models import UserLogin
from bookRent.utils import verify_password


router = APIRouter()

@router.post("/login")
def login(user: UserLogin, db: Session = Depends(get_db)):
    db_user = db.query(bookRent.models.user_model.User).filter(bookRent.models.user_model.User.username == user.username).first()
    if not db_user:
        raise HTTPException(status_code=400, detail="Invalid username or password")

    if not verify_password(user.password, db_user.password):
        raise HTTPException(status_code=400, detail="Invalid username or password")

    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": db_user.username, "role": db_user.role.value}, expires_delta=access_token_expires
    )

    return {"access_token": access_token, "token_type": "bearer"}