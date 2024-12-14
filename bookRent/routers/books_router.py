from fastapi import APIRouter, HTTPException

from bookRent.BooksCRUD.add.book_add import add_copy
from bookRent.BooksCRUD.add.rental_add import add_reservation, add_rental
from bookRent.BooksCRUD.get.copy_get import *
from bookRent.db_config import get_db
from bookRent.schematics.schematics import CopyCreate, ReservationCreate, RentalCreate

router = APIRouter()

# Tylko dla workerów
@router.post("/add")
async def add(copy: CopyCreate, db: Session = Depends(get_db())):
    try:
        # Używamy modelu CopyCreate do przekazania danych do funkcji add_copy
        result = add_copy(
            original_title=copy.original_title,
            original_lang=copy.original_language,
            original_series=copy.original_series,
            edition_title=copy.edition_title,
            edition_lang=copy.edition_language,
            edition_series=copy.edition_series,
            author_name=copy.author.name,
            author_surname=copy.author.surname,
            birth_year=copy.author.birth_year,
            death_year=copy.author.death_year,
            illustrator_name=copy.illustrator.name,
            illustrator_surname=copy.illustrator.surname,
            translator_name=copy.translator.name,
            translator_surname=copy.translator.surname,
            publisher=copy.publisher,
            edition_number=copy.edition_number,
            edition_year=copy.edition_year,
            form=copy.form,
            isbn=copy.isbn,
            ukd=copy.ukd,
            categories=copy.categories,
            db=db
        )
        return result

    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

# User
@router.post("/reserve")
async def make_reservation(reservation: ReservationCreate, db: Session = Depends(get_db())):
    try:
        result = add_reservation(
            user_id=reservation.user_id,
            copy_id=reservation.copy_id,
            db=db
        )
        return result

    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


# Worker
@router.post("/rent")
async def rent(rental: RentalCreate, db: Session = Depends(get_db())):
    try:
        result = add_rental(
            user_id=rental.user_id,
            copy_id=rental.copy_id,
            db=db
        )
        return result

    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

"""
@router.get("/get_copies_alt")
def get_copies_alt(copy: CopySearch, db: Session = Depends(get_db())):
    try:
        result = bookRent.BooksCRUD.get.copy_get.get_copies(copy, db)
        return result

    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
"""

