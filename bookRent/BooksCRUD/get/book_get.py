from typing import List

from fastapi import Depends
from sqlalchemy.orm import Session

from bookRent.BooksCRUD.get.language_get import get_language
from bookRent.BooksCRUD.get.person_get import get_persons_by_name, get_persons_by_surname, get_persons_by_full_name, \
    get_persons_by_birth_year, get_persons_by_death_year
from bookRent.db_config import get_db
from bookRent.models import Copy
from bookRent.models.book_category_model import BookCategory
from bookRent.models.book_model import Book, models_to_schemas, model_to_schema
from bookRent.models.edition_model import EditionInfo


# === BOOK ===

def get_all_books(db: Session = Depends(get_db)):
    books = db.query(Book).all()
    return models_to_schemas(books)

def get_book_by_id(book_id: int, db: Session = Depends(get_db())):
    book = db.query(Book).filter_by(id=book_id).first()
    return model_to_schema(book)

def get_book_by_copy_id(copy_id: int, db: Session = Depends(get_db())):
    copy = db.query(Copy).filter_by(id=copy_id).first()
    if copy is None:
        raise ValueError(f"Copy with id {copy_id} does not exist")
    edition = db.query(EditionInfo).filter_by(id=copy.ed_id).first()
    if edition is None:
        raise ValueError(f"Edition with id {copy.ed_id} does not exist")
    book = db.query(Book).filter_by(id=edition.book_id).first()
    return model_to_schema(book)

def get_books_by_title(title: str, db: Session = Depends(get_db())):
    books = db.query(Book).filter(Book.title.ilike(f"%{title}%")).all()
    return models_to_schemas(books)

def get_books_by_series(series: str, db: Session = Depends(get_db())):
    books = db.query(Book).filter(Book.series.ilike(f"%{series}%")).all()
    return models_to_schemas(books)

def get_books_by_language(language: str, db: Session = Depends(get_db())):
    lang = get_language(language, db)
    if lang is None:
        return []
    books = db.query(Book).filter_by(lang_id=lang.id).all()
    return models_to_schemas(books)

def get_books_by_language_id(lang_id: int, db: Session = Depends(get_db())):
    books = db.query(Book).filter_by(lang_id=lang_id).all()
    return models_to_schemas(books)

def get_books_by_authors(authors, db: Session = Depends(get_db())):
    books = []
    for author in authors:
        books.extend(get_books_by_author_id(author.id, db))
    return books

def get_books_by_author_id(author_id: int, db: Session = Depends(get_db())):
    books = db.query(Book).filter_by(author_id=author_id).all()
    return models_to_schemas(books)

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

# ???
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