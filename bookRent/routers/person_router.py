from fastapi import APIRouter, HTTPException

from bookRent.BooksCRUD.get.copy_get import *
from bookRent.BooksCRUD.tools import get_results
from bookRent.db_config import get_db

router = APIRouter()

# User
@router.get("/get")
def get(cond: dict, db: Session = Depends(get_db())):
    try:
        temp = []
        if cond["id"]:
            temp.append(get_person_by_id(cond["id"], db))
        if cond["name"]:
            temp.append(get_persons_by_name(cond["name"], db))
        if cond["surname"]:
            temp.append(get_persons_by_surname(cond["surname"], db))
        if cond["birth"]:
            temp.append(get_persons_by_birth_year(cond["birth"], db))
        if cond["death"]:
            temp.append(get_persons_by_death_year(cond["death"], db))

        inter = False
        if cond["intersect"]:
            inter = True

        return get_results(temp, inter)

    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))