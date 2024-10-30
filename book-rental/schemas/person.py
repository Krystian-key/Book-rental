from pydantic import BaseModel
from typing import Optional

class Person(BaseModel):
    name: str
    surname: str
    birth_year: Optional[str] = None
    death_year: Optional[str] = None