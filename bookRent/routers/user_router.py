from fastapi import APIRouter, HTTPException, Depends
from bookRent.dependiencies import get_current_user, role_required
from bookRent.schematics.schematics import ReaderCreate
from bookRent.Register_user.user_add import add_user


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
def get_usr_data(user: dict = Depends(get_current_user), role: str = Depends(role_required(['User']))):
    return {"message": "Jesteś czytelnikiem", "user": user['username'], "role": role}
