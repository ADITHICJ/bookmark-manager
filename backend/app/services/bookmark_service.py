from typing import List, Optional

from app.core.supabase_client import get_supabase_client
from app.schemas.bookmark import BookmarkCreate, BookmarkUpdate


TABLE_NAME = "bookmarks"


# Optional: SQL for your Supabase table (run once in SQL editor)
"""
create table if not exists public.bookmarks (
  id uuid primary key default gen_random_uuid(),
  user_id text not null,
  title text not null,
  url text not null,
  description text,
  created_at timestamptz not null default now()
);
"""


def list_bookmarks(user_id: str) -> List[dict]:
    supabase = get_supabase_client()
    res = (
        supabase.table(TABLE_NAME)
        .select("*")
        .eq("user_id", user_id)
        .order("created_at", desc=True)
        .execute()
    )
    return res.data or []


def get_bookmark(user_id: str, bookmark_id: str) -> Optional[dict]:
    supabase = get_supabase_client()
    res = (
        supabase.table(TABLE_NAME)
        .select("*")
        .eq("user_id", user_id)
        .eq("id", bookmark_id)
        .single()
        .execute()
    )
    return res.data


def create_bookmark(user_id: str, data: BookmarkCreate) -> dict:
    supabase = get_supabase_client()
    payload = {
        "user_id": user_id,
        "title": data.title,
        "url": str(data.url),
        "description": data.description,
    }
    res = supabase.table(TABLE_NAME).insert(payload).select("*").single().execute()
    return res.data


def update_bookmark(user_id: str, bookmark_id: str, data: BookmarkUpdate) -> Optional[dict]:
    supabase = get_supabase_client()
    update_data = {k: v for k, v in data.model_dump(exclude_unset=True).items()}

    if not update_data:
        return get_bookmark(user_id, bookmark_id)

    res = (
        supabase.table(TABLE_NAME)
        .update(update_data)
        .eq("user_id", user_id)
        .eq("id", bookmark_id)
        .select("*")
        .single()
        .execute()
    )
    return res.data


def delete_bookmark(user_id: str, bookmark_id: str) -> bool:
    supabase = get_supabase_client()
    res = (
        supabase.table(TABLE_NAME)
        .delete()
        .eq("user_id", user_id)
        .eq("id", bookmark_id)
        .execute()
    )
    # if no error and something was deleted, treat as success
    return True
