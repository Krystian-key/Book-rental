from pydantic import BaseModel


class LanguageBase(BaseModel):
    lang: str


class LanguageCreate(LanguageBase):
    pass


class Language(LanguageBase):
    id: int

    class Config:
        orm_mode = True