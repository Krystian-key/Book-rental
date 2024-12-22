from bookRent.BooksCRUD.get.book_get import *
from bookRent.BooksCRUD.get.form_get import *
from bookRent.BooksCRUD.get.language_get import *
from bookRent.BooksCRUD.get.person_get import *
from bookRent.BooksCRUD.get.publisher_get import *
from bookRent.db_config import get_db
from bookRent.models.edition_model import EditionInfo
from bookRent.schematics import edition_schemas


# === EDITION ===

def get_edition_by_id(edition_id: int, db: Session = Depends(get_db())):
    ed = db.query(EditionInfo).filter_by(id=edition_id).first()
    return model_to_schema(ed)


def get_editions_by_book_id(book_id: int, db: Session = Depends(get_db())):
    eds = db.query(EditionInfo).filter_by(book_id=book_id).all()
    return models_to_schemas(eds)

def get_editions_by_books(books, db: Session = Depends(get_db())):
    editions = []
    for book in books:
        editions.extend(get_editions_by_book_id(book.id, db))
    return editions

def get_editions_by_edition_title(title: str, db: Session = Depends(get_db())):
    eds = db.query(EditionInfo).filter(EditionInfo.ed_title.ilike(f"%{title}%")).all()
    return models_to_schemas(eds)

def get_editions_by_original_title(title: str, db: Session = Depends(get_db())):
    books = get_books_by_title(title)
    return get_editions_by_books(books, db)

def get_editions_by_title(title: str, db: Session = Depends(get_db())):
    editions = get_editions_by_edition_title(title, db)
    editions.extend(get_editions_by_original_title(title, db))
    return editions

def get_editions_by_edition_series(series: str, db: Session = Depends(get_db())):
    eds = db.query(EditionInfo).filter(EditionInfo.ed_series.ilike(f"%{series}%")).all()
    return models_to_schemas(eds)

def get_editions_by_original_series(series: str, db: Session = Depends(get_db())):
    books = get_books_by_series(series, db)
    return get_editions_by_books(books, db)

def get_editions_by_series(series:str, db: Session = Depends(get_db())):
    editions = get_editions_by_edition_series(series, db)
    editions.extend(get_editions_by_original_series(series, db))
    return editions

def get_editions_by_author_id(author_id: int, db: Session = Depends(get_db())):
    books = get_books_by_author_id(author_id, db)
    return get_editions_by_books(books, db)

def get_editions_by_author_name(name: str, db: Session = Depends(get_db())):
    books = get_books_by_author_name(name, db)
    return get_editions_by_books(books, db)

def get_editions_by_author_surname(surname: str, db: Session = Depends(get_db())):
    books = get_books_by_author_surname(surname, db)
    return get_editions_by_books(books, db)

def get_editions_by_author_full_name(name: str, surname: str, db: Session = Depends(get_db())):
    books = get_books_by_author_full_name(name, surname, db)
    return get_editions_by_books(books, db)

def get_editions_by_author_birth_year(year: int, db: Session = Depends(get_db())):
    books = get_books_by_author_birth_year(year, db)
    return get_editions_by_books(books, db)

def get_editions_by_author_death_year(year: int, db: Session = Depends(get_db())):
    books = get_books_by_author_death_year(year, db)
    return get_editions_by_books(books, db)

def get_editions_by_illustrator_id(ill_id: int, db: Session = Depends(get_db())):
    eds = db.query(EditionInfo).filter_by(illustrator_id=ill_id).all()
    return models_to_schemas(eds)

def get_editions_by_illustrators(illustrators, db: Session = Depends(get_db())):
    editions = []
    for illustrator in illustrators:
        editions.extend(get_editions_by_illustrator_id(illustrator.id, db))
    return editions

def get_editions_by_illustrator_name(name: str, db: Session = Depends(get_db())):
    illustrators = get_persons_by_name(name, db)
    return get_editions_by_illustrators(illustrators, db)

def get_editions_by_illustrator_surname(surname: str, db: Session = Depends(get_db())):
    illustrators = get_persons_by_surname(surname, db)
    return get_editions_by_illustrators(illustrators, db)

def get_editions_by_illustrator_full_name(name: str, surname: str, db: Session = Depends(get_db())):
    illustrators = get_persons_by_full_name(name, surname, db)
    return get_editions_by_illustrators(illustrators, db)

def get_editions_by_illustrator_birth_year(year: int, db: Session = Depends(get_db())):
    illustrators = get_persons_by_birth_year(year, db)
    return get_editions_by_illustrators(illustrators, db)

def get_editions_by_illustrator_death_year(year: int, db: Session = Depends(get_db())):
    illustrators = get_persons_by_death_year(year, db)
    return get_editions_by_illustrators(illustrators, db)

def get_editions_by_translator_id(tran_id: int, db: Session = Depends(get_db())):
    eds = db.query(EditionInfo).filter_by(translator_id=tran_id).all()
    return models_to_schemas(eds)

def get_editions_by_translators(translators, db: Session = Depends(get_db())):
    editions = []
    for translator in translators:
        editions.extend(get_editions_by_translator_id(translator.id, db))
    return editions

def get_editions_by_translator_name(name: str, db: Session = Depends(get_db())):
    translators = get_persons_by_name(name, db)
    return get_editions_by_translators(translators, db)

def get_editions_by_translator_surname(surname: str, db: Session = Depends(get_db())):
    translators = get_persons_by_surname(surname, db)
    return get_editions_by_translators(translators, db)

