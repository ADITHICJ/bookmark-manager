from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    SUPABASE_URL: str
    SUPABASE_SERVICE_ROLE_KEY: str
    CLERK_JWKS_URL: str  # NEW

    class Config:
        env_file = ".env"

settings = Settings()