@router.get("/get_copies")
def get_copies(cond: dict, db: Session = Depends(get_db())):
    try:
        temp = []
        if cond["copy_id"]:
            temp.append(get_copy_by_id(cond["copy_id"], db))
        if cond["rented"] is not None:
            temp.append(get_copies_by_rented(cond["rented"], db))
        if cond["ed_id"]:
            temp.append(get_edition_by_id(cond["ed_id"], db))
        if cond["book_id"]:
            temp.append(get_editions_by_book_id(cond["book_id"], db))
        if cond["ed_title"]:
            temp.append(get_copies_by_edition_title(cond["ed_title"], db))
        if cond["or_title"]:
            temp.append(get_copies_by_original_title(cond["or_title"], db))
        if cond["title"]:
            temp.append(get_copies_by_title(cond["title"], db))
        if cond["ed_series"]:
            temp.append(get_copies_by_edition_series(cond["ed_series"], db))
        if cond["or_series"]:
            temp.append(get_copies_by_original_series(cond["or_series"], db))
        if cond["series"]:
            temp.append(get_copies_by_series(cond["series"], db))
        if cond["author_id"]:
            temp.append(get_copies_by_author_id(cond["author_id"], db))
        if cond["author_name"]:
            temp.append(get_copies_by_author_name(cond["author_name"], db))
        if cond["author_surname"]:
            temp.append(get_copies_by_author_surname(cond["author_surname"], db))
        if cond["author_birth"]:
            temp.append(get_copies_by_author_birth_year(cond["author_birth"], db))
        if cond["author_death"]:
            temp.append(get_copies_by_author_death_year(cond["author_death"], db))
        if cond["ill_id"]:
            temp.append(get_copies_by_illustrator_id(cond["ill_id"], db))
        if cond["ill_name"]:
            temp.append(get_copies_by_illustrator_name(cond["ill_name"], db))
        if cond["ill_surname"]:
            temp.append(get_copies_by_illustrator_surname(cond["ill_surname"], db))
        if cond["ill_birth"]:
            temp.append(get_copies_by_illustrator_birth_year(cond["ill_birth"], db))
        if cond["ill_death"]:
            temp.append(get_copies_by_illustrator_death_year(cond["ill_death"], db))
        if cond["tran_id"]:
            temp.append(get_copies_by_translator_id(cond["tran_id"], db))
        if cond["tran_name"]:
            temp.append(get_copies_by_translator_name(cond["tran_name"], db))
        if cond["tran_surname"]:
            temp.append(get_copies_by_translator_surname(cond["tran_surname"], db))
        if cond["tran_birth"]:
            temp.append(get_copies_by_translator_birth_year(cond["tran_birth"], db))
        if cond["tran_death"]:
            temp.append(get_copies_by_translator_death_year(cond["tran_death"], db))
        if cond["ed_lang"]:
            temp.append(get_copies_by_edition_language(cond["ed_lang"], db))
        if cond["ed_lang_id"]:
            temp.append(get_copies_by_edition_language_id(cond["ed_lang_id"], db))
        if cond["or_lang"]:
            temp.append(get_copies_by_original_language(cond["or_lang"], db))
        if cond["or_lang_id"]:
            temp.append(get_copies_by_original_language_id(cond["or_lang_id"], db))
        if cond["lang"]:
            temp.append(get_copies_by_language(cond["lang"], db))
        if cond["lang_id"]:
            temp.append(get_copies_by_language_id(cond["lang_id"], db))
        if cond["publ_id"]:
            temp.append(get_copies_by_publisher_id(cond["publ_id"], db))
        if cond["publ_name"]:
            temp.append(get_copies_by_publisher_name(cond["publ_name"], db))
        if cond["publ_city"]:
            temp.append(get_copies_by_publisher_city(cond["publ_city"], db))
        if cond["publ_year"]:
            temp.append(get_copies_by_publisher_foundation_year(cond["publ_year"], db))
        if cond["ed_num"]:
            temp.append(get_copies_by_edition_number(cond["ed_num"], db))
        if cond["ed_year"]:
            temp.append(get_copies_by_edition_year(cond["ed_year"], db))
        if cond["form"]:
            temp.append(get_copies_by_form(cond["form"], db))
        if cond["form_id"]:
            temp.append(get_copies_by_form_id(cond["form_id"], db))
        if cond["isbn"]:
            temp.append(get_copies_by_isbn(cond["isbn"], db))
        if cond["ukd"]:
            temp.append(get_copies_by_ukd(cond["ukd"], db))

        inter = False
        if cond["intersect"]:
            inter = True

        return get_results(temp, inter)

    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))



