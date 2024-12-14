from typing import Optional

from pydantic import BaseModel

class AnnotationCreate(BaseModel):
    content: str
    book_id: Optional[int] = None
    edition_id: Optional[int] = None
    copy_id: Optional[int] = None

    class Config:
        orm_mode = True