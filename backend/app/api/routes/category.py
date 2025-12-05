from fastapi import APIRouter, Depends, HTTPException, status
from typing import List

from app.api.deps import get_current_user
from app.schemas.category import Category, CategoryCreate
from app.services import category_service

router = APIRouter(prefix="/categories", tags=["categories"])


def _uid(u): return u.get("sub") or u.get("id")


@router.get("/", response_model=List[Category])
def list_categories(current=Depends(get_current_user)):
    return category_service.list_categories(_uid(current))


@router.post("/", response_model=Category, status_code=201)
def create_category(data: CategoryCreate, current=Depends(get_current_user)):
    return category_service.create_category(_uid(current), data)


@router.delete("/{category_id}", status_code=204)
def delete_category(category_id: str, current=Depends(get_current_user)):
    ok = category_service.delete_category(_uid(current), category_id)
    if not ok:
        raise HTTPException(404, "Category not found")
    return
