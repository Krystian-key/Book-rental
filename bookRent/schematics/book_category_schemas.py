from pydantic import BaseModel


class BookCategoryBase(BaseModel):
    book_id: int
    category_id: int


class BookCategoryCreate(BookCategoryBase):
    pass


class BookCategory(BookCategoryBase):

    class Config:
        orm_mode = True