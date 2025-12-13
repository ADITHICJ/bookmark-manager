from typing import List
from app.core.supabase_client import get_supabase_client
from app.schemas.bookmark_tag import BookmarkTagCreate

BOOKMARK_TABLE = "bookmarks"
TAG_TABLE = "tags"
BOOKMARK_TAG_TABLE = "bookmark_tags"


def add_tag_to_bookmark(user_id: str, data: BookmarkTagCreate) -> dict:
    supabase = get_supabase_client()

    # Verify bookmark ownership
    bm = (
        supabase.table(BOOKMARK_TABLE)
        .select("id")
        .eq("id", data.bookmark_id)
        .eq("user_id", user_id)
        .single()
        .execute()
    )
    if not bm.data:
        raise ValueError("Bookmark not found")

    # Verify tag ownership
    tg = (
        supabase.table(TAG_TABLE)
        .select("id")
        .eq("id", data.tag_id)
        .eq("user_id", user_id)
        .single()
        .execute()
    )
    if not tg.data:
        raise ValueError("Tag not found")

    # Insert mapping
    res = (
        supabase.table(BOOKMARK_TAG_TABLE)
        .insert({
            "bookmark_id": data.bookmark_id,
            "tag_id": data.tag_id
        })
        .execute()
    )

    return res.data[0]


def remove_tag_from_bookmark(user_id: str, bookmark_id: str, tag_id: str) -> bool:
    supabase = get_supabase_client()

    # Verify bookmark ownership
    bm = (
        supabase.table(BOOKMARK_TABLE)
        .select("id")
        .eq("id", bookmark_id)
        .eq("user_id", user_id)
        .single()
        .execute()
    )
    if not bm.data:
        raise ValueError("Bookmark not found")

    supabase.table(BOOKMARK_TAG_TABLE) \
        .delete() \
        .eq("bookmark_id", bookmark_id) \
        .eq("tag_id", tag_id) \
        .execute()

    return True


def list_tags_for_bookmark(user_id: str, bookmark_id: str) -> List[dict]:
    supabase = get_supabase_client()

    # Verify bookmark ownership
    bm = (
        supabase.table(BOOKMARK_TABLE)
        .select("id")
        .eq("id", bookmark_id)
        .eq("user_id", user_id)
        .single()
        .execute()
    )
    if not bm.data:
        raise ValueError("Bookmark not found")

    res = (
        supabase.table(BOOKMARK_TAG_TABLE)
        .select("tags(*)")
        .eq("bookmark_id", bookmark_id)
        .execute()
    )

    return res.data or []


def list_bookmarks_for_tag(user_id: str, tag_id: str) -> List[dict]:
    supabase = get_supabase_client()

    # Verify tag ownership
    tg = (
        supabase.table(TAG_TABLE)
        .select("id")
        .eq("id", tag_id)
        .eq("user_id", user_id)
        .single()
        .execute()
    )
    if not tg.data:
        raise ValueError("Tag not found")

    res = (
        supabase.table(BOOKMARK_TAG_TABLE)
        .select("bookmarks(*)")
        .eq("tag_id", tag_id)
        .execute()
    )

    return res.data or []
