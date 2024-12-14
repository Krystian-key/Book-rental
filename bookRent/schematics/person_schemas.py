from typing import Optional

from pydantic import BaseModel


class PersonBase(BaseModel):
    name: str
    surname: str
    birth_year: Optional[int] = None
    death_year: Optional[int] = None


class PersonCreate(PersonBase):
    pass


class Person(PersonBase):
    id: int

    class Config:
        orm_mode = True