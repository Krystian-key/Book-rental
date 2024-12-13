from typing import List

from bookRent.BooksCRUD.get.language_get import *
from bookRent.BooksCRUD.get.person_get import *
from bookRent.db_config import get_db
from bookRent.models.models import Book, BookCategory

# === BOOK ===

def get_book_by_id(book_id: int, db: Session = Depends(get_db())):
    return db.query(Book).filter_by(id=book_id).first()

def get_books_by_title(title: str, db: Session = Depends(get_db())):
    return db.query(Book).filter_by(title=title).all()

def get_books_by_series(series: str, db: Session = Depends(get_db())):
    return db.query(Book).filter_by(series=series).all()

def get_books_by_language(language: str, db: Session = Depends(get_db())):
    lang = get_language(language, db)
    if lang is None:
        raise ValueError(f"Język {language} nie istnieje")
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





