from fastapi import Header, HTTPException
from app.core.clerk import verify_clerk_token

def get_current_user(
    authorization: str = Header(default=None, alias="Authorization"),
    authorization_alt: str = Header(default=None, alias="authorization")
):
    """
    Extracts and validates the Clerk JWT from the Authorization header.

    Supports both:
    - "Authorization"
    - "authorization"
    (Swagger UI sends lowercase)
    """

    token_header = authorization or authorization_alt

    if not token_header:
        raise HTTPException(status_code=401, detail="Missing Authorization header")

    if not token_header.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Invalid token format. Expected 'Bearer <token>'")

    token = token_header.replace("Bearer ", "")
    
    # Validate Clerk token using JWKS
    user = verify_clerk_token(token)

    return user  # contains user["sub"]
