from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel
import jwt
from api.utils.db import get_db
from api.models.user import User
from api.utils import security
import config

router = APIRouter()

class UserRegister(BaseModel):
    username: str
    email: str
    password: str

class UserLogin(BaseModel):
    username: str
    password: str

# ---------------- Register ----------------
@router.post("/register")
def register_user(user: UserRegister, db: Session = Depends(get_db)):
    # Vérifier si l'utilisateur existe déjà
    if db.query(User).filter(User.username == user.username).first():
        raise HTTPException(status_code=409, detail="Username already taken")
    if db.query(User).filter(User.email == user.email).first():
        raise HTTPException(status_code=409, detail="Email already registered")
    
    # Hacher le mot de passe
    hashed_pw = security.hash_password(user.password)
    
    # Créer l'utilisateur
    db_user = User(username=user.username, email=user.email, hashed_password=hashed_pw)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    
    return {"message": f"User {user.username} registered successfully"}

# ---------------- Login ----------------
@router.post("/login")
def login(user: UserLogin, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.username == user.username).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    
    if not security.verify_password(user.password, db_user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    
    # Générer JWT
    token = jwt.encode(
        {"user": db_user.username},
        config.JWT_SECRET,
        algorithm="HS256"
    )
    return {"token": token}
