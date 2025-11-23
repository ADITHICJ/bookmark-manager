from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import APIKeyHeader
from fastapi.openapi.utils import get_openapi

from app.api.routes import public, bookmarks

app = FastAPI(
    title="Bookmark Manager API",
    version="1.0.0",
)

# --- SECURITY SCHEME (Enables Swagger Authorize Button) ---
api_key_header = APIKeyHeader(
    name="Authorization",
    description="Enter your token as: Bearer <JWT>",
)


# --- CORS SETUP ---
origins = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# --- ROUTES ---
app.include_router(public.router)
app.include_router(bookmarks.router)


@app.get("/")
def root():
    return {"status": "ok", "message": "FastAPI + Supabase backend running!"}


# --- CUSTOM OPENAPI (Adds Security to Docs) ---
def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema

    openapi_schema = get_openapi(
        title="Bookmark Manager API",
        version="1.0.0",
        routes=app.routes,
    )

    # Add security scheme so Swagger shows "Authorize" button
    openapi_schema["components"]["securitySchemes"] = {
        "BearerAuth": {
            "type": "apiKey",
            "in": "header",
            "name": "Authorization",
        }
    }

    # Apply security to all routes starting with /bookmarks
    for path in openapi_schema["paths"]:
        if path.startswith("/bookmarks"):
            for method in openapi_schema["paths"][path]:
                openapi_schema["paths"][path][method]["security"] = [
                    {"BearerAuth": []}
                ]

    app.openapi_schema = openapi_schema
    return app.openapi_schema


app.openapi = custom_openapi
