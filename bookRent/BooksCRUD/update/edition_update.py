from fastapi import Depends
from sqlalchemy.orm import Session

from bookRent.BooksCRUD.tools import try_commit
from bookRent.db_config import get_db
from bookRent.models.book_model import Book
from bookRent.models.edition_model import EditionInfo, model_to_schema
from bookRent.models.form_model import Form
from bookRent.models.language_model import Language
from bookRent.models.person_model import Person
from bookRent.models.publisher_model import Publisher
from bookRent.schematics.edition_schemas import EditionUpdate


def update_edition(ed: EditionUpdate, db: Session = Depends(get_db)):
    db_edition = db.query(EditionInfo).filter(EditionInfo.id == ed.id).first()
    if db_edition is None:
        raise ValueError(f"Edition with id {ed.id} does not exist")

    if ed.book_id is not None:
        book = db.query(Book).filter(Book.id == ed.book_id).first()
        if book is None:
            raise ValueError(f"Book with id {ed.book_id} does not exist")
        db_edition.book_id = ed.book_id

    if ed.ed_title is not None:
        title = ed.ed_title
        if title == "":
            title = None
        db_edition.ed_title = title

    if ed.ed_series is not None:
        series = ed.ed_series
        if series == "":
            series = None
        db_edition.ed_series = series

    if ed.publisher_id is not None:
        publ = db.query(Publisher).filter(Publisher.id == ed.publisher_id).first()
        if publ is None:
            raise ValueError(f"Publisher with id {ed.publisher_id} does not exist")
        db_edition.publisher_id = ed.publisher_id

    if ed.ed_lang_id is not None:
        lang_id = ed.ed_lang_id
        if lang_id == 0:
            lang_id = None
        else:
            lang = db.query(Language).filter(Language.id == lang_id).first()
            if lang is None:
                raise ValueError(f"Language with id {lang_id} does not exist")
        db_edition.ed_lang_id = lang_id

    if ed.illustrator_id is not None:
        ill_id = ed.illustrator_id
        if ill_id == 0:
            ill_id = None
        else:
            ill = db.query(Person).filter(Person.id == ill_id).first()
            if ill is None:
                raise ValueError(f"Person with id {ill_id} does not exist")
        db_edition.illustrator_id = ill_id

    if ed.translator_id is not None:
        tran_id = ed.translator_id
        if tran_id == 0:
            tran_id = None
        else:
            tran = db.query(Person).filter(Person.id == tran_id).first()
            if tran is None:
                raise ValueError(f"Person with id {tran_id} does not exist")
        db_edition.translator_id = tran_id

    if ed.ed_year is not None:
        db_edition.ed_year = ed.ed_year

    if ed.ed_num is not None:
        db_edition.ed_num = ed.ed_num

    if ed.form_id is not None:
        form = db.query(Form).filter(Form.id == ed.form_id).first()
        if form is None:
            raise ValueError(f"Form with id {ed.form_id} does not exist")
        db_edition.form_id = ed.form_id

    if ed.ukd is not None:
        db_edition.ukd = ed.ukd

    if ed.isbn is not None:
        db_edition.isbn = ed.isbn

    try_commit(db, "An error has occurred during edition update")
    return model_to_schema(db_edition)