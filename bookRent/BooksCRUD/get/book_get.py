from typing import List, Type

from fastapi import HTTPException

from bookRent.BooksCRUD.get.language_get import *
from bookRent.BooksCRUD.get.person_get import *
from bookRent.db_config import get_db
from bookRent.models.book_category_model import BookCategory
from bookRent.models.book_model import Book
from bookRent.schematics import book_schemas


# === BOOK ===

def get_all_books(db: Session = Depends(get_db)):
    books = db.query(Book).all()
    return models_to_schemas(books)

def get_book_by_id(book_id: int, db: Session = Depends(get_db())):
    book = db.query(Book).filter_by(id=book_id).first()
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


def model_to_schema(model: Type[Book] | None):
    if model is None:
        return None
        #raise HTTPException(status_code=404, detail="Book not found")
    series = ""
    if model.series is not None:
        series = model.series
    return book_schemas.Book(
        id=model.id,
        title=model.title,
        series=series,
        lang_id=model.lang_id,
        author_id=model.author_id
    )


def models_to_schemas(models: List[Type[Book]]):
    schemas = []
    for model in models:
        schema: book_schemas.Book = model_to_schema(model)
        schemas.append(schema)
    return schemas