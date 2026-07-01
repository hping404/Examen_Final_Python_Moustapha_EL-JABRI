import os
from fastapi import Header, HTTPException, status
from typing import Optional

API_KEY = os.getenv("API_KEY")


def verify_api_key(x_api_key: Optional[str] = Header(None)):
    if API_KEY is None:
        raise HTTPException(status_code=500, detail="API_KEY not set")

    if x_api_key != API_KEY:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Invalid or missing API key",
        )
