from fastapi import APIRouter
from pydantic import BaseModel
import json

router = APIRouter()

class ThemeUpdate(BaseModel):
    bot_id: str
    primary_color: str
    background_color: str
    font: str

@router.post("/")
def update_theme(data: ThemeUpdate):
    path = f"data/bots/{data.bot_id}.json"

    with open(path, "r") as f:
        bot = json.load(f)

    bot["theme"] = data.dict(exclude={"bot_id"})

    with open(path, "w") as f:
        json.dump(bot, f, indent=2)

    return {"status": "theme updated"}
