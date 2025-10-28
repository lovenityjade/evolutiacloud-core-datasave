# auth.py - Authentication handling (login, JWT token)
from fastapi import APIRouter, HTTPException
import jwt
import config

# Create FastAPI router for auth
router = APIRouter()

# Prototype login endpoint
@router.post("/login")
def login(username: str, password: str):
    """
    Prototype login: checks a temporary username/password
    Returns a JWT token if credentials are correct
    """
    # For now, only admin is hardcoded
    if username == "CHANGE" and password == "CHANGE":
        # Create a simple JWT token
        token = jwt.encode(
            {"user": username},
            config["api"]["jwt_secret"],
            algorithm="HS256"
        )
        return {"token": token}
    
    # Return error if credentials are invalid
    raise HTTPException(status_code=401, detail="Invalid credentials")
