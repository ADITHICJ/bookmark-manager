from fastapi import APIRouter

router = APIRouter(prefix="/public", tags=["Public"])

@router.get("/health")
def health():
    return {"status": "ok"}
