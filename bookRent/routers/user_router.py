from fastapi import APIRouter, HTTPException, Depends
from bookRent.dependiencies import get_current_user, role_required
from bookRent.schematics.schematics import ReaderCreate
from bookRent.Register_user.user_add import add_user
from bookRent.utils import get_user_from_token
from bookRent.db_config import get_db
from sqlalchemy.orm import Session


router = APIRouter()

@router.post("/register")
async def register(user: ReaderCreate):
    try:
            # Używamy modelu ReaderCreate do przekazania danych do funkcji add_user
        result = add_user(
            email=user.email,
            password=user.password,
            name=user.name,
            surname=user.surname,
            phone=user.phone
            )
        return result
    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/dashboard")
def get_usr_data(user: dict = Depends(get_current_user), role: str = Depends(role_required(['User', 'Admin', 'Worker'])), db: Session = Depends(get_db)):

    user_data = get_user_from_token(user, db)

    return{
        "message": "User data info",
        "user_data": user_data,
        "role": role
    }
