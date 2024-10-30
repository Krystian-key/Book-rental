from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker, Session
from bookRent.models.user_model import ReaderCreate
from bookRent.db_config import DATABASE_URL
import bcrypt


def add_user(user: ReaderCreate):
    db_engine = create_engine(DATABASE_URL)
    Session = sessionmaker(bind=db_engine)

    with Session() as session:
        hashed_pasword = hash_password(user.password)
        query = text("INSERT INTO users (username, password, role) VALUES (:username, :password, 'czytelnik')")

        try:
            session.execute(query, {"username": user.username, "password": hashed_pasword})
            session.commit()
        except Exception as e:
            session.rollback()
            raise e

def hash_password(password: str) -> str:
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password.decode('utf-8')  # Konwertuje na str dla łatwego przechowywania
