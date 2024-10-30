from pydantic import BaseModel

class Publisher(BaseModel):
    name: str
    city: str
    foundation_year: int