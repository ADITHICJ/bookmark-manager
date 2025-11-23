from fastapi import APIRouter, Depends, HTTPException

from app.api.deps import get_current_user
from app.schemas.bookmark import BookmarkCreate, BookmarkUpdate
from app.services.bookmark_service import (
    create_bookmark,
    list_bookmarks,
    get_bookmark_by_id,
    update_bookmark,
    delete_bookmark,
)

router = APIRouter(prefix="/bookmarks", tags=["Bookmarks"])


@router.post("/")
def create(data: BookmarkCreate, user=Depends(get_current_user)):
    return create_bookmark(data, user["sub"])


@router.get("/")
def get_all(user=Depends(get_current_user)):
    return list_bookmarks(user["sub"])


@router.get("/{bookmark_id}")
def get_one(bookmark_id: int, user=Depends(get_current_user)):
    result = get_bookmark_by_id(bookmark_id, user["sub"])
    if not result:
        raise HTTPException(status_code=404, detail="Bookmark not found")
    return result


@router.put("/{bookmark_id}")
def update(bookmark_id: int, data: BookmarkUpdate, user=Depends(get_current_user)):
    result = update_bookmark(bookmark_id, data, user["sub"])
    if not result:
        raise HTTPException(status_code=404, detail="Bookmark not found")
    return result


@router.delete("/{bookmark_id}")
def remove(bookmark_id: int, user=Depends(get_current_user)):
    if not delete_bookmark(bookmark_id, user["sub"]):
        raise HTTPException(status_code=404, detail="Bookmark not found")
    return {"message": "Deleted"}
