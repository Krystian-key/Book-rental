from bookRent.BooksCRUD.get.book_get import *
from bookRent.BooksCRUD.get.form_get import *
from bookRent.BooksCRUD.get.language_get import *
from bookRent.BooksCRUD.get.person_get import *
from bookRent.BooksCRUD.get.publisher_get import *
from bookRent.db_config import get_db
from bookRent.models.edition_model import EditionInfo
from bookRent.schematics.search_schemas import EditionSearch


# === EDITION ===

def get_edition_by_id(edition_id: int, db: Session = Depends(get_db())):
    return db.query(EditionInfo).filter_by(id=edition_id).first()

def get_editions_by_book_id(book_id: int, db: Session = Depends(get_db())):
    return db.query(EditionInfo).filter_by(book_id=book_id).all()

def get_editions_by_books(books, db: Session = Depends(get_db())):
    editions = []
    for book in books:
        editions.extend(get_editions_by_book_id(book.id, db))
    return editions

def get_editions_by_edition_title(title: str, db: Session = Depends(get_db())):
    return db.query(EditionInfo).filter_by(ed_title=title).all()

def get_editions_by_original_title(title: str, db: Session = Depends(get_db())):
    books = get_books_by_title(title)
    return get_editions_by_books(books, db)

def get_editions_by_title(title: str, db: Session = Depends(get_db())):
    editions = get_editions_by_edition_title(title, db)
    editions.extend(get_editions_by_original_title(title, db))
    return editions

def get_editions_by_edition_series(series: str, db: Session = Depends(get_db())):
    return db.query(EditionInfo).filter_by(ed_series=series).all()

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
    return db.query(EditionInfo).filter_by(illustrator_id=ill_id).all()

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
    return db.query(EditionInfo).filter_by(translator_id=tran_id).all()

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
        raise ValueError(f"Language {language.lower()} does not exist")
    return db.query(EditionInfo).filter_by(ed_language_id=lang.id).all()

def get_editions_by_edition_language_id(lang_id: int, db: Session = Depends(get_db())):
    return db.query(EditionInfo).filter_by(ed_language_id=lang_id).all()

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
    return db.query(EditionInfo).filter_by(publisher_id=publisher_id).all()

def get_editions_by_publishers(publishers, db: Session = Depends(get_db())):
    editions = []
    for publisher in publishers:
        editions.extend(get_editions_by_publisher_id(publisher.id, db))
    return editions

def get_editions_by_publisher_name(name: str, db: Session = Depends(get_db())):
    publisher = get_publisher_by_name(name, db)
    if publisher is None:
        raise ValueError(f"Publisher {name} does not exist")
    return db.query(EditionInfo).filter_by(publisher_id=publisher.id).all()

def get_editions_by_publisher_city(city: str, db: Session = Depends(get_db())):
    publishers = get_publishers_by_city(city, db)
    return get_editions_by_publishers(publishers, db)

def get_editions_by_publisher_foundation_year(year: int, db: Session = Depends(get_db())):
    publishers = get_publishers_by_foundation_year(year, db)
    return get_editions_by_publishers(publishers, db)

def get_editions_by_edition_number(num: int, db: Session = Depends(get_db())):
    return db.query(EditionInfo).filter_by(ed_number=num).all()

def get_editions_by_edition_year(year: int, db: Session = Depends(get_db())):
    return db.query(EditionInfo).filter_by(ed_year=year).all()

def get_editions_by_form_id(form_id: int, db: Session = Depends(get_db())):
    return db.query(EditionInfo).filter_by(form_id=form_id).all()

def get_editions_by_form(form: str, db: Session = Depends(get_db())):
    form_ = get_form(form.lower(), db)
    if form_ is None:
        raise ValueError(f"Form {form.lower()} does not exist")
    return db.query(EditionInfo).filter_by(form_id=form_.id).all()

def get_edition_by_isbn(isbn: int, db: Session = Depends(get_db())):
    return db.query(EditionInfo).filter_by(isbn=isbn).first()

def get_edition_by_ukd(ukd: str, db: Session = Depends(get_db())):
    return db.query(EditionInfo).filter_by(ukd=ukd).first()

# SearchModel
def get_editions(edition: EditionSearch, db: Session = Depends(get_db())):
    result = []
    query = db.query(EditionInfo)
    intersect = edition.intersect

    if edition.id:
        get_result(result, query, intersect, id=edition.id)
    if edition.edition_title:
        get_result(result, query, intersect, ed_title=edition.edition_title)
    if edition.edition_series:
        get_result(result, query, intersect, ed_series=edition.edition_series)
    if edition.edition_number:
        get_result(result, query, intersect, ed_num=edition.edition_number)
    if edition.edition_year:
        get_result(result, query, intersect, ed_year=edition.edition_year)
    if edition.isbn:
        get_result(result, query, intersect, isbn=edition.isbn)
    if edition.ukd:
        get_result(result, query, intersect, ukd=edition.ukd)

    if intersect:
        result = query.all()

    editions_by_book = []
    if edition.book:
        books = get_books(edition.book, db)
        for book in books:
            editions_by_book.extend(get_editions_by_book_id(book.id, db))

    editions_by_lang = []
    if edition.edition_language:
        langs = get_languages(edition.edition_language, db)
        for lang in langs:
            editions_by_lang.extend(get_editions_by_edition_language_id(lang.id, db))

    editions_by_form = []
    if edition.form:
        forms = get_forms(edition.form, db)
        for form in forms:
            editions_by_form.extend(get_editions_by_form_id(form.id, db))

    editions_by_publisher = []
    if edition.publisher:
        publishers = get_publishers(edition.publisher, db)
        for publisher in publishers:
            editions_by_publisher.extend(get_editions_by_publisher_id(publisher.id, db))

    editions_by_illustrator = []
    if edition.illustrator:
        illustrators = get_persons(edition.illustrator, db)
        for illustrator in illustrators:
            editions_by_illustrator.extend(get_editions_by_illustrator_id(illustrator.id, db))

    editions_by_translators = []
    if edition.translator:
        translators = get_persons(edition.translator, db)
        for translator in translators:
            editions_by_translators.extend(get_editions_by_translator_id(translator.id, db))

    if intersect and result != []:
        result = set(result).intersection(editions_by_book,
                                          editions_by_lang,
                                          editions_by_form,
                                          editions_by_publisher,
                                          editions_by_illustrator,
                                          editions_by_translators)
        result = list(result)
        return result

    result.extend(editions_by_book)
    result.extend(editions_by_lang)
    result.extend(editions_by_form)
    result.extend(editions_by_publisher)
    result.extend(editions_by_illustrator)
    result.extend(editions_by_translators)
    return list(set(result))