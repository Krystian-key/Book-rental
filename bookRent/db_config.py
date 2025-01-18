from sqlalchemy import create_engine, text, MetaData
import os
from dotenv import load_dotenv
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker


load_dotenv()

DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")


print(f"DB_USER: {DB_USER}")
print(f"DB_PASSWORD: {DB_PASSWORD}")
print(f"DB_HOST: {DB_HOST}")
print(f"DB_PORT: {DB_PORT}")
print(f"DB_NAME: {DB_NAME}")

DATABASE_URL = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"


def initialize_tables():
    db_engine = create_engine(DATABASE_URL)
    with db_engine.connect() as conn:
        with open("bookRent/DB/db-creation.sql", "r") as sql_file:
            sql_commands = sql_file.read()

        commands = sql_commands.split("\n\n")
        for command in commands:
            command = command.strip()

            if command:
                try:
                    conn.execute(text(command))
                    #print(f"Pomyślnie wykonano: {command}")
                except Exception as e:
                    print(f"Błąd podczas wykonywania polecenia: {command} - {e}")

        conn.commit()



engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
metadata = MetaData()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
