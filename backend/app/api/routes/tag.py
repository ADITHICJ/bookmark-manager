from fastapi import APIRouter, Depends, HTTPException
from typing import List

from app.api.deps import get_current_user
from app.schemas.tag import Tag, TagCreate
from app.services import tag_service

router = APIRouter(prefix="/tags", tags=["tags"])


def _uid(u): return u.get("sub") or u.get("id")


@router.get("/", response_model=List[Tag])
def list_tags(current=Depends(get_current_user)):
    return tag_service.list_tags(_uid(current))


@router.post("/", response_model=Tag, status_code=201)
def create_tag(data: TagCreate, current=Depends(get_current_user)):
    return tag_service.create_tag(_uid(current), data)


@router.delete("/{tag_id}", status_code=204)
def delete_tag(tag_id: str, current=Depends(get_current_user)):
    ok = tag_service.delete_tag(_uid(current), tag_id)
    if not ok:
        raise HTTPException(404, "Tag not found")
    return
