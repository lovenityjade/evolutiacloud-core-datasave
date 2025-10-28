from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import jwt
import config
from api.models.user import get_user_by_username, create_user
from api.utils.hashing import verify_password

router = APIRouter()

class UserRegister(BaseModel):
    username: str
    email: str
    password: str

class UserLogin(BaseModel):
    username: str
    password: str

# Register endpoint
@router.post("/register")
def register_user(user: UserRegister):
    existing_user = get_user_by_username(user.username)
    if existing_user:
        raise HTTPException(status_code=400, detail="Username already exists")
    created = create_user(user.username, user.email, user.password)
    return {"message": f"User {created['username']} registered successfully"}

# Login endpoint
@router.post("/login")
def login(user: UserLogin):
    db_user = get_user_by_username(user.username)
    if not db_user or not verify_password(user.password, db_user["password"]):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    
    token = jwt.encode(
        {"user": user.username},
        config["api"]["jwt_secret"],
        algorithm="HS256"
    )
    return {"token": token}
