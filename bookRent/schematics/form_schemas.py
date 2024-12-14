from pydantic import BaseModel


class FormBase(BaseModel):
    form: str


class FormCreate(FormBase):
    pass


class Form(FormBase):
    id: int

    class Config:
        orm_mode = True