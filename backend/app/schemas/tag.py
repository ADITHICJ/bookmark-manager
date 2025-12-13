from datetime import datetime
from pydantic import BaseModel


class TagBase(BaseModel):
    name: str
    color: str


class TagCreate(TagBase):
    pass


class Tag(TagBase):
    id: str
    user_id: str
    created_at: datetime

    class Config:
        from_attributes = True
