from typing import List, Optional
import uuid
from datetime import datetime

from app.core.supabase_client import get_supabase_client
from app.schemas.tag import TagCreate

TABLE = "tags"


def list_tags(user_id: str) -> List[dict]:
    supabase = get_supabase_client()
    res = (
        supabase.table(TABLE)
        .select("*")
        .eq("user_id", user_id)
        .order("created_at", desc=True)
        .execute()
    )
    return res.data or []


def get_tag(user_id: str, tag_id: str) -> Optional[dict]:
    supabase = get_supabase_client()
    res = (
        supabase.table(TABLE)
        .select("*")
        .eq("id", tag_id)
        .eq("user_id", user_id)
        .single()
        .execute()
    )
    return res.data


def create_tag(user_id: str, data: TagCreate) -> dict:
    supabase = get_supabase_client()

    payload = {
        "id": str(uuid.uuid4()),
        "user_id": user_id,
        "name": data.name,
        "color": data.color,
        "created_at": datetime.utcnow().isoformat(),
    }

    res = supabase.table(TABLE).insert(payload).execute()
    return res.data[0]


def delete_tag(user_id: str, tag_id: str) -> bool:
    supabase = get_supabase_client()

    res = (
        supabase.table(TABLE)
        .delete()
        .eq("id", tag_id)
        .eq("user_id", user_id)
        .execute()
    )

    return bool(res.data)
