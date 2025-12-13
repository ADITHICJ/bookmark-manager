from pydantic import BaseModel


class TagBase(BaseModel):
    name: str
    color: str


class TagCreate(TagBase):
    pass


class Tag(TagBase):
    id: str
    user_id: str

    class Config:
        from_attributes = True
