from pydantic import BaseModel


class PublisherBase(BaseModel):
    name: str
    localization: str
    foundation_year: int


class PublisherCreate(PublisherBase):
    pass


class Publisher(PublisherBase):
    id: int

    class Config:
        orm_mode = True