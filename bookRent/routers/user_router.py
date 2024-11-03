from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session

from bookRent.db_config import get_db
from bookRent.models.user_model import ReaderCreate
from bookRent.Register_user.user_add import add_user

router = APIRouter()

@router.post("/register")
async def register(user: ReaderCreate):
    try:
        add_user(user)
        return {"message": "użytkownik został dodany pomyślnie"}
    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


