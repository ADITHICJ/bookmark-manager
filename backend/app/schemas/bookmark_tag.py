from pydantic import BaseModel


class BookmarkTagCreate(BaseModel):
    bookmark_id: str
    tag_id: str
