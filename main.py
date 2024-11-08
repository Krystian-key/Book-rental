from fastapi import FastAPI
from bookRent.db_config import initialize_tables
from bookRent.routers.user_router import router as user_router


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