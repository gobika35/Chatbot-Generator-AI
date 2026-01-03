from pydantic import BaseModel
from app.models.business_profile import BusinessProfile
from app.themes.theme_model import Theme

class ChatbotInstance(BaseModel):
    bot_id: str
    business: BusinessProfile
    system_prompt: str
    theme: Theme
