from typing import Optional

from pydantic import BaseModel


class PersonBase(BaseModel):
    name: str
    surname: Optional[str] = None
    birth_year: Optional[int] = None
    death_year: Optional[int] = None


class PersonCreate(PersonBase):
    pass


class Person(PersonBase):
    id: int

    class Config:
        from_attributes = True


class PersonUpdate(BaseModel):
    id: int
    name: Optional[str] = None
    surname: Optional[str] = None
    birth_year: Optional[int] = None
    death_year: Optional[int] = None