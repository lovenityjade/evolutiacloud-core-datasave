# api/routes/auth.py
"""
Authentication handling for EvolutiaCloud DataSave
Endpoints:
- /auth/register : register a new user (prototype)
- /auth/login    : login and receive JWT token (prototype)
"""

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import jwt

# Import your config dictionary from api/config.py
from api.config import config

# FastAPI router
router = APIRouter()

# ---------- Pydantic models ----------
class UserRegister(BaseModel):
    username: str
    email: str
    password: str

class UserLogin(BaseModel):
    username: str
    password: str

# ---------- Endpoints ----------
@router.post("/register")
async def register_user(user: UserRegister):
    """
    Prototype user registration.
    Currently just returns a success message.
    """
    return {"message": f"User {user.username} registered successfully"}

@router.post("/login")
async def login(user: UserLogin):
    """
    Prototype login:
    Checks a hardcoded username/password and returns a JWT token.
    """
    # Hardcoded admin credentials for prototype
    if user.username == "CHANGE" and user.password == "CHANGE":
        token = jwt.encode(
            {"user": user.username},
            config["api"]["jwt_secret"],
            algorithm="HS256"
        )
        return {"token": token}

    # Invalid credentials
    raise HTTPException(status_code=401, detail="Invalid credentials")
