from bookRent.BooksCRUD.get.edition_get import *
from bookRent.db_config import get_db
from bookRent.models.copy_model import Copy
from bookRent.schematics import copy_schemas


# === COPY ===

def get_all_copies(db: Session = Depends(get_db)):
    copies = db.query(Copy).all()
    return models_to_schemas(copies)

def get_copy_by_id(copy_id: int, db: Session = Depends(get_db())):
    copy = db.query(Copy).filter_by(id=copy_id).first()
    return model_to_schema(copy)

def get_copies_by_rented(rented: bool, db: Session = Depends(get_db())):
    copies = db.query(Copy).filter_by(rented=rented).all()
    return models_to_schemas(copies)

def get_copies_by_edition_id(ed_id: int, db: Session = Depends(get_db())):
    copies = db.query(Copy).filter_by(edition_id=ed_id).all()
    return models_to_schemas(copies)

def get_copies_by_editions(editions, db: Session = Depends(get_db())):
    copies = []
    for edition in editions:
        copies.extend(get_copies_by_edition_id(edition.id, db))
    return copies

def get_copies_by_book_id(book_id: int, db: Session = Depends(get_db())):
    editions = get_editions_by_book_id(book_id, db)
    return get_copies_by_editions(editions, db)

def get_copies_by_edition_title(title: str, db: Session = Depends(get_db())):
    editions = get_editions_by_edition_title(title, db)
    return get_copies_by_editions(editions, db)

def get_copies_by_original_title(title: str, db: Session = Depends(get_db())):
    editions = get_editions_by_original_title(title, db)
    return get_copies_by_editions(editions, db)

def get_copies_by_title(title: str, db: Session = Depends(get_db())):
    editions = get_editions_by_title(title, db)
    return get_copies_by_editions(editions, db)

def get_copies_by_edition_series(series: str, db: Session = Depends(get_db())):
    editions = get_editions_by_edition_series(series, db)
    return get_copies_by_editions(editions, db)

def get_copies_by_original_series(series: str, db: Session = Depends(get_db())):
    editions = get_editions_by_original_series(series, db)
    return get_copies_by_editions(editions, db)

def get_copies_by_series(series: str, db: Session = Depends(get_db())):
    editions = get_editions_by_series(series, db)
    return get_copies_by_editions(editions, db)

def get_copies_by_author_id(author_id: int, db: Session = Depends(get_db())):
    editions = get_editions_by_author_id(author_id, db)
    return get_copies_by_editions(editions, db)

def get_copies_by_author_name(name: str, db: Session = Depends(get_db())):
    editions = get_editions_by_author_name(name, db)
    return get_copies_by_editions(editions, db)

def get_copies_by_author_surname(surname: str, db: Session = Depends(get_db())):
    editions = get_editions_by_author_surname(surname, db)
    return get_copies_by_editions(editions, db)

def get_copies_by_author_full_name(name: str, surname: str, db: Session = Depends(get_db())):
    editions = get_editions_by_author_full_name(name, surname, db)
    return get_copies_by_editions(editions, db)

def get_copies_by_author_birth_year(year: int, db: Session = Depends(get_db())):
    editions = get_editions_by_author_birth_year(year, db)
    return get_copies_by_editions(editions, db)

def get_copies_by_author_death_year(year: int, db: Session = Depends(get_db())):
    editions = get_editions_by_author_death_year(year, db)
    return get_copies_by_editions(editions, db)

def get_copies_by_illustrator_id(illustrator_id: int, db: Session = Depends(get_db())):
    editions = get_editions_by_illustrator_id(illustrator_id, db)
    return get_copies_by_editions(editions, db)

def get_copies_by_illustrator_name(name: str, db: Session = Depends(get_db())):
    editions = get_editions_by_illustrator_name(name, db)
    return get_copies_by_editions(editions, db)

def get_copies_by_illustrator_surname(surname: str, db: Session = Depends(get_db())):
    editions = get_editions_by_illustrator_surname(surname, db)
    return get_copies_by_editions(editions, db)

def get_copies_by_illustrator_full_name(name: str, surname: str, db: Session = Depends(get_db())):
    editions = get_editions_by_illustrator_full_name(name, surname, db)
    return get_copies_by_editions(editions, db)

def get_copies_by_illustrator_birth_year(year: int, db: Session = Depends(get_db())):
    editions = get_editions_by_illustrator_birth_year(year, db)
    return get_copies_by_editions(editions, db)

def get_copies_by_illustrator_death_year(year: int, db: Session = Depends(get_db())):
    editions = get_editions_by_illustrator_death_year(year, db)
    return get_copies_by_editions(editions, db)

