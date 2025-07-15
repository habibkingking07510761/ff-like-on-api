from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import json

app = FastAPI()

with open("habib.json") as f:
    tokens = json.load(f)["tokens"]  # ধরে নিচ্ছি tokens একটা লিস্ট

class LikeRequest(BaseModel):
    user_id: int
    action: str

@app.post("/like")
async def like_post(data: LikeRequest):
    if data.action != "like":
        raise HTTPException(status_code=400, detail="Invalid action")

    # এখানে সব token দিয়ে লাইক সিমুলেট করবে
    likes_done = []
    for token in tokens:
        # বাস্তবে এখানে তোমার টোকেন দিয়ে freefire like করার API call বা লজিক হবে
        # এখানে শুধু সিমুলেট করছি
        likes_done.append(f"Liked with token {token[:10]}...")

    return {
        "status": "success",
        "user_id": data.user_id,
        "total_likes": len(likes_done),
        "details": likes_done
    }
