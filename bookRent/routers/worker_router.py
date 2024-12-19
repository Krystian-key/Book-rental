
from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session

from bookRent.db_config import get_db
from bookRent.dependiencies import role_required, get_current_user
from bookRent.utils import get_user_from_token


router = APIRouter()

@router.get("/dashboard")
def get_usr_data(user: dict = Depends(get_current_user), role: str = Depends(role_required(['Worker'])), db: Session = Depends(get_db)):
    user_data = get_user_from_token(user, db)

    return {
        "message": "User data info", "user_data": user_data, "role": role
    }
