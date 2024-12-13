from typing import Optional

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from bookRent.BooksCRUD.tools import try_commit
from bookRent.models.models import Person, Publisher, Book, Language, Category, BookCategory, Form, \
    EditionInfo, Copy, Annotation
from bookRent.db_config import DATABASE_URL

def add_person(name: str, surname: str,
               birth_year: Optional[int], death_year: Optional[int], force_add = False):
    db_engine = create_engine(DATABASE_URL)
    Session = sessionmaker(bind=db_engine)

    with Session() as session:
        if not force_add:
            existing_person = session.query(Person).filter_by(
                name=name,
                surname=surname,
                birth_year=birth_year,
                death_year=death_year
            ).first()
            if existing_person:
                raise ValueError("Podana osoba jest już w bazie")

        new_person = Person(
            name=name,
            surname=surname,
            birth_year=birth_year,
            death_year=death_year
        )

        session.add(new_person)
        return {"message": try_commit(
            session,
            f"Osoba {name} {surname} ({birth_year}-{death_year}) została dodana",
            "Wystąpił błąd podczas dodawania osoby"
        )}


def add_publisher(name: str, localization: str, foundation_year: int, force_add = False):
    db_engine = create_engine(DATABASE_URL)
    Session = sessionmaker(bind=db_engine)

    with Session() as session:
        if not force_add:
            existing_publisher = session.query(Publisher).filter_by(name=name).first()
            if existing_publisher:
                raise ValueError("Wydawnictwo o tej nazwie jest już w bazie")

        new_publisher = Publisher(
            name=name,
            localization=localization,
            foundation_year=foundation_year
        )

        session.add(new_publisher)
        return {"message": try_commit(
            session,
            f"Wydawnictwo {name} zostało dodane",
            "Wystąpił błąd podczas dodawania wydawnictwa"
        )}


def add_language(language: str, force_add = False):
    db_engine = create_engine(DATABASE_URL)
    Session = sessionmaker(bind=db_engine)

    with Session() as session:
        if not force_add:
            existing_language = session.query(Language).filter_by(name=language).first()
            if existing_language:
                raise ValueError("Podany język jest już w bazie")

        new_language = Language(lang=language)
        session.add(new_language)
        return {"message":try_commit(
            session,
            f"Dodano język {language} do bazy",
            "Wystąpił błąd podczas dodawania języka"
        )}


def add_form(form: str, force_add = False):
    db_engine = create_engine(DATABASE_URL)
    Session = sessionmaker(bind=db_engine)

    with Session() as session:
        if not force_add:
            existing_form = session.query(Form).filter_by(form=form).first()
            if existing_form:
                raise ValueError("Podana forma jest już w bazie")

        new_form = Form(form=form)
        session.add(new_form)
        return {"message":try_commit(
            session,
            f"Dodano formę {form} do bazy",
            "Wystąpił błąd podczas dodawania formy"
        )}


def add_category(category: str, force_add = False):
    db_engine = create_engine(DATABASE_URL)
    Session = sessionmaker(bind=db_engine)

    with Session() as session:
        if not force_add:
            existing_category = session.query(Category).filter_by(name=category).first()
            if existing_category:
                raise ValueError("Podana kategoria jest już w bazie")

        new_category = Category(category=category)
        session.add(new_category)
        return {"message": try_commit(
            session,
            f"Dodano kategorię {category} do bazy",
            "Wystąpił błąd podczas dodawania kategorii"
        )}


def add_book(original_title: str, original_lang: str, original_series: Optional[str],
             author_name: str, author_surname: str, birth_year: int, death_year: Optional[int],
             *categories, force_add = False):
    db_engine = create_engine(DATABASE_URL)
    Session = sessionmaker(bind=db_engine)

    messages = []

    with Session() as session:
        author = session.query(Person).filter_by(
            name=author_name,
            surname=author_surname,
            birth_year=birth_year
        ).first()
        if not author:
            messages.append(add_person(
                author_name,
                author_surname,
                birth_year,
                death_year,
                True
            )['message'])
            author = session.query(Person).filter_by(
                name=author_name,
                surname=author_surname,
                birth_year=birth_year
            ).first()

        language = session.query(Language).filter_by(name=original_lang).first()
        if not language:
            messages.append(add_language(original_lang, True)['message'])
            language = session.query(Language).filter_by(name=original_lang).first()

        if not force_add:
            existing_book = session.query(Book).filter_by(
                original_title=original_title,
                author_id=author.id
            ).first()
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
        messages.append(try_commit(
            session,
            f"Dodano książkę {original_title} autora {author.name} {author.surname} do bazy",
            "Wystąpił błąd podczas dodawania książki")
        )

        book = session.query(Book).filter_by(original_title=original_title, author_id=author.id).first()
        for category in categories:
            existing_category = session.query(Category).filter_by(category=category).first()
            if not existing_category:
                messages.append(add_category(category, True))
                existing_category = session.query(Category).filter_by(category=category).first()

            book_category = BookCategory(
                book_id=book.id,
                category_id=existing_category.id
            )

            session.add(book_category)
            messages.append(try_commit(
                session,
                f"Przypisano kategorię {category} do książki",
                f"Nie udało się przypisać kategorii {category} do książki"
            ))

    return {"messages": messages}