def get_editions_by_translator_full_name(name: str, surname: str, db: Session = Depends(get_db())):
    translators = get_persons_by_full_name(name, surname, db)
    return get_editions_by_translators(translators, db)

def get_editions_by_translator_birth_year(year: int, db: Session = Depends(get_db())):
    translators = get_persons_by_birth_year(year, db)
    return get_editions_by_translators(translators, db)

def get_editions_by_translator_death_year(year: int, db: Session = Depends(get_db())):
    translators = get_persons_by_death_year(year, db)
    return get_editions_by_translators(translators, db)

def get_editions_by_edition_language(language: str, db: Session = Depends(get_db())):
    lang = get_language(language.lower(), db)
    if lang is None:
        return []
        #raise ValueError(f"Language \'{language.lower()}\' does not exist")
    eds = db.query(EditionInfo).filter_by(ed_language_id=lang.id).all()
    return models_to_schemas(eds)

def get_editions_by_edition_language_id(lang_id: int, db: Session = Depends(get_db())):
    eds = db.query(EditionInfo).filter_by(ed_language_id=lang_id).all()
    return models_to_schemas(eds)

def get_editions_by_original_language(language: str, db: Session = Depends(get_db())):
    books = get_books_by_language(language, db)
    return get_editions_by_books(books, db)

def get_editions_by_original_language_id(lang_id: int, db: Session = Depends(get_db())):
    books = get_books_by_language_id(lang_id, db)
    return get_editions_by_books(books, db)

def get_editions_by_language(language: str, db: Session = Depends(get_db())):
    editions = get_editions_by_edition_language(language, db)
    editions.extend(get_editions_by_original_language(language, db))
    return editions

def get_editions_by_language_id(lang_id: int, db: Session = Depends(get_db())):
    editions = get_editions_by_edition_language_id(lang_id, db)
    editions.extend(get_editions_by_original_language_id(lang_id, db))
    return editions

def get_editions_by_publisher_id(publisher_id: int, db: Session = Depends(get_db())):
    eds = db.query(EditionInfo).filter_by(publisher_id=publisher_id).all()
    return models_to_schemas(eds)

def get_editions_by_publishers(publishers, db: Session = Depends(get_db())):
    editions = []
    for publisher in publishers:
        editions.extend(get_editions_by_publisher_id(publisher.id, db))
    return editions

def get_editions_by_publisher_name(name: str, db: Session = Depends(get_db())):
    publisher = get_publisher_by_name(name, db)
    if publisher is None:
        return []
        #raise ValueError(f"Publisher \'{name}\' does not exist")
    eds = db.query(EditionInfo).filter_by(publisher_id=publisher.id).all()
    return models_to_schemas(eds)

def get_editions_by_publisher_city(city: str, db: Session = Depends(get_db())):
    publishers = get_publishers_by_city(city, db)
    return get_editions_by_publishers(publishers, db)

def get_editions_by_publisher_foundation_year(year: int, db: Session = Depends(get_db())):
    publishers = get_publishers_by_foundation_year(year, db)
    return get_editions_by_publishers(publishers, db)

def get_editions_by_edition_number(num: int, db: Session = Depends(get_db())):
    eds = db.query(EditionInfo).filter_by(ed_number=num).all()
    return models_to_schemas(eds)

def get_editions_by_edition_year(year: int, db: Session = Depends(get_db())):
    eds = db.query(EditionInfo).filter_by(ed_year=year).all()
    return models_to_schemas(eds)

def get_editions_by_form_id(form_id: int, db: Session = Depends(get_db())):
    eds = db.query(EditionInfo).filter_by(form_id=form_id).all()
    return models_to_schemas(eds)

def get_editions_by_form(form: str, db: Session = Depends(get_db())):
    form_ = get_form(form.lower(), db)
    if form_ is None:
        return []
        #raise ValueError(f"Form \'{form.lower()}\' does not exist")
    eds = db.query(EditionInfo).filter_by(form_id=form_.id).all()
    return models_to_schemas(eds)

def get_edition_by_isbn(isbn: int, db: Session = Depends(get_db())):
    ed = db.query(EditionInfo).filter_by(isbn=isbn).first()
    return model_to_schema(ed)

def get_editions_by_ukd(ukd: str, db: Session = Depends(get_db())):
    eds = db.query(EditionInfo).filter_by(ukd=ukd).all()
    return models_to_schemas(eds)


def model_to_schema(model: Type[EditionInfo] | None):
    if model is None:
        return None
        #raise HTTPException(status_code=404, detail="Edition not found")

    ed_title = ""
    if model.ed_title is not None:
        ed_title = model.ed_title

    ed_series = ""
    if model.ed_series is not None:
        ed_series = model.ed_series

    return edition_schemas.Edition(
        id=model.id,
        book_id=model.book_id,
        ed_title=ed_title,
        ed_series=ed_series,
        illustrator_id=model.illustrator_id,
        translator_id=model.translator_id,
        ed_lang_id=model.ed_lang_id,
        publisher_id=model.publisher_id,
        ed_num=model.ed_num,
        ed_year=model.ed_year,
        form_id=model.form_id,
        isbn=model.isbn,
        ukd=model.ukd
    )


def models_to_schemas(models: List[Type[EditionInfo]]):
    schemas = []
    for model in models:
        schema: edition_schemas.Edition = model_to_schema(model)
        schemas.append(schema)
    return schemas
