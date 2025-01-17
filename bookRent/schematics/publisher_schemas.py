from typing import Optional

from pydantic import BaseModel, ConfigDict


class PublisherBase(BaseModel):
    name: str
    localization: str
    foundation_year: int


class PublisherCreate(PublisherBase):
    pass


class Publisher(PublisherBase):
    id: int
    model_config = ConfigDict(from_attributes=True)


class PublisherUpdate(BaseModel):
    id: int
    name: Optional[str] = None
    localization: Optional[str] = None
    foundation_year: Optional[int] = None