from fastapi import APIRouter, HTTPException, Depends
from api.utils.db import get_db
import jwt
from api.config import config

router = APIRouter()

# Temporary prototype login route
@router.post("/login")
def login(username: str, password: str):
    # TODO: Replace with proper password check
    if username == "admin" and password == "A3e5t122!":
        token = jwt.encode({"user": username}, config["api"]["jwt_secret"], algorithm="HS256")
        return {"token": token}
    raise HTTPException(status_code=401, detail="Invalid credentials")
