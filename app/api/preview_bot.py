from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field
from app.core.flow_controller import handle_message

router = APIRouter()

class PreviewInput(BaseModel):
    bot_id: str
    message: str = Field(..., max_length=500)
    session_id: str

@router.post("/")
def preview_chat(data: PreviewInput):
    try:
        reply = handle_message(
            bot_id=data.bot_id,
            user_message=data.message,
            session_id=data.session_id
        )
        return {"reply": reply}
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid request")
