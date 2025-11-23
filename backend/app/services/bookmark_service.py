from app.core.supabase_client import supabase
from app.schemas.bookmark import BookmarkCreate, BookmarkUpdate


def create_bookmark(data: BookmarkCreate, user_id: str):
    response = (
        supabase.table("bookmarks")
        .insert({
            "title": data.title,
            "url": data.url,
            "tag": data.tag,
            "user_id": user_id,
        })
        .execute()
    )
    return response.data[0] if response.data else None


def list_bookmarks(user_id: str):
    response = (
        supabase.table("bookmarks")
        .select("*")
        .eq("user_id", user_id)
        .order("created_at", desc=True)
        .execute()
    )
    return response.data or []


def get_bookmark_by_id(bookmark_id: int, user_id: str):
    response = (
        supabase.table("bookmarks")
        .select("*")
        .eq("id", bookmark_id)
        .eq("user_id", user_id)
        .single()
        .execute()
    )
    return response.data


def update_bookmark(bookmark_id: int, data: BookmarkUpdate, user_id: str):
    update_data = {k: v for k, v in data.dict().items() if v is not None}

    response = (
        supabase.table("bookmarks")
        .update(update_data)
        .eq("id", bookmark_id)
        .eq("user_id", user_id)
        .execute()
    )

    return response.data[0] if response.data else None


def delete_bookmark(bookmark_id: int, user_id: str):
    response = (
        supabase.table("bookmarks")
        .delete()
        .eq("id", bookmark_id)
        .eq("user_id", user_id)
        .execute()
    )

    return bool(response.data)
