from app.core.bot_builder import build_chatbot
from pydantic import BaseModel

class DummyBusiness(BaseModel):
    business_name: str = "Test Clinic"
    business_type: str = "Healthcare"
    services: list[str] = ["Consultation"]
    language: str = "English"
    tone: str = "professional"

def test_bot_creation():
    bot = build_chatbot(DummyBusiness())
    assert "bot_id" in bot