def add_edition_info(original_title: str, original_lang: str, original_series: Optional[str],
             edition_title: Optional[str], edition_lang: Optional[str], edition_series: Optional[str],
             author_name: str, author_surname: str, birth_year: int, death_year: Optional[int],
             illustrator_name: Optional[str], illustrator_surname: Optional[str],
             translator_name: Optional[str], translator_surname: Optional[str],
             publisher_name: str, edition_number: int, edition_year: int,
             form: str, isbn: int, ukd: str,
             *categories, force_add = False):
    db_engine = create_engine(DATABASE_URL)
    Session = sessionmaker(bind=db_engine)
    messages = []

    with Session() as session:

        if not force_add:
            existing_edition = session.query(EditionInfo).filter_by(isbn=isbn).first()
            if existing_edition:
                messages.append(f"Wydanie {isbn} już jest w bazie")
                return {"messages": messages}

        author = session.query(Person).filter_by(
            name=author_name,
            surname=author_surname,
            birth_year=birth_year
        ).first()
        if not author:
            # Jeśli nie ma autora, to książki też nie ma
            messages.append(
                add_book(
                    original_title,
                    original_lang,
                    original_series,
                    author_name,
                    author_surname,
                    birth_year,
                    death_year,
                    categories
                )['messages'])
            author = session.query(Person).filter_by(
                name=author_name,
                surname=author_surname,
                birth_year=birth_year
            ).first()

        book = session.query(Book).filter_by(original_title=original_title, author_id=author.id).first()
        if not book:
            messages.append(
                add_book(
                    original_title,
                    original_lang,
                    original_series,
                    author_name,
                    author_surname,
                    birth_year,
                    death_year,
                    categories,
                    True
                )['messages'])
            book = session.query(Book).filter_by(
                original_title=original_title,
                author_id=author.id
            ).first()

        illustrator = session.query(Person).filter_by(
            name=illustrator_name,
            surname=illustrator_surname
        ).first()
        if not illustrator:
            messages.append(add_person(illustrator_name, illustrator_surname, force_add=True)['message'])
            illustrator = session.query(Person).filter_by(
                name=illustrator_name,
                surname=illustrator_surname
            ).first()

        translator = session.query(Person).filter_by(
            name=translator_name,
            surname=translator_surname
        ).first()
        if not translator:
            messages.append(add_person(
                translator_name,
                translator_surname,
                force_add=True
            )['message'])
            translator = session.query(Person).filter_by(
                name=translator_name,
                surname=translator_surname
            ).first()

        ed_lang = session.query(Language).filter_by(name=edition_lang).first()
        if not ed_lang:
            messages.append(add_language(edition_lang, True)['message'])
            ed_lang = session.query(Language).filter_by(name=edition_lang).first()

        publisher = session.query(Publisher).filter_by(name=publisher_name).first()
        if not publisher:
            messages.append(add_publisher(publisher_name, True)['message'])
            publisher = session.query(Publisher).filter_by(name=publisher_name).first()

        ed_form = session.query(Form).filter_by(name=form).first()
        if not ed_form:
            messages.append(add_form(form, True)['message'])
            ed_form = session.query(Form).filter_by(name=form).first()

        new_edition = EditionInfo(
            book_id=book.id,
            ed_title=edition_title,
            ed_series=edition_series,
            ed_lang_id=ed_lang.id,
            illustrator_id=illustrator.id,
            translator_id=translator.id,
            publisher_id=publisher.id,
            ed_num=edition_number,
            ed_year=edition_year,
            form_id=ed_form.id,
            isbn=isbn,
            ukd=ukd
        )
        session.add(new_edition)
        messages.append(try_commit(
            session,
            f"Dodano wydanie {isbn} do bazy",
            "Wystąpił błąd podczas dodawania wydania do bazy"
        ))
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
    messages = []

    with Session() as session:
        edition = session.query(EditionInfo).filter_by(isbn=isbn).first()
        if not edition:
            messages.append(
                add_edition_info(original_title, original_lang, original_series,
                                 edition_title, edition_lang, edition_series,
                                 author_name, author_surname, birth_year, death_year,
                                 illustrator_name, illustrator_surname, translator_name,
                                 translator_surname, publisher, edition_number, edition_year,
                                 form, isbn, ukd, *categories, True
            )['messages'])
            edition = session.query(EditionInfo).filter_by(isbn=isbn).first()

        new_copy = Copy(
            ed_id=edition.id,
            rented=False
        )
        session.add(new_copy)
        messages.append(try_commit(
            session,
            f"Dodano nowy egzemplarz wydania {isbn}",
            "Wystąpił błąd podczas dodawania egzemplarza do bazy"
        ))
    return {"messages": messages}


def add_annotation(book_id: Optional[int], edition_id: Optional[int], copy_id: Optional[int],
                   content: str):
    if not(book_id or edition_id or copy_id):
        raise ValueError("Nie podano do czego przypisać adnotację")

    db_engine = create_engine(DATABASE_URL)
    Session = sessionmaker(bind=db_engine)
    word: str
    id: int

    with Session() as session:
        if book_id:
            edition_id = None
            copy_id = None
            word = "książki"
            id = book_id
            book = session.query(Book).filter_by(id=book_id).first()
            if not book:
                raise ValueError(f"Książka o id {book_id} nie istnieje")
        if edition_id:
            copy_id = None
            word = "wydania"
            id = edition_id
            edition = session.query(EditionInfo).filter_by(id=edition_id).first()
            if not edition:
                raise ValueError(f"Wydanie o id {edition_id} nie istnieje")
        if copy_id:
            word = "egzemplarza"
            id = copy_id
            copy = session.query(Copy).filter_by(id=copy_id).first()
            if not copy:
                raise ValueError(f"Egzemplarz o id {copy_id} nie istnieje")

        new_annotation = Annotation(
            book_id=book_id,
            ed_id=edition_id,
            copy_id=copy_id,
            content=content,
        )
        session.add(new_annotation)
        return {"message": try_commit(
            session,
            f"Dodano adnotację do {word} {id}",
            f"Wystąpił błąd podczas dodawania adnotacji"
        )}