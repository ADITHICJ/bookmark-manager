from datetime import datetime
from typing import Optional

from pydantic import BaseModel, HttpUrl


class BookmarkBase(BaseModel):
    title: str
    url: HttpUrl
    description: Optional[str] = None


class BookmarkCreate(BookmarkBase):
    pass


class BookmarkUpdate(BaseModel):
    title: Optional[str] = None
    url: Optional[HttpUrl] = None
    description: Optional[str] = None


class Bookmark(BookmarkBase):
    id: str
    user_id: str
    created_at: datetime

    class Config:
        from_attributes = True
