from functools import lru_cache

import requests
from fastapi import HTTPException, status
from jose import jwt, JWTError  # python-jose

from app.core.config import settings


@lru_cache
def _get_jwks():
    """Fetch JWKS from Clerk (cached in memory)."""
    resp = requests.get(settings.CLERK_JWKS_URL, timeout=5)
    resp.raise_for_status()
    return resp.json()


def _get_key_for_token(token: str):
    unverified_header = jwt.get_unverified_header(token)
    kid = unverified_header.get("kid")

    jwks = _get_jwks()
    for key in jwks.get("keys", []):
        if key.get("kid") == kid:
            return key

    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Unable to find matching JWKS key",
    )


def verify_clerk_token(token: str) -> dict:
    """
    Validate a Clerk-issued JWT and return its payload.
    """
    key = _get_key_for_token(token)

    try:
        payload = jwt.decode(
            token,
            key,
            algorithms=["RS256"],
            issuer=settings.CLERK_ISSUER,
            options={"verify_aud": False},  # disable audience check for now
        )
        return payload
    except JWTError as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=f"Invalid authentication credentials: {str(e)}",
        )
