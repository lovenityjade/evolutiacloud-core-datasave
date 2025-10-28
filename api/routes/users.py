from fastapi import APIRouter
from api.utils.db import get_db

router = APIRouter()

@router.get("/")
def list_users():
    db = get_db()
    users = db.execute("SELECT username, permissions, patreontier FROM `CloudSave-users`").fetchall()
    return {"users": [dict(u) for u in users]}
