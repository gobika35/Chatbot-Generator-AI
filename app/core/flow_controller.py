import json
from groq import Groq
from app.config import settings
from app.core.intent_engine import detect_intent
from app.memory.conversation_state import get_state, update_state

client = Groq(api_key=settings.GROQ_API_KEY)

MAX_MESSAGE_LENGTH = 500
MAX_TURNS = 12

RESPONSE_RULES = """
MANDATORY RESPONSE FORMAT:
- Maximum 5 bullet points
- Each bullet must be ONE short sentence
- NO paragraphs
- NO explanations unless explicitly asked
- Be concise and professional
- Focus only on business information
"""

def handle_message(bot_id: str, user_message: str, session_id: str):
    # Basic input hardening
    if not user_message or not user_message.strip():
        return "• Please enter a valid message"

    if len(user_message) > MAX_MESSAGE_LENGTH:
        return "• Message is too long\n• Please shorten your question"

    # Load chatbot config safely
    try:
        with open(f"data/bots/{bot_id}.json", "r") as f:
            bot = json.load(f)
    except Exception:
        return "• Chatbot configuration not found"

    # Load conversation state
    state = get_state(session_id) or {}
    turns = state.get("turns", 0)
    intent = state.get("intent")

    # Turn limit enforcement
    if turns >= MAX_TURNS:
        return "• This conversation has reached its limit\n• Please contact a human assistant"

    # Intent detection + locking
    if not intent:
        intent = detect_intent(user_message)

    update_state(
        session_id=session_id,
        intent=intent,
        turns=turns + 1
    )

    # LLM call with strict limits
    try:
        response = client.chat.completions.create(
            model=settings.MODEL_NAME,
            messages=[
                {
                    "role": "system",
                    "content": bot["system_prompt"] + RESPONSE_RULES
                },
                {
                    "role": "user",
                    "content": user_message
                }
            ],
            max_tokens=120,
            temperature=0.3
        )
    except Exception:
        return "• Unable to respond right now\n• Please try again later"

    if not response.choices or not response.choices[0].message:
        return "• Sorry, I couldn’t process that\n• Please try again"

    final_reply = response.choices[0].message.content.strip()

    # Final response safety check
    if len(final_reply) > 600:
        return "• Response was too long\n• Please ask a simpler question"

    return final_reply