def get_copies_by_translator_id(translator_id: int, db: Session = Depends(get_db())):
    editions = get_editions_by_translator_id(translator_id, db)
    return get_copies_by_editions(editions, db)

def get_copies_by_translator_name(name: str, db: Session = Depends(get_db())):
    editions = get_editions_by_translator_name(name, db)
    return get_copies_by_editions(editions, db)

def get_copies_by_translator_surname(surname: str, db: Session = Depends(get_db())):
    editions = get_editions_by_translator_surname(surname, db)
    return get_copies_by_editions(editions, db)

def get_copies_by_translator_full_name(name: str, surname: str, db: Session = Depends(get_db())):
    editions = get_editions_by_translator_full_name(name, surname, db)
    return get_copies_by_editions(editions, db)

def get_copies_by_translator_birth_year(year: int, db: Session = Depends(get_db())):
    editions = get_editions_by_translator_birth_year(year, db)
    return get_copies_by_editions(editions, db)

def get_copies_by_translator_death_year(year: int, db: Session = Depends(get_db())):
    editions = get_editions_by_translator_death_year(year, db)
    return get_copies_by_editions(editions, db)

def get_copies_by_edition_language(language: str, db: Session = Depends(get_db())):
    editions = get_editions_by_edition_language(language, db)
    return get_copies_by_editions(editions, db)

def get_copies_by_edition_language_id(lang_id: int, db: Session = Depends(get_db())):
    editions = get_editions_by_edition_language_id(lang_id, db)
    return get_copies_by_editions(editions, db)

def get_copies_by_original_language(language: str, db: Session = Depends(get_db())):
    editions = get_editions_by_original_language(language, db)
    return get_copies_by_editions(editions, db)

def get_copies_by_original_language_id(lang_id: int, db: Session = Depends(get_db())):
    editions = get_editions_by_original_language_id(lang_id, db)
    return get_copies_by_editions(editions, db)

def get_copies_by_language(language: str, db: Session = Depends(get_db())):
    editions = get_editions_by_language(language, db)
    return get_copies_by_editions(editions, db)

def get_copies_by_language_id(lang_id: int, db: Session = Depends(get_db())):
    editions = get_editions_by_language_id(lang_id, db)
    return get_copies_by_editions(editions, db)

def get_copies_by_publisher_id(publisher_id: int, db: Session = Depends(get_db())):
    editions = get_editions_by_publisher_id(publisher_id, db)
    return get_copies_by_editions(editions, db)

def get_copies_by_publisher_name(name: str, db: Session = Depends(get_db())):
    editions = get_editions_by_publisher_name(name, db)
    return get_copies_by_editions(editions, db)

def get_copies_by_publisher_city(city: str, db: Session = Depends(get_db())):
    editions = get_editions_by_publisher_city(city, db)
    return get_copies_by_editions(editions, db)

def get_copies_by_publisher_foundation_year(year: int, db: Session = Depends(get_db())):
    editions = get_editions_by_publisher_foundation_year(year, db)
    return get_copies_by_editions(editions, db)

def get_copies_by_edition_number(num: int, db: Session = Depends(get_db())):
    editions = get_editions_by_edition_number(num, db)
    return get_copies_by_editions(editions, db)

def get_copies_by_edition_year(year: int, db: Session = Depends(get_db())):
    editions = get_editions_by_edition_year(year, db)
    return get_copies_by_editions(editions, db)

def get_copies_by_form(form: str, db: Session = Depends(get_db())):
    editions = get_editions_by_form(form, db)
    return get_copies_by_editions(editions, db)

def get_copies_by_form_id(form_id: int, db: Session = Depends(get_db())):
    editions = get_editions_by_form_id(form_id, db)
    return get_copies_by_editions(editions, db)

def get_copies_by_isbn(isbn: int, db: Session = Depends(get_db())):
    edition = get_edition_by_isbn(isbn, db)
    return get_copies_by_edition_id(edition.id, db)

def get_copies_by_ukd(ukd: str, db: Session = Depends(get_db())):
    edition = get_editions_by_ukd(ukd, db)
    return get_copies_by_edition_id(edition.id, db)


def model_to_schema(model: Type[Copy] | None):
    if model is None:
        return None
        #raise HTTPException(status_code=404, detail="Copy not found")

    return copy_schemas.Copy(
        id=model.id,
        ed_id=model.ed_id,
        rented=model.rented
    )


def models_to_schemas(models: List[Type[Copy]]):
    schemas = []
    for model in models:
        schema: copy_schemas.Copy = model_to_schema(model)
        schemas.append(schema)
    return schemas