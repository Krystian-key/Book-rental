from sqlalchemy.exc import IntegrityError

def try_commit(session, mess_success: str, mess_fail: str):
    try:
        session.commit()
        return mess_success
    except IntegrityError:
        session.rollback()
        raise ValueError(mess_fail)
    except Exception as e:
        session.rollback()
        raise ValueError(mess_fail + f" {e}")

def get_result(result, query, intersect: bool, **kwargs):
    if intersect:
        query = query.filter_by(kwargs)
        return
    result.extend(query.filter_by(kwargs).all())