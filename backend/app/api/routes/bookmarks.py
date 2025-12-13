from typing import List
from fastapi import APIRouter, Depends, HTTPException, status

from app.api.deps import get_current_user
from app.schemas.bookmark import Bookmark, BookmarkCreate, BookmarkUpdate
from app.services import bookmark_service

router = APIRouter(prefix="/bookmarks", tags=["bookmarks"])


def _get_user_id_from_token(clerk_payload: dict) -> str:
    user_id = (
        clerk_payload.get("sub")
        or clerk_payload.get("id")
        or clerk_payload.get("user_id")
    )
    if not user_id:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Could not determine user_id from token",
        )
    return user_id


@router.get("/", response_model=List[Bookmark])
def list_user_bookmarks(current_user=Depends(get_current_user)):
    user_id = _get_user_id_from_token(current_user)
    return bookmark_service.list_bookmarks(user_id)


@router.post("/", response_model=Bookmark, status_code=status.HTTP_201_CREATED)
def create_user_bookmark(
    data: BookmarkCreate,
    current_user=Depends(get_current_user),
):
    user_id = _get_user_id_from_token(current_user)
    return bookmark_service.create_bookmark(user_id, data)


@router.get("/{bookmark_id}", response_model=Bookmark)
def get_user_bookmark(
    bookmark_id: str,
    current_user=Depends(get_current_user),
):
    user_id = _get_user_id_from_token(current_user)
    bookmark = bookmark_service.get_bookmark(user_id, bookmark_id)
    if not bookmark:
        raise HTTPException(status_code=404, detail="Bookmark not found")
    return bookmark


@router.put("/{bookmark_id}", response_model=Bookmark)
def update_user_bookmark(
    bookmark_id: str,
    data: BookmarkUpdate,
    current_user=Depends(get_current_user),
):
    user_id = _get_user_id_from_token(current_user)
    bookmark = bookmark_service.update_bookmark(user_id, bookmark_id, data)
    if not bookmark:
        raise HTTPException(status_code=404, detail="Bookmark not found")
    return bookmark


@router.delete("/{bookmark_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user_bookmark(
    bookmark_id: str,
    current_user=Depends(get_current_user),
):
    user_id = _get_user_id_from_token(current_user)
    bookmark_service.delete_bookmark(user_id, bookmark_id)
    return
