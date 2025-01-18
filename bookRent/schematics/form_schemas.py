from pydantic import BaseModel, ConfigDict


class FormBase(BaseModel):
    form: str


class FormCreate(FormBase):
    pass


class Form(FormBase):
    id: int
    model_config = ConfigDict(from_attributes=True)


class FormUpdate(Form):
    pass