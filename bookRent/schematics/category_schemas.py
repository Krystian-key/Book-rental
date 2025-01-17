from pydantic import BaseModel, ConfigDict


class CategoryBase(BaseModel):
    category: str


class CategoryCreate(CategoryBase):
    pass


class Category(CategoryBase):
    id: int
    model_config = ConfigDict(from_attributes=True)

class CategoryUpdate(Category):
    pass