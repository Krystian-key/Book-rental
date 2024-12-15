from fastapi.params import Depends
from sqlalchemy.orm import Session

from bookRent.BooksCRUD.tools import try_commit
from bookRent.db_config import get_db
from bookRent.models.book_model import Book
from bookRent.models.edition_model import EditionInfo
from bookRent.models.form_model import Form
from bookRent.models.language_model import Language
from bookRent.models.person_model import Person
from bookRent.models.publisher_model import Publisher
from bookRent.schematics.edition_schemas import EditionCreate


def create_edition(edition: EditionCreate, db: Session = Depends(get_db())):
    item = db.query(Book).filter_by(id=edition.book_id).first()
    if item is None:
        raise ValueError(f'Książka o id {edition.book_id} nie istnieje')

    item = db.query(Publisher).filter_by(id=edition.publisher_id).first()
    if item is None:
        raise ValueError(f"Wydawnictwo o id {edition.publisher_id} nie istnieje")

    item = db.query(EditionInfo).filter_by(
        book_id=edition.book_id,
        publisher_id=edition.publisher_id,
        ed_num=edition.ed_num
    ).first()
    if item:
        raise ValueError("To wydanie już istnieje")

    item = db.query(Form).filter_by(id=edition.form_id).first()
    if item is None:
        raise ValueError(f"Forma o id {edition.form_id} nie istnieje")

    if edition.ed_lang_id:
        item = db.query(Language).filter_by(id=edition.ed_lang_id).first()
        if item is None:
            raise ValueError(f"Język o id {edition.ed_lang_id} nie istnieje")

    if edition.illustrator_id:
        item = db.query(Person).filter_by(id=edition.illustrator_id).first()
        if item is None:
            raise ValueError(f"Ilustrator o id {edition.illustrator_id} nie istnieje")

    if edition.translator_id:
        item = db.query(Person).filter_by(id=edition.translator_id).first()
        if item is None:
            raise ValueError(f"Tłumacz o id {edition.translator_id} nie istnieje")

    db_ed = edition.Edition(
        book_id=edition.book_id,
        ed_title=edition.ed_title,
        ed_series=edition.ed_series,
        illustrator_id=edition.illustrator_id,
        translator_id=edition.translator_id,
        ed_lang_id=edition.ed_lang_id,
        publisher_id=edition.publisher_id,
        ed_num=edition.ed_num,
        ed_year=edition.ed_year,
        form_id=edition.form_id,
        isbn=edition.isbn,
        ukd=edition.ukd.upper(),
    )
    db.add(db_ed)
    return {"message": try_commit(
        db,
        f"Wydanie {db_ed.ed_num} książki {db_ed.book_id} od wydawnictwa {db_ed.publisher_id} zostało dodane",
        "Wystąpił błąd podczas dodawania wydania"
    )}






# Nie ma jak rozdzielić entities od kwargs
def check_if_exists(db: Session = Depends(get_db()), *entities, **kwargs):
    item = db.query(entities).filter_by(**kwargs).first()
    if item is None:
        raise ValueError(f"{entities[0]} o podanych kryteriach nie istnieje")