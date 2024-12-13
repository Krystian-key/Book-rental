

from fastapi import FastAPI
from bookRent.db_config import initialize_tables

from bookRent.routers.auth_router import router as auth_router
from bookRent.routers.worker_router import router as worker_router
from bookRent.routers.user_router import router as user_router
from bookRent.routers.books_router import router as books_router
from bookRent.routers.publishers_router import router as publishers_router
from bookRent.routers.annotation_router import router as annotation_router


app = FastAPI()

@app.on_event("startup")
def startup():
    initialize_tables()

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


app.include_router(user_router, prefix="/users", tags=["users"])

app.include_router(auth_router, prefix="/auth", tags=["auth"])

app.include_router(worker_router, prefix="/worker", tags=["worker"])

app.include_router(books_router, prefix="/books", tags=["books"])

app.include_router(publishers_router, prefix="/publishers", tags=["publishers"])

app.include_router(annotation_router, prefix="/annotations", tags=["annotations"])

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