@router.get("/get_editions")
def get_editions(cond: dict, db: Session = Depends(get_db())):
    try:
        temp = []
        if cond["ed_id"]:
            temp.append(get_edition_by_id(cond["ed_id"], db))
        if cond["book_id"]:
            temp.append(get_editions_by_book_id(cond["book_id"], db))
        if cond["ed_title"]:
            temp.append(get_editions_by_edition_title(cond["ed_title"], db))
        if cond["or_title"]:
            temp.append(get_editions_by_original_title(cond["or_title"], db))
        if cond["title"]:
            temp.append(get_editions_by_title(cond["title"], db))
        if cond["ed_series"]:
            temp.append(get_editions_by_edition_series(cond["ed_series"], db))
        if cond["or_series"]:
            temp.append(get_editions_by_original_series(cond["or_series"], db))
        if cond["series"]:
            temp.append(get_editions_by_series(cond["series"], db))
        if cond["author_id"]:
            temp.append(get_editions_by_author_id(cond["author_id"], db))
        if cond["author_name"]:
            temp.append(get_editions_by_author_name(cond["author_name"], db))
        if cond["author_surname"]:
            temp.append(get_editions_by_author_surname(cond["author_surname"], db))
        if cond["author_birth"]:
            temp.append(get_editions_by_author_birth_year(cond["author_birth"], db))
        if cond["author_death"]:
            temp.append(get_editions_by_author_death_year(cond["author_death"], db))
        if cond["ill_id"]:
            temp.append(get_editions_by_illustrator_id(cond["ill_id"], db))
        if cond["ill_name"]:
            temp.append(get_editions_by_illustrator_name(cond["ill_name"], db))
        if cond["ill_surname"]:
            temp.append(get_editions_by_illustrator_surname(cond["ill_surname"], db))
        if cond["ill_birth"]:
            temp.append(get_editions_by_illustrator_birth_year(cond["ill_birth"], db))
        if cond["ill_death"]:
            temp.append(get_editions_by_illustrator_death_year(cond["ill_death"], db))
        if cond["tran_id"]:
            temp.append(get_editions_by_translator_id(cond["tran_id"], db))
        if cond["tran_name"]:
            temp.append(get_editions_by_translator_name(cond["tran_name"], db))
        if cond["tran_surname"]:
            temp.append(get_editions_by_translator_surname(cond["tran_surname"], db))
        if cond["tran_birth"]:
            temp.append(get_editions_by_translator_birth_year(cond["tran_birth"], db))
        if cond["tran_death"]:
            temp.append(get_editions_by_translator_death_year(cond["tran_death"], db))
        if cond["ed_lang"]:
            temp.append(get_editions_by_edition_language(cond["ed_lang"], db))
        if cond["ed_lang_id"]:
            temp.append(get_editions_by_edition_language_id(cond["ed_lang_id"], db))
        if cond["or_lang"]:
            temp.append(get_editions_by_original_language(cond["or_lang"], db))
        if cond["or_lang_id"]:
            temp.append(get_editions_by_original_language_id(cond["or_lang_id"], db))
        if cond["lang"]:
            temp.append(get_editions_by_language(cond["lang"], db))
        if cond["lang_id"]:
            temp.append(get_editions_by_language_id(cond["lang_id"], db))
        if cond["publ_id"]:
            temp.append(get_editions_by_publisher_id(cond["publ_id"], db))
        if cond["publ_name"]:
            temp.append(get_editions_by_publisher_name(cond["publ_name"], db))
        if cond["publ_city"]:
            temp.append(get_editions_by_publisher_city(cond["publ_city"], db))
        if cond["publ_year"]:
            temp.append(get_editions_by_publisher_foundation_year(cond["publ_year"], db))
        if cond["ed_num"]:
            temp.append(get_editions_by_edition_number(cond["ed_num"], db))
        if cond["ed_year"]:
            temp.append(get_editions_by_edition_year(cond["ed_year"], db))
        if cond["form"]:
            temp.append(get_editions_by_form(cond["form"], db))
        if cond["form_id"]:
            temp.append(get_editions_by_form_id(cond["form_id"], db))
        if cond["isbn"]:
            temp.append(get_edition_by_isbn(cond["isbn"], db))
        if cond["ukd"]:
            temp.append(get_edition_by_ukd(cond["ukd"], db))

        inter = False
        if cond["intersect"]:
            inter = True

        return get_results(temp, inter)


    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))



@router.get("/get_books")
def get_books(cond: dict, db: Session = Depends(get_db())):
    try:
        temp = []
        if cond["book_id"]:
            temp.append(get_book_by_id(cond["book_id"], db))
        if cond["or_title"]:
            temp.append(get_books_by_title(cond["or_title"], db))
        if cond["title"]:
            temp.append(get_books_by_title(cond["title"], db))
        if cond["or_series"]:
            temp.append(get_books_by_series(cond["or_series"], db))
        if cond["series"]:
            temp.append(get_books_by_series(cond["series"], db))
        if cond["author_id"]:
            temp.append(get_books_by_author_id(cond["author_id"], db))
        if cond["author_name"]:
            temp.append(get_books_by_author_name(cond["author_name"], db))
        if cond["author_surname"]:
            temp.append(get_books_by_author_surname(cond["author_surname"], db))
        if cond["author_birth"]:
            temp.append(get_books_by_author_birth_year(cond["author_birth"], db))
        if cond["author_death"]:
            temp.append(get_books_by_author_death_year(cond["author_death"], db))
        if cond["or_lang"]:
            temp.append(get_books_by_language(cond["lang"], db))
        if cond["or_lang_id"]:
            temp.append(get_books_by_language_id(cond["lang_id"], db))
        if cond["lang"]:
            temp.append(get_books_by_language(cond["lang"], db))
        if cond["lang_id"]:
            temp.append(get_books_by_language_id(cond["lang_id"], db))

        inter = False
        if cond["intersect"]:
            inter = True

        return get_results(temp, inter)


    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))




def get_results(temp, inter: bool):
    result = []
    if inter:
        result = set()
        for i in temp:
            if not result:
                result.add(i)
            else:
                result = set(result).intersection(i)
            if not result:
                return []
    else:
        for i in temp:
            result.extend(i)

    result = list(set(result))
    return result





