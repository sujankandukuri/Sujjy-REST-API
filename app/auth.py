from fastapi import Header, HTTPException


API_KEY = "sujjy123"


def verify_api_key(x_api_key: str = Header(None)):
    if x_api_key != API_KEY:
        raise HTTPException(
            status_code=401,
            detail="Invalid or missing API key"
        )

    return True