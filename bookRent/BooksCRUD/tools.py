from typing import Optional

from fastapi import HTTPException, Depends
from sqlalchemy.dialects.mysql import match
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from bookRent.db_config import get_db


def try_commit(session, mess_fail: str):
    try:
        session.commit()
        return
    except IntegrityError:
        session.rollback()
        raise ValueError(mess_fail)
    except Exception as e:
        session.rollback()
        raise ValueError(mess_fail + f" {e}")


# for gets
def get_result(result, query, intersect: bool, **kwargs):
    if intersect:
        query = query.filter_by(kwargs)
        return
    result.extend(query.filter_by(kwargs).all())


# for routers
def get_results(temp, inter: bool):
    result = []
    if inter:
        result = set()
        for i in temp:
            if not result:
                result.add(i)
            else:
                result = set(result).intersection(i)
            if not result:
                return []
    else:
        for i in temp:
            result.extend(i)

    result = list(set(result))
    return result


def remap_person(cond: dict, from_: str, to: str):
    id: Optional[int] = None
    name: Optional[str] = None
    surname: Optional[str] = None
    birth: Optional[int] = None
    death: Optional[int] = None

    result = dict()

    match from_:
        case "person":
            id = cond["id"]
            name = cond["name"]
            surname = cond["surname"]
            birth = cond["birth"]
            death = cond["death"]
        case "author":
            id = cond["author_id"]
            name = cond["author_name"]
            surname = cond["author_surname"]
            birth = cond["author_birth"]
            death = cond["author_death"]
        case "illustrator":
            id = cond["ill_id"]
            name = cond["ill_name"]
            surname = cond["ill_surname"]
            birth = cond["ill_birth"]
            death = cond["ill_death"]
        case "translator":
            id = cond["tran_id"]
            name = cond["tran_name"]
            surname = cond["tran_surname"]
            birth = cond["tran_birth"]
            death = cond["tran_death"]
        case _:
            raise ValueError(f"Unknown person type \'{from_}\'")

    match to:
        case "person":
            result["id"] = id
            result["name"] = name
            result["surname"] = surname
            result["birth"] = birth
            result["death"] = death
        case "author":
            result["author_id"] = id
            result["author_name"] = name
            result["author_surname"] = surname
            result["author_birth"] = birth
            result["author_death"] = death
        case "illustrator":
            result["ill_id"] = id
            result["ill_name"] = name
            result["ill_surname"] = surname
            result["ill_birth"] = birth
            result["ill_death"] = death
        case "translator":
            result["tran_id"] = id
            result["tran_name"] = name
            result["tran_surname"] = surname
            result["tran_birth"] = birth
            result["tran_death"] = death
        case _:
            raise ValueError(f"Unknown person type \'{to}\'")

    return result


def two_arg_fun(func, arg1, arg2, db: Session = Depends(get_db)):
    return func(arg1, arg2, db)


def one_arg_fun(func, arg, db: Session = Depends(get_db)):
    return func(arg, db)


def no_arg_fun(func, db: Session = Depends(get_db)):
    return func(db)


def try_perform(func, *args, db: Session = Depends(get_db)):
    try:
        size = len(args)
        match size:
            case 0:
                return no_arg_fun(func, db)
            case 1:
                return one_arg_fun(func, args[0], db)
            case 2:
                return two_arg_fun(func, args[0], args[1], db)

    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))

    except HTTPException as he:
        raise he

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))