from typing import Optional

from pydantic import BaseModel, ConfigDict

class AnnotationBase(BaseModel):
    book_id: Optional[int] = None
    ed_id: Optional[int] = None
    copy_id: Optional[int] = None
    content: str

class AnnotationCreate(AnnotationBase):
    pass


class Annotation(AnnotationBase):
    id: int
    model_config = ConfigDict(from_attributes=True)