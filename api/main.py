# api/main.py
"""
Main entrypoint for EvolutiaCloud DataSave API
Starts FastAPI app and includes all routers
"""

from fastapi import FastAPI
from api.routes import auth  # include auth routes

app = FastAPI(title="EvolutiaCloud DataSave API")

# Include auth router with /auth prefix
app.include_router(auth.router, prefix="/auth", tags=["Authentication"])

# ---------- Root endpoint ----------
@app.get("/")
async def root():
    """
    Basic health check
    """
    return {"message": "EvolutiaCloud DataSave API running successfully"}
