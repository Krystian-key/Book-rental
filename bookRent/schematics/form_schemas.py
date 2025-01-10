from pydantic import BaseModel


class FormBase(BaseModel):
    form: str


class FormCreate(FormBase):
    pass


class Form(FormBase):
    id: int

    class Config:
        from_attributes = True


class FormUpdate(Form):
    pass