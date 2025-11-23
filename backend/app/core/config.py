import os
from functools import lru_cache
from pydantic import BaseModel
from dotenv import load_dotenv

# Load .env
load_dotenv()

class Settings(BaseModel):
    SUPABASE_URL: str = os.getenv("SUPABASE_URL")
    SUPABASE_SERVICE_ROLE_KEY: str = os.getenv("SUPABASE_SERVICE_ROLE_KEY")

    CLERK_ISSUER: str = os.getenv("CLERK_ISSUER")
    CLERK_JWKS_URL: str = os.getenv("CLERK_JWKS_URL")

    FRONTEND_URL: str = os.getenv("FRONTEND_URL", "http://localhost:3000")

    @property
    def BACKEND_CORS_ORIGINS(self) -> list[str]:
        return [self.FRONTEND_URL]


@lru_cache
def get_settings() -> Settings:
    return Settings()


settings = get_settings()
