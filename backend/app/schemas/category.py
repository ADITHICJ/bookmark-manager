from datetime import datetime
from pydantic import BaseModel


class CategoryBase(BaseModel):
    name: str


class CategoryCreate(CategoryBase):
    pass


class Category(CategoryBase):
    category_id: str
    user_id: str
    created_at: datetime

    class Config:
        from_attributes = True