"""
@router.get("/get_copies", response_model=)
def get_copies(copy: CopySearch, db: Session = Depends(get_db())):
    try:

        inter = copy.intersect
        temp = []
        if copy.id:
            temp.append(get_copy_by_id(copy.id, db))
            if not temp[0] and inter:
                return None

        if copy.edition:
            temp.extend(get_editions(copy.edition, inter, db))



        inter = copy.intersect
        if copy.id:
            cid = get_copy_by_id(copy.id, db)
        if copy.edition:
            ed = copy.edition
            if ed.id:
                eid = get_copies_by_edition_id(ed.id, db)
            if





    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


def get_editions(ed: EditionSearch, intersect: Optional[bool] = None, db: Session = Depends(get_db())):
    inter = False
    if ed.intersect:
        inter = ed.intersect
    if intersect:
        inter = intersect

    temp = []

    if ed.id:
        temp.append(get_copies_by_edition_id(ed.id, db))
    if ed.edition_title:
        temp.append(get_copies_by_edition_title(ed.edition_title, db))
    if ed.edition_series:
        temp.append(get_copies_by_edition_series(ed.edition_series, db))
    if ed.edition_number:
        temp.append(get_copies_by_edition_number(ed.edition_number, db))
    if ed.edition_year:
        temp.append(get_copies_by_edition_year(ed.edition_year, db))
    if ed.isbn:
        temp.append(get_copies_by_isbn(ed.isbn, db))
    if ed.ukd:
        temp.append(get_copies_by_ukd(ed.ukd, db))
    if ed.book:
        temp.extend(get_books(ed.book, inter, db))






def get_books(book: BookSearch, intersect: Optional[bool] = None, db: Session = Depends(get_db())):
    inter = False
    if book.intersect:
        inter = book.intersect
    if intersect:
        inter = intersect

    temp = []
    if book.id:
        temp.append(get_copies_by_book_id(book.id, db))
    if book.original_title:
        temp.append(get_copies_by_original_title(book.original_title, db))
    if book.original_series:
        temp.append(get_copies_by_original_series(book.original_series, db))
    if book.



def get_or_langs(lang: LanguageSearch, intersect: Optional[bool] = None, db: Session = Depends(get_db())):
    inter = False
    if lang.intersect:
        inter = lang.intersect
    if intersect:
        inter = intersect

    temp = []

    if lang.id:
        temp.append(get_copies_by_original_language_id(lang.id, db))
    if lang.language:
        temp.append(get_copies_by_original_language(lang.language, db))

    return temp


def get_or_langs(lang: LanguageSearch, intersect: Optional[bool] = None, db: Session = Depends(get_db())):
    inter = False
    if lang.intersect:
        inter = lang.intersect
    if intersect:
        inter = intersect

    temp = []

    if lang.id:
        temp.append(get_copies_by_edition_language_id(lang.id, db))
    if lang.language:
        temp.append(get_copies_by_edition_language(lang.language, db))

    return temp


def get_forms(form: FormSearch, intersect: Optional[bool] = None, db: Session = Depends(get_db())):
    inter = False
    if form.intersect:
        inter = form.intersect
    if intersect:
        inter = intersect

    temp = []

    if form.id:
        temp.append(get_copies_by_form_id(form.id, db))
    if form.form:
        temp.append(get_copies_by_form(form.form, db))

    return temp


def get_authors(author: PersonSearch, intersect: Optional[bool] = None, db: Session = Depends(get_db())):
    inter = False
    if author.intersect:
        inter = author.intersect
    if intersect:
        inter = intersect

    temp = []

    if author.id:
        temp.append(get_copies_by_a)


def get_illustrators(ill: PersonSearch, intersect: Optional[bool] = None, db: Session = Depends(get_db())):
    inter = False
    if ed.intersect:
        inter = ed.intersect
    if intersect:
        inter = intersect


def get_translators(tran: PersonSearch, intersect: Optional[bool] = None, db: Session = Depends(get_db())):
    inter = False
    if ed.intersect:
        inter = ed.intersect
    if intersect:
        inter = intersect


def get_publishers(publisher: Publisher, intersect: Optional[bool] = None, db: Session = Depends(get_db())):
    inter = False
    if ed.intersect:
        inter = ed.intersect
    if intersect:
        inter = intersect
"""

def join_lists(to, from_, intersect: bool):
    if intersect and to != []:
        to = set(to).intersection(from_)
        to = list(to)
        return to

    to.append(from_)
    return to