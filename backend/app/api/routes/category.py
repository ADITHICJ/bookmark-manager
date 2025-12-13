from fastapi import APIRouter, Depends, HTTPException, status
from typing import List

from app.api.deps import get_current_user
from app.schemas.category import Category, CategoryCreate
from app.services import category_service

router = APIRouter(prefix="/categories", tags=["categories"])


def _get_user_id(user: dict) -> str:
    uid = user.get("sub") or user.get("id")
    if not uid:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid user token",
        )
    return uid


@router.get("/", response_model=List[Category])
def list_categories(current=Depends(get_current_user)):
    return category_service.list_categories(_get_user_id(current))


@router.post("/", response_model=Category, status_code=status.HTTP_201_CREATED)
def create_category(data: CategoryCreate, current=Depends(get_current_user)):
    return category_service.create_category(_get_user_id(current), data)


@router.delete("/{category_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_category(category_id: str, current=Depends(get_current_user)):
    ok = category_service.delete_category(_get_user_id(current), category_id)
    if not ok:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Category not found",
        )
    return
