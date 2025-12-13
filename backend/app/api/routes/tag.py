from fastapi import APIRouter, Depends, HTTPException, status
from typing import List

from app.api.deps import get_current_user
from app.schemas.tag import Tag, TagCreate
from app.services import tag_service

router = APIRouter(prefix="/tags", tags=["tags"])


def _get_user_id(user: dict) -> str:
    uid = user.get("sub") or user.get("id")
    if not uid:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid user token",
        )
    return uid


@router.get("/", response_model=List[Tag])
def list_tags(current=Depends(get_current_user)):
    return tag_service.list_tags(_get_user_id(current))


@router.post("/", response_model=Tag, status_code=status.HTTP_201_CREATED)
def create_tag(data: TagCreate, current=Depends(get_current_user)):
    return tag_service.create_tag(_get_user_id(current), data)


@router.delete("/{tag_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_tag(tag_id: str, current=Depends(get_current_user)):
    ok = tag_service.delete_tag(_get_user_id(current), tag_id)
    if not ok:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Tag not found",
        )
    return
