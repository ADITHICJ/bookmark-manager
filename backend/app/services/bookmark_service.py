from typing import List, Optional
import uuid
from datetime import datetime

from app.core.supabase_client import get_supabase_client
from app.schemas.bookmark import BookmarkCreate, BookmarkUpdate

BOOKMARK_TABLE = "bookmarks"
BOOKMARK_TAG_TABLE = "bookmark_tags"


# ---------- helpers ----------
def _normalize_bookmark(bookmark: dict) -> dict:
    bookmark["tag_ids"] = [
        bt["tag_id"] for bt in bookmark.get("bookmark_tags", [])
    ]
    bookmark.pop("bookmark_tags", None)
    return bookmark


# ---------- queries ----------
def list_bookmarks(user_id: str) -> List[dict]:
    supabase = get_supabase_client()

    res = (
        supabase.table(BOOKMARK_TABLE)
        .select(
            """
            *,
            bookmark_tags (
                tag_id
            )
            """
        )
        .eq("user_id", user_id)
        .order("created_at", desc=True)
        .execute()
    )

    return [_normalize_bookmark(b) for b in (res.data or [])]


def get_bookmark(user_id: str, bookmark_id: str) -> Optional[dict]:
    supabase = get_supabase_client()

    res = (
        supabase.table(BOOKMARK_TABLE)
        .select(
            """
            *,
            bookmark_tags (
                tag_id
            )
            """
        )
        .eq("user_id", user_id)
        .eq("id", bookmark_id)
        .single()
        .execute()
    )

    return _normalize_bookmark(res.data) if res.data else None


def create_bookmark(user_id: str, data: BookmarkCreate) -> dict:
    supabase = get_supabase_client()

    bookmark_id = str(uuid.uuid4())

    bookmark_payload = {
        "id": bookmark_id,
        "user_id": user_id,
        "title": data.title,
        "url": str(data.url),
        "description": data.description,
        "category_id": data.category_id,
        "created_at": datetime.utcnow().isoformat(),
    }

    res = supabase.table(BOOKMARK_TABLE).insert(bookmark_payload).execute()
    bookmark = res.data[0]

    if data.tag_ids:
        tag_rows = [
            {"bookmark_id": bookmark_id, "tag_id": tag_id}
            for tag_id in data.tag_ids
        ]
        supabase.table(BOOKMARK_TAG_TABLE).insert(tag_rows).execute()

    return _normalize_bookmark(bookmark)


def update_bookmark(
    user_id: str,
    bookmark_id: str,
    data: BookmarkUpdate,
) -> Optional[dict]:
    supabase = get_supabase_client()

    update_data = data.model_dump(
        exclude_unset=True,
        exclude={"tag_ids"},
    )

    if "url" in update_data:
        update_data["url"] = str(update_data["url"])

    if update_data:
        supabase.table(BOOKMARK_TABLE) \
            .update(update_data) \
            .eq("id", bookmark_id) \
            .eq("user_id", user_id) \
            .execute()

    if data.tag_ids is not None:
        supabase.table(BOOKMARK_TAG_TABLE) \
            .delete() \
            .eq("bookmark_id", bookmark_id) \
            .execute()

        if data.tag_ids:
            tag_rows = [
                {"bookmark_id": bookmark_id, "tag_id": tag_id}
                for tag_id in data.tag_ids
            ]
            supabase.table(BOOKMARK_TAG_TABLE).insert(tag_rows).execute()

    return get_bookmark(user_id, bookmark_id)


def delete_bookmark(user_id: str, bookmark_id: str) -> bool:
    supabase = get_supabase_client()

    supabase.table(BOOKMARK_TABLE) \
        .delete() \
        .eq("id", bookmark_id) \
        .eq("user_id", user_id) \
        .execute()

    return True
