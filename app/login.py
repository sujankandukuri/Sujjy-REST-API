from fastapi import APIRouter, HTTPException
from jose import jwt

router = APIRouter()

SECRET_KEY = "sujjy-secret-key"
ALGORITHM = "HS256"

users = {
    "sujan": "1234"
}


@router.post("/login")
def login(username: str, password: str):

    if username not in users or users[username] != password:
        raise HTTPException(
            status_code=401,
            detail="Invalid username or password"
        )

    token = jwt.encode(
        {"sub": username},
        SECRET_KEY,
        algorithm=ALGORITHM
    )

    return {
        "access_token": token,
        "token_type": "bearer"
    }