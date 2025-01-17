from pydantic import BaseModel, ConfigDict


class LanguageBase(BaseModel):
    lang: str


class LanguageCreate(LanguageBase):
    pass


class Language(LanguageBase):
    id: int
    model_config = ConfigDict(from_attributes=True)


class LanguageUpdate(Language):
    pass