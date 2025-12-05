from typing import List, Optional
import uuid
from app.core.supabase_client import get_supabase_client
from app.schemas.tag import TagCreate

TABLE = "Tag"


def list_tags(user_id: str) -> List[dict]:
    supabase = get_supabase_client()
    res = supabase.table(TABLE).select("*").eq("user_id", user_id).execute()
    return res.data or []


def get_tag(user_id: str, tag_id: str) -> Optional[dict]:
    supabase = get_supabase_client()
    res = supabase.table(TABLE).select("*").eq("user_id", user_id).eq("tag_id", tag_id).single().execute()
    return res.data


def create_tag(user_id: str, data: TagCreate) -> dict:
    supabase = get_supabase_client()
    payload = {
    "tag_id": str(uuid.uuid4()),   # ← Generate UUID for tag primary key
    "user_id": user_id,
    "tag_name": data.tag_name,
    }
    res = supabase.table(TABLE).insert(payload).execute()
    return res.data[0]


def delete_tag(user_id: str, tag_id: str) -> bool:
    supabase = get_supabase_client()
    res = supabase.table(TABLE).delete().eq("user_id", user_id).eq("tag_id", tag_id).execute()
    return True
