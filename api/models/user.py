# api/models/user.py - User model helpers (PyMySQL version)
from api.utils.db import get_db
from api.utils.hashing import hash_password, verify_password  # à créer pour sécurité

def create_user(username: str, email: str, password: str):
    conn = get_db()
    hashed_pw = hash_password(password)
    with conn.cursor() as cursor:
        cursor.execute(
            "INSERT INTO users (username, email, password) VALUES (%s, %s, %s)",
            (username, email, hashed_pw)
        )
    return {"username": username, "email": email}

def get_user_by_username(username: str):
    conn = get_db()
    with conn.cursor() as cursor:
        cursor.execute("SELECT * FROM users WHERE username=%s", (username,))
        return cursor.fetchone()
