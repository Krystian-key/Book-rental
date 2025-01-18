

from fastapi import FastAPI
from contextlib import asynccontextmanager
from apscheduler.schedulers.background import BackgroundScheduler

from bookRent.BooksCRUD.update.reservation_update import update_all_reservations
from bookRent.db_config import initialize_tables

from bookRent.routers.auth_router import router as auth_router
from bookRent.routers.worker_router import router as worker_router
from bookRent.routers.user_router import router as user_router
from bookRent.routers.rental_router import router as rental_router
from bookRent.routers.reservation_router import router as reservation_router
from bookRent.routers.book_router import router as book_router
from bookRent.routers.edition_router import router as edition_router
from bookRent.routers.copy_router import router as copy_router
from bookRent.routers.annotation_router import router as annotation_router
from bookRent.routers.publisher_router import router as publisher_router
from bookRent.routers.person_router import router as person_router
from bookRent.routers.language_router import router as language_router
from bookRent.routers.form_router import router as form_router
from bookRent.routers.category_router import router as category_router
from bookRent.routers.book_category_router import router as book_category_router
from bookRent.config.cors import add_cors



# Konfiguracja harmonogramu
scheduler = BackgroundScheduler()

# Dodanie zadania, które uruchamia się codziennie o północy
scheduler.add_job(update_all_reservations, 'cron', hour=0, minute=0)

@asynccontextmanager
async def lifespan(app: FastAPI):
    initialize_tables()
    scheduler.start()
    yield
    scheduler.shutdown()

app = FastAPI(lifespan=lifespan)

add_cors(app)

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


app.include_router(user_router, prefix="/users", tags=["users"])

app.include_router(auth_router, prefix="/auth", tags=["auth"])

app.include_router(worker_router, prefix="/worker", tags=["worker"])

app.include_router(book_router, prefix="/book", tags=["book"])

app.include_router(publisher_router, prefix="/publisher", tags=["publisher"])

app.include_router(annotation_router, prefix="/annotation", tags=["annotation"])

app.include_router(rental_router, prefix="/rental", tags=["rental"])

app.include_router(reservation_router, prefix="/reservation", tags=["reservation"])
app.include_router(edition_router, prefix="/edition", tags=["edition"])
app.include_router(copy_router, prefix="/copy", tags=["copy"])
app.include_router(person_router, prefix="/person", tags=["person"])
app.include_router(language_router, prefix="/language", tags=["language"])
app.include_router(form_router, prefix="/form", tags=["form"])
app.include_router(category_router, prefix="/category", tags=["category"])
app.include_router(book_category_router, prefix="/book-category", tags=["book-category"])

"""
@app.post("/login")
def login(user: UserLogin, db: Session = Depends(get_db)):
    db_user = db.query(bookRent.models.user_model.User).filter(bookRent.models.user_model.User.username == user.username).first()
    if not db_user:
        raise HTTPException(status_code=400, detail="Invalid username or password")

    if not verify_password(user.password, db_user.password):
        raise HTTPException(status_code=400, detail="Invalid username or password")

    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": db_user.username}, expires_delta=access_token_expires
    )

    return {"access_token": access_token, "token_type": "bearer"}

"""