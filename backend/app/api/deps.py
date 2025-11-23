from fastapi import Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

from app.core.clerk import verify_clerk_token

auth_scheme = HTTPBearer(auto_error=True)


def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(auth_scheme),
) -> dict:
    """
    Dependency that validates the Authorization: Bearer <token> header
    and returns the Clerk JWT payload.
    """
    token = credentials.credentials
    payload = verify_clerk_token(token)
    return payload
