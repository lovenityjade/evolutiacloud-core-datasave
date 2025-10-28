# main.py - Entry point of the FastAPI server
from fastapi import FastAPI
from api.routes import auth, saves, users

# Create the FastAPI app
app = FastAPI(
    title="EvolutiaCloud DataSave Core API",
    version="0.01.0",
    description="Alpha 0.01.0 Prototype - Cloud Save synchronization server"
)

# Include all routers (endpoints)
app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(saves.router, prefix="/saves", tags=["saves"])
app.include_router(users.router, prefix="/users", tags=["users"])

# Root route to verify the server is running
@app.get("/")
def root():
    return {"message": "EvolutiaCloud DataSave API running successfully"}
