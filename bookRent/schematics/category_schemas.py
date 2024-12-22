from pydantic import BaseModel


class CategoryBase(BaseModel):
    category: str


class CategoryCreate(CategoryBase):
    pass


class Category(CategoryBase):
    id: int

    class Config:
        from_attributes = True