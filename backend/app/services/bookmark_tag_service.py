from typing import List
from app.core.supabase_client import get_supabase_client
from app.schemas.bookmark_tag import BookmarkTagCreate

TABLE = "bookmark_tag"


def add_tag_to_bookmark(user_id: str, data: BookmarkTagCreate) -> dict:
    supabase = get_supabase_client()

    # Verify user owns the bookmark
    bm = (
        supabase.table("Bookmark")
        .select("*")
        .eq("id", data.bookmark_id)
        .eq("user_id", user_id)
        .single()
        .execute()
    )
    if bm is None or bm.data is None:
        raise Exception("Bookmark not found")

    # Verify user owns the tag
    tg = (
        supabase.table("Tag")
        .select("*")
        .eq("tag_id", data.tag_id)
        .eq("user_id", user_id)
        .maybe_single()
        .execute()
    )
    if tg is None or tg.data is None:
        raise Exception("Tag not found")

    res = supabase.table(TABLE).insert(data.model_dump()).execute()
    return res.data[0]


def remove_tag_from_bookmark(user_id: str, bookmark_id: str, tag_id: str) -> bool:
    supabase = get_supabase_client()
    supabase.table(TABLE).delete().eq("bookmark_id", bookmark_id).eq("tag_id", tag_id).execute()
    return True


def list_tags_for_bookmark(user_id: str, bookmark_id: str) -> List[dict]:
    supabase = get_supabase_client()
    return (
        supabase.table("bookmark_tag")
        .select("*, Tag(*)")
        .eq("bookmark_id", bookmark_id)
        .execute()
        .data
        or []
    )


def list_bookmarks_for_tag(user_id: str, tag_id: str) -> List[dict]:
    supabase = get_supabase_client()
    return (
        supabase.table(TABLE)
        .select("Bookmark:Bookmark(*)")
        .eq("tag_id", tag_id)
        .execute()
        .data
        or []
    )
