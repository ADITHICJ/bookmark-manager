import requests
from jose import jwt
from fastapi import HTTPException, status
from functools import lru_cache

# Your Clerk JWKS URL
JWKS_URL = "https://amazed-duck-99.clerk.accounts.dev/.well-known/jwks.json"


# Cache the JWKS for performance
@lru_cache()
def get_jwks():
    response = requests.get(JWKS_URL)
    if response.status_code != 200:
        raise HTTPException(status_code=500, detail="Failed to fetch JWKS keys")
    return response.json()


def verify_clerk_token(token: str):
    """
    Verifies a Clerk JWT using JWKS (automatic key rotation).
    """

    jwks = get_jwks()

    # Decode headers to find which keyId ("kid") was used
    try:
        header = jwt.get_unverified_header(token)
    except Exception:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token header")

    kid = header.get("kid", None)
    if not kid:
        raise HTTPException(status_code=401, detail="Token missing 'kid' header")

    # Find matching JWKS key
    key = None
    for jwk in jwks["keys"]:
        if jwk["kid"] == kid:
            key = jwk
            break

    if not key:
        raise HTTPException(status_code=401, detail="Matching JWKS key not found")

    # Verify token using jose + JWKS key
    try:
        payload = jwt.decode(
            token,
            key,
            algorithms=[key["alg"]],
            options={"verify_aud": False},  # Clerk tokens don't require audience matching here
        )
        return payload  # contains user["sub"]
    except Exception as e:
        raise HTTPException(status_code=401, detail="Invalid or expired token")
