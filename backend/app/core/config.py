import os
from functools import lru_cache
from pydantic import BaseModel


class Settings(BaseModel):
    # Supabase
    SUPABASE_URL: str = os.getenv("SUPABASE_URL", "")
    SUPABASE_SERVICE_ROLE_KEY: str = os.getenv("SUPABASE_SERVICE_ROLE_KEY", "")

    # Clerk
    CLERK_ISSUER: str = os.getenv(
        "CLERK_ISSUER",
        "https://amazed-duck-99.clerk.accounts.dev",  # your instance
    )
    CLERK_JWKS_URL: str = os.getenv(
        "CLERK_JWKS_URL",
        "https://amazed-duck-99.clerk.accounts.dev/.well-known/jwks.json",
    )

    # CORS – add your frontend URL here
    FRONTEND_URL: str = os.getenv("FRONTEND_URL", "http://localhost:3000")

    @property
    def BACKEND_CORS_ORIGINS(self) -> list[str]:
        # You can extend this later
        return [self.FRONTEND_URL]


@lru_cache
def get_settings() -> Settings:
    return Settings()


settings = get_settings()
