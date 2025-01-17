from pydantic import BaseModel, ConfigDict


class BookCategoryBase(BaseModel):
    book_id: int
    category_id: int


class BookCategoryCreate(BookCategoryBase):
    pass


class BookCategory(BookCategoryBase):
    model_config = ConfigDict(from_attributes=True)