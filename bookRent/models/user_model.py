from pydantic import BaseModel, constr

class ReaderCreate(BaseModel):
    username: constr(min_length=4, max_length=15)
    password: constr(min_length=8)

    class Config:
        orm_mode = True


