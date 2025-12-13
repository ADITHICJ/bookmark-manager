from datetime import datetime
from typing import Optional, List
from pydantic import BaseModel, HttpUrl


# ---------- Base ----------
class BookmarkBase(BaseModel):
    title: str
    url: HttpUrl
    description: Optional[str] = None
    category_id: Optional[str] = None


# ---------- Create ----------
class BookmarkCreate(BookmarkBase):
    tag_ids: Optional[List[str]] = []


# ---------- Update ----------
class BookmarkUpdate(BaseModel):
    title: Optional[str] = None
    url: Optional[HttpUrl] = None
    description: Optional[str] = None
    category_id: Optional[str] = None
    tag_ids: Optional[List[str]] = None


# ---------- Response ----------
class Bookmark(BookmarkBase):
    id: str
    user_id: str
    created_at: datetime

    class Config:
        from_attributes = True
