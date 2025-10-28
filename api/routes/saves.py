from fastapi import APIRouter, UploadFile, File, HTTPException
from api.utils.db import get_db
import os, hashlib, datetime
import config

router = APIRouter()

@router.post("/upload")
async def upload_save(userid: int, file: UploadFile = File(...)):
    # Storage path
    base_path = config["storage"]["base_path"]
    user_path = os.path.join(base_path, str(userid))
    os.makedirs(user_path, exist_ok=True)

    file_path = os.path.join(user_path, file.filename)
    with open(file_path, "wb") as f:
        content = await file.read()
        f.write(content)

    # SHA3 hash for corruption check
    sha3 = hashlib.sha3_256()
    sha3.update(content)
    file_hash = sha3.hexdigest()

    # Save metadata in DB
    db = get_db()
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    db.execute(
        "INSERT INTO `CloudSave-Saves` (userid, savefilename, savecore, console, savesize, savepath, lastsync) VALUES (%s,%s,%s,%s,%s,%s,%s)",
        (userid, file.filename, "unknown", "unknown", len(content), file_path, now)
    )
    db.commit()

    return {"message": "File uploaded", "sha3": file_hash}
