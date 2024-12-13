from datetime import datetime

from sqlalchemy import create_engine
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import sessionmaker
from bookRent.models.models import User, UserInfo
from bookRent.db_config import DATABASE_URL
import bcrypt


def add_user(email: str, password: str, name: str, surname: str, phone: str):
    db_engine = create_engine(DATABASE_URL)
    Session = sessionmaker(bind=db_engine)

    with Session() as session:
        existing_user = session.query(User).filter_by(email=email).first()
        if existing_user:
            raise ValueError("Użytkownik o podanym mailu istnieje")

        hashed_password = hash_password(password)

        last_card = session.query(UserInfo).order_by(UserInfo.card_num.desc()).first()
        last_card_num = int(last_card.card_num) if last_card else 0
        new_card_num = str(last_card_num + 1)

        new_user_info = UserInfo(
            name=name,
            surname=surname,
            phone=phone,
            card_num=new_card_num
        )

        session.add(new_user_info)
        session.commit()


        new_user = User(
            email=email,
            password =hashed_password,
            user_infos_id = new_user_info.id,
            role = 'user',
            created_at = datetime.utcnow()
        )

        session.add(new_user)


        try:
            session.commit()
            return {"message": f"użytkownik {email} został zarejestrowany"}
        except IntegrityError:
            session.rollback()
            raise ValueError("Wystąpił błąd podczas rejestracji")
        except Exception as e:
            session.rollback()
            raise ValueError(f"Wystąpił błąc podczas rejestracji {e}")

    return {"message": f"Użytkownik {email} został pomyślnie zarejestrowany"}










def hash_password(password: str) -> str:
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password.decode('utf-8')  # Konwertuje na str dla łatwego przechowywania
