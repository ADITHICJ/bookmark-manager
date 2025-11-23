from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.routes import public, bookmarks
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


@app.get("/health", tags=["health"])
def health_check():
    return {"status": "ok"}
