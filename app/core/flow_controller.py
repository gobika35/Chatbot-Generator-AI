import json
from groq import Groq
from app.config import settings
from app.core.intent_engine import detect_intent
from app.memory.conversation_state import get_state, update_state

client = Groq(api_key=settings.GROQ_API_KEY)

RESPONSE_RULES = """
MANDATORY RESPONSE FORMAT:
- Maximum 5 bullet points
- Each bullet must be ONE short sentence
- NO paragraphs
- NO explanations unless explicitly asked
- Be concise and professional
- Focus only on business information
"""

def handle_message(bot_id, user_message, session_id):
    # Load chatbot config
    with open(f"data/bots/{bot_id}.json", "r") as f:
        bot = json.load(f)

    # Intent handling
    state = get_state(session_id) or {}
    intent = state.get("intent")

    if not intent:
        intent = detect_intent(user_message)
        update_state(session_id, intent)

    # LLM call with strict limits
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
        max_tokens=120,      # Hard limit to prevent long answers
        temperature=0.3      # Less creativity, more control
    )

    if not response.choices or not response.choices[0].message:
        return "• Sorry, I couldn’t process that\n• Please try again"

    return response.choices[0].message.content.strip()
