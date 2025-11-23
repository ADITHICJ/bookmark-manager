from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Import your routers
# from api.routes import public, bookmarks

# (Optional) Import DB initialization
# from db.base import create_all

app = FastAPI(
    title="Bookmark Manager API",
    version="1.0.0"
)

# -------------------------------
# 🚀 CORS Setup (Very Important)
# -------------------------------

origins = [
    "http://localhost:3000",     # Next.js local dev
    "http://127.0.0.1:3000",
    # Add your frontend production domain here:
    # "https://your-frontend.vercel.app",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,          # Only allow your frontend
    allow_credentials=True,
    allow_methods=["*"],            # GET, POST, PUT, DELETE
    allow_headers=["*"],            # Authorization, Content-Type
)

# -------------------------------
# 🚀 Include Routers
# -------------------------------

# app.include_router(public.router)
# app.include_router(bookmarks.router)


# -------------------------------
# 🏠 Root Route
# -------------------------------

@app.get("/")
def root():
    return {"message": "Bookmark Manager API is running"}
