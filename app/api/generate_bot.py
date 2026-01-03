from fastapi import APIRouter
from pydantic import BaseModel
from app.core.bot_builder import build_chatbot

router = APIRouter()

class BusinessInput(BaseModel):
    business_name: str
    business_type: str
    services: list[str]
    language: str = "English"
    tone: str = "professional"

@router.post("/")
def generate_bot(data: BusinessInput):
    bot_config = build_chatbot(data)
    return bot_config
