from pydantic import BaseModel

class BookmarkBase(BaseModel):
    title: str
    url: str
    tag: str | None = None


class BookmarkCreate(BookmarkBase):
    pass


class BookmarkUpdate(BaseModel):
    title: str | None = None
    url: str | None = None
    tag: str | None = None


class BookmarkResponse(BookmarkBase):
    id: int
    user_id: str

    class Config:
        orm_mode = True
