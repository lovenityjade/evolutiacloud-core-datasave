# users.py - User management
from fastapi import APIRouter
import get_db

router = APIRouter()

@router.get("/")
def list_users():
    """
    Returns the list of users with permissions and Patreon tier
    """
    db = get_db()  # Connect to database
    # Select basic information for prototype
    users = db.execute(
        "SELECT username, permissions, patreontier FROM `CloudSave-users`"
    ).fetchall()
    
    # Convert to list of dictionaries for JSON response
    return {"users": [dict(u) for u in users]}
