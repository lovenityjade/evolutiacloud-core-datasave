# auth.py - Authentication handling (login, JWT token)
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import jwt
import config  # Assure-toi que config.py est correct et accessible

# Pydantic models
class UserRegister(BaseModel):
    username: str
    email: str
    password: str

class UserLogin(BaseModel):
    username: str
    password: str

# Create FastAPI router for auth
router = APIRouter()

# Prototype login endpoint
@router.post("/login")
async def login(user: UserLogin):
    """
    Prototype login: checks a temporary username/password
    Returns a JWT token if credentials are correct
    """
    # For now, only admin is hardcoded
    if user.username == "CHANGE" and user.password == "CHANGE":
        # Create a simple JWT token
        token = jwt.encode(
            {"user": user.username},
            config.api["jwt_secret"],
            algorithm="HS256"
        )
        return {"token": token}
    
    # Return error if credentials are invalid
    raise HTTPException(status_code=401, detail="Invalid credentials")

# Prototype register endpoint
@router.post("/register")
async def register_user(user: UserRegister):
    # For now, just a dummy response
    return {"message": f"User {user.username} registered successfully"}
