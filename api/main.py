from fastapi import FastAPI
from api.routes import auth, saves, users

app = FastAPI(title="EvolutiaCloud DataSave Core API", version="0.1.0")

app.include_router(auth.router)
app.include_router(saves.router)
app.include_router(users.router)

@app.get("/")
def root():
    return {"message": "EvolutiaCloud DataSave API running successfully"}
