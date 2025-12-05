from pydantic import BaseModel


class TagBase(BaseModel):
    tag_name: str


class TagCreate(TagBase):
    pass


class Tag(TagBase):
    tag_id: str
    user_id: str

    class Config:
        from_attributes = True
