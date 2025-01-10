from pydantic import BaseModel


class LanguageBase(BaseModel):
    lang: str


class LanguageCreate(LanguageBase):
    pass


class Language(LanguageBase):
    id: int

    class Config:
        from_attributes = True


class LanguageUpdate(Language):
    pass