from fastapi import HTTPException
from fastapi.params import Depends
from sqlalchemy.orm import Session

from bookRent.BooksCRUD.tools import try_commit
from bookRent.db_config import get_db
from bookRent.models.book_model import Book
from bookRent.models.edition_model import EditionInfo, model_to_schema
from bookRent.models.form_model import Form
from bookRent.models.language_model import Language
from bookRent.models.person_model import Person
from bookRent.models.publisher_model import Publisher
from bookRent.schematics.edition_schemas import EditionCreate


def create_edition(edition: EditionCreate, db: Session = Depends(get_db())):
    item = db.query(Book).filter_by(id=edition.book_id).first()
    if item is None:
        raise ValueError(f'Book with id {edition.book_id} does not exist')

    item = db.query(Publisher).filter_by(id=edition.publisher_id).first()
    if item is None:
        raise ValueError(f"Publisher with id {edition.publisher_id} does not exist")

    item = db.query(EditionInfo).filter_by(
        book_id=edition.book_id,
        publisher_id=edition.publisher_id,
        ed_num=edition.ed_num
    ).first()
    if item:
        raise HTTPException(status_code=409, detail="This edition already exists")

    item = db.query(Form).filter_by(id=edition.form_id).first()
    if item is None:
        raise ValueError(f"Form with id {edition.form_id} does not exist")

    if edition.ed_lang_id:
        item = db.query(Language).filter_by(id=edition.ed_lang_id).first()
        if item is None:
            raise ValueError(f"Language with id {edition.ed_lang_id} does not exist")

    if edition.illustrator_id:
        item = db.query(Person).filter_by(id=edition.illustrator_id).first()
        if item is None:
            raise ValueError(f"Illustrator with id {edition.illustrator_id} does not exist")

    if edition.translator_id:
        item = db.query(Person).filter_by(id=edition.translator_id).first()
        if item is None:
            raise ValueError(f"Translator with id {edition.translator_id} does not exist")

    db_ed = EditionInfo(
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
    try_commit(db, "An error has occurred during edition adding")
    return model_to_schema(db_ed)