from fastapi import APIRouter, HTTPException

from bookRent.BooksCRUD.book_add import add_copy, add_annotation
from bookRent.BooksCRUD.rental_add import add_reservation, add_rental
from bookRent.schematics.schematics import CopyCreate, AnnotationCreate, ReservationCreate, RentalCreate

router = APIRouter()

# Tylko dla workerów
@router.post("/add")
async def add(copy: CopyCreate):
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
            categories=copy.categories
        )
        return result

    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

# User
@router.post("/reserve")
async def make_reservation(reservation: ReservationCreate):
    try:
        result = add_reservation(
            user_id=reservation.user_id,
            copy_id=reservation.copy_id
        )
        return result

    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


# Worker
@router.post("/rent")
async def rent(rental: RentalCreate):
    try:
        result = add_rental(
            user_id=rental.user_id,
            copy_id=rental.copy_id
        )
        return result

    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
