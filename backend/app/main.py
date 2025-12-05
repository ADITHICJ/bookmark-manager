from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.routes import public, bookmarks
from app.api.routes.category import router as category_router
from app.api.routes.tag import router as tag_router
from app.api.routes.bookmark_tag import router as bookmark_tag_router
from app.core.config import settings

app = FastAPI(title="Bookmark Manager API")

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.BACKEND_CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routers
app.include_router(public.router)
app.include_router(bookmarks.router, prefix="/api")  # /api/bookmarks/...
app.include_router(category_router, prefix="/api")
app.include_router(tag_router, prefix="/api")
app.include_router(bookmark_tag_router, prefix="/api")

@app.get("/health", tags=["health"])
def health_check():
    return {"status": "ok"}
