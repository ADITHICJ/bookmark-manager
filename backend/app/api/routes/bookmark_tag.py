from fastapi import APIRouter, Depends, HTTPException
from app.api.deps import get_current_user
from app.schemas.bookmark_tag import BookmarkTagCreate
from app.services import bookmark_tag_service

router = APIRouter(prefix="/bookmark-tags", tags=["bookmark-tags"])


def _uid(u): return u.get("sub") or u.get("id")


@router.post("/", status_code=201)
def add_tag(data: BookmarkTagCreate, current=Depends(get_current_user)):
    try:
        return bookmark_tag_service.add_tag_to_bookmark(_uid(current), data)
    except ValueError as e:
        raise HTTPException(404, str(e))


@router.delete("/", status_code=204)
def remove_tag(bookmark_id: str, tag_id: str, current=Depends(get_current_user)):
    bookmark_tag_service.remove_tag_from_bookmark(_uid(current), bookmark_id, tag_id)
    return


@router.get("/bookmark/{bookmark_id}")
def list_tags(bookmark_id: str, current=Depends(get_current_user)):
    return bookmark_tag_service.list_tags_for_bookmark(_uid(current), bookmark_id)


@router.get("/tag/{tag_id}")
def list_bookmarks(tag_id: str, current=Depends(get_current_user)):
    return bookmark_tag_service.list_bookmarks_for_tag(_uid(current), tag_id)
