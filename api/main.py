from fastapi import FastAPI
from api.routes import auth, saves, users

app = FastAPI(title="EvolutiaCloud DataSave Core API", version="0.01.0")

# Include routers
app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(saves.router, prefix="/saves", tags=["saves"])
app.include_router(users.router, prefix="/users", tags=["users"])

@app.get("/")
def root():
    return {"message": "EvolutiaCloud DataSave API running successfully"}
