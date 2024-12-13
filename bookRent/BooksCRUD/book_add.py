from typing import Optional

from sqlalchemy import create_engine
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import sessionmaker
from bookRent.models.models import User, UserInfo, Person, Publisher, Book, Language, Category, BookCategory
from bookRent.db_config import DATABASE_URL

def add_person(name: str, surname: str, birth_year: Optional[int], death_year: Optional[int]):
    db_engine = create_engine(DATABASE_URL)
    Session = sessionmaker(bind=db_engine)

    with Session() as session:
        existing_person = session.query(Person).filter_by(name=name, surname=surname, birth_year=birth_year, death_year=death_year).first()
        if existing_person:
            raise ValueError("Podana osoba jest już w bazie")

        new_person = Person(
            name=name,
            surname=surname,
            birth_year=birth_year,
            death_year=death_year
        )

        session.add(new_person)
        return {"message":
                try_commit(session,
                           f"Osoba {name} {surname} ({birth_year}-{death_year}) została dodana",
                           "Wystąpił błąd podczas dodawania osoby"
               )}


def add_publisher(name: str, localization: str, foundation_year: int):
    db_engine = create_engine(DATABASE_URL)
    Session = sessionmaker(bind=db_engine)

    with Session() as session:
        existing_publisher = session.query(Publisher).filter_by(name=name).first()
        if existing_publisher:
            raise ValueError("Wydawnictwo o tej nazwie jest już w bazie")

        new_publisher = Publisher(
            name=name,
            localization=localization,
            foundation_year=foundation_year
        )

        session.add(new_publisher)
        return {"message":
                try_commit(session,
                           f"Wydawnictwo {name} zostało dodane",
                           "Wystąpił błąd podczas dodawania wydawnictwa")}


def add_book(original_title: str, original_lang: str, original_series: Optional[str],
             author_name: str, author_surname: str, birth_year: int, death_year: Optional[int],
             *categories):
    db_engine = create_engine(DATABASE_URL)
    Session = sessionmaker(bind=db_engine)

    messages = []

    with Session() as session:
        author = session.query(Person).filter_by(name=author_name, surname=author_surname, birth_year=birth_year).first()
        if not author:
            new_author = Person(
                name=author_name,
                surname=author_surname,
                birth_year=birth_year,
                death_year=death_year
            )
            session.add(new_author)
            session.commit()
            messages.append(f"Dodano nowego autora {author_name} {author_surname} ({birth_year}-{death_year}) do bazy")
            author = session.query(Person).filter_by(name=author_name, surname=author_surname, birth_year=birth_year).first()

        language = session.query(Language).filter_by(name=original_lang).first()
        if not language:
            new_language = Language(lang=original_lang)
            session.add(new_language)
            session.commit()
            messages.append(f"Dodano nowy język {original_lang} do bazy")
            language = session.query(Language).filter_by(name=original_lang).first()

        existing_book = session.query(Book).filter_by(original_title=original_title, author_id=author.id).first()
        if existing_book:
            messages.append(f"Książka {original_title} autora {author.name} {author.surname} już jest w bazie")
            return {"messages": messages}

        new_book = Book(
            title=original_title,
            author_id=author.id,
            series=original_series,
            lang_id=language.id,
        )

        session.add(new_book)
        try:
            session.commit()
            messages.append(f"Dodano książkę {original_title} autora {author.name} {author.surname} do bazy")
        except IntegrityError:
            session.rollback()
            raise ValueError("Wystąpił błąd podczas rejestracji")
        except Exception as e:
            session.rollback()
            raise ValueError(f"Wystąpił błąc podczas rejestracji {e}")

        book = session.query(Book).filter_by(original_title=original_title, author_id=author.id).first()
        for category in categories:
            existing_category = session.query(Category).filter_by(category=category).first()
            if not existing_category:
                new_category = Category(category=category)
                session.add(new_category)
                session.commit()
                messages.append(f"Dodano kategorię {category} do bazy")
                existing_category = session.query(Category).filter_by(category=category).first()

            book_category = BookCategory(
                book_id=book.id,
                category_id=existing_category.id
            )
            session.add(book_category)
            session.commit()
            messages.append(f"Przypisano kategorię {category} do książki")

    return {"messages": messages}


"""
Dodawanie egzemplarza mogłoby wyglądać tak, że można wybrać poszczególne elementy składowe
istniejące już w bazie: książka, autor, ilustrator, tłumacz
Wtedy pola formularza automatycznie by się wypełniały
"""

def add_copy(original_title: str, original_lang: str, original_series: Optional[str],
             edition_title: Optional[str], edition_lang: Optional[str], edition_series: Optional[str],
             author_name: str, author_surname: str, birth_year: int, death_year: Optional[int],
             illustrator_name: Optional[str], illustrator_surname: Optional[str],
             translator_name: Optional[str], translator_surname: Optional[str],
             publisher: str, edition_number: int, edition_year: int,
             form: str, isbn: int, ukd: str,
             *categories
             ):
    db_engine = create_engine(DATABASE_URL)
    Session = sessionmaker(bind=db_engine)

    with Session() as session:
        pass


def try_commit(session, mess_success: str, mess_fail: str):
    try:
        session.commit()
        return mess_success
    except IntegrityError:
        session.rollback()
        return mess_fail
    except Exception as e:
        session.rollback()
        return mess_fail + f" {e}"
