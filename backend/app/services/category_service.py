from typing import List, Optional
from app.core.supabase_client import get_supabase_client
from app.schemas.category import CategoryCreate
import uuid

TABLE = "Category"


def list_categories(user_id: str) -> List[dict]:
    supabase = get_supabase_client()
    res = supabase.table(TABLE).select("*").eq("user_id", user_id).order("created_at", desc=True).execute()
    return res.data or []


def get_category(user_id: str, category_id: str) -> Optional[dict]:
    supabase = get_supabase_client()
    res = supabase.table(TABLE).select("*").eq("user_id", user_id).eq("category_id", category_id).single().execute()
    return res.data


def create_category(user_id: str, data: CategoryCreate) -> dict:
    supabase = get_supabase_client()
    payload = {
    "category_id": str(uuid.uuid4()),   # ← generate UUID manually
    "user_id": user_id,
    "name": data.name,
    }
    res = supabase.table(TABLE).insert(payload).execute()
    return res.data[0]


def delete_category(user_id: str, category_id: str) -> bool:
    supabase = get_supabase_client()
    res = supabase.table(TABLE).delete().eq("user_id", user_id).eq("category_id", category_id).execute()
    return True
