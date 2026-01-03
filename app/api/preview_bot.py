from fastapi import APIRouter
from pydantic import BaseModel
from app.core.flow_controller import handle_message

router = APIRouter()

class PreviewInput(BaseModel):
    bot_id: str
    message: str
    session_id: str

@router.post("/")
def preview_chat(data: PreviewInput):
    reply = handle_message(
        bot_id=data.bot_id,
        user_message=data.message,
        session_id=data.session_id
    )
    return {"reply": reply}
