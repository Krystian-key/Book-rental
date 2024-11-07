
from fastapi import Depends, APIRouter

from bookRent.dependiencies import role_required, get_current_user


router = APIRouter()

@router.get("/dashboard")
def get_usr_data(user: dict = Depends(get_current_user), role: str = Depends(role_required(['pracownik']))):
    return {"message": "Jesteś pracownikiem", "user": user['username']}
