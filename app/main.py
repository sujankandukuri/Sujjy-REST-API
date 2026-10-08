from fastapi import FastAPI, Request
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded

from app.routes import students
from app import login


# Rate limiter
limiter = Limiter(key_func=get_remote_address)


# Create FastAPI app
app = FastAPI(
    title="Sujjy Student Management API",
    description="Production-ready REST API project",
    version="1.0.0"
)


# Configure rate limiting
app.state.limiter = limiter

app.add_exception_handler(
    RateLimitExceeded,
    _rate_limit_exceeded_handler
)


# Home endpoint
@app.get("/")
@limiter.limit("5/minute")
def home(request: Request):
    return {
        "message": "Sujjy REST API is running"
    }


# Student API - Version 1
app.include_router(
    students.router,
    prefix="/api/v1/students",
    tags=["Students"]
)


# Login / JWT authentication
app.include_router(
    login.router,
    prefix="/auth",
    tags=["Authentication"]
)