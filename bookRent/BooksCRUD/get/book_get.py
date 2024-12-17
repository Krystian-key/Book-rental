from typing import List

from bookRent.BooksCRUD.get.language_get import *
from bookRent.BooksCRUD.get.person_get import *
from bookRent.db_config import get_db
from bookRent.models.book_category_model import BookCategory
from bookRent.models.book_model import Book
from bookRent.schematics.search_schemas import BookSearch


# === BOOK ===

def get_book_by_id(book_id: int, db: Session = Depends(get_db())):
    return db.query(Book).filter_by(id=book_id).first()

def get_books_by_title(title: str, db: Session = Depends(get_db())):
    return db.query(Book).filter_by(title=title).all()

def get_books_by_series(series: str, db: Session = Depends(get_db())):
    return db.query(Book).filter_by(series=series).all()

def get_books_by_language(language: str, db: Session = Depends(get_db())):
    lang = get_language(language.lower(), db)
    if lang is None:
        raise ValueError(f"Language {language.lower()} does not exist")
    return db.query(Book).filter_by(ed_language_id=lang.id).all()

def get_books_by_language_id(lang_id: int, db: Session = Depends(get_db())):
    return db.query(Book).filter_by(ed_language_id=lang_id).all()

def get_books_by_authors(authors, db: Session = Depends(get_db())):
    books = []
    for author in authors:
        books.extend(get_books_by_author_id(author.id, db))
    return books

def get_books_by_author_id(author_id: int, db: Session = Depends(get_db())):
    return db.query(Book).filter_by(author_id=author_id).all()

def get_books_by_author_name(name: str, db: Session = Depends(get_db())):
    authors = get_persons_by_name(name, db)
    return get_books_by_authors(authors, db)

def get_books_by_author_surname(surname: str, db: Session = Depends(get_db())):
    authors = get_persons_by_surname(surname, db)
    return get_books_by_authors(authors, db)

def get_books_by_author_full_name(name: str, surname: str, db: Session = Depends(get_db())):
    authors = get_persons_by_full_name(name, surname, db)
    return get_books_by_authors(authors, db)

def get_books_by_author_birth_year(year: int, db: Session = Depends(get_db())):
    authors = get_persons_by_birth_year(year, db)
    return get_books_by_authors(authors, db)

def get_books_by_author_death_year(year: int, db: Session = Depends(get_db())):
    authors = get_persons_by_death_year(year, db)
    return get_books_by_authors(authors, db)

def get_books_by_category(category: str, db: Session = Depends(get_db())):
    book_categories = db.query(BookCategory).filter_by(category=category).all()
    books = []
    for book_category in book_categories:
        books.append(get_book_by_id(book_category.book_id, db))
    return books

def get_books_by_categories(categories: List[str], db: Session = Depends(get_db())):
    book_categories = []
    for category in categories:
        book_categories.extend(db.query(BookCategory).filter_by(category=category).all())
    book_categories = set(book_categories)

    books = []
    for book_category in book_categories:
        books.append(get_book_by_id(book_category.book_id, db))
    return books


# SearchModel
def get_books(book: BookSearch, db: Session = Depends(get_db())):
    result = []
    query = db.query(Book)
    intersect = book.intersect

    if book.id:
        get_result(result, query, intersect, id=book.id)
    if book.title:
        get_result(result, query, intersect, title=book.title)
    if book.series:
        get_result(result, query, intersect, series=book.series)

    if intersect:
        result = query.all()

    books_by_lang = []
    if book.language:
        langs = get_languages(book.language, db)
        for lang in langs:
            books_by_lang.extend(get_books_by_language_id(lang.id, db))

    books_by_author = []
    if book.author:
        authors = get_persons(book.author, db)
        for author in authors:
            books_by_author.extend(get_books_by_author_id(author.id, db))

    if intersect and result != []:
        result = set(result).intersection(books_by_lang, books_by_author)
        result = list(result)
        return result

    result.extend(books_by_lang)
    result.extend(books_by_author)
    return list(set(result))