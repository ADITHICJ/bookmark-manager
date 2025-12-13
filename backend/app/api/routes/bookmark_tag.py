from fastapi import APIRouter, Depends, HTTPException, status
from app.api.deps import get_current_user
from app.schemas.bookmark_tag import BookmarkTagCreate
from app.services import bookmark_tag_service

router = APIRouter(prefix="/bookmark-tags", tags=["bookmark-tags"])


def _get_user_id(user: dict) -> str:
    uid = user.get("sub") or user.get("id")
    if not uid:
        raise HTTPException(status_code=400, detail="Invalid user token")
    return uid


@router.post("/", status_code=status.HTTP_201_CREATED)
def add_tag(
    data: BookmarkTagCreate,
    current=Depends(get_current_user),
):
    try:
        return bookmark_tag_service.add_tag_to_bookmark(
            _get_user_id(current), data
        )
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.delete("/", status_code=status.HTTP_204_NO_CONTENT)
def remove_tag(
    bookmark_id: str,
    tag_id: str,
    current=Depends(get_current_user),
):
    try:
        bookmark_tag_service.remove_tag_from_bookmark(
            _get_user_id(current),
            bookmark_id,
            tag_id,
        )
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    return


@router.get("/bookmark/{bookmark_id}")
def list_tags(
    bookmark_id: str,
    current=Depends(get_current_user),
):
    try:
        return bookmark_tag_service.list_tags_for_bookmark(
            _get_user_id(current),
            bookmark_id,
        )
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.get("/tag/{tag_id}")
def list_bookmarks(
    tag_id: str,
    current=Depends(get_current_user),
):
    try:
        return bookmark_tag_service.list_bookmarks_for_tag(
            _get_user_id(current),
            tag_id,
        )
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
