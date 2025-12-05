from typing import List, Optional
import uuid
from datetime import datetime
from app.core.supabase_client import get_supabase_client
from app.schemas.bookmark import BookmarkCreate, BookmarkUpdate


TABLE_NAME = "Bookmark"


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
    "id": str(uuid.uuid4()),
    "user_id": user_id,
    "title": data.title,
    "url": str(data.url),
    "description": data.description,
    "created_at": datetime.utcnow().isoformat(),   # 🔥 FIX
    }

    res = supabase.table(TABLE_NAME).insert(payload).execute()
    return res.data[0]  # Supabase returns list of rows


def update_bookmark(user_id: str, bookmark_id: str, data: BookmarkUpdate) -> Optional[dict]:
    supabase = get_supabase_client()
    update_data = data.model_dump(exclude_unset=True)
    if "url" in update_data:
        update_data["url"] = str(update_data["url"])


    if not update_data:
        return get_bookmark(user_id, bookmark_id)

    res = (
    supabase.table(TABLE_NAME)
    .update(update_data)
    .eq("user_id", user_id)
    .eq("id", bookmark_id)
    .execute()
    )

    return res.data[0] if res.data else None


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
