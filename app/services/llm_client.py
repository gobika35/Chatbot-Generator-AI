from groq import Groq
from app.config import settings

_client = Groq(api_key=settings.GROQ_API_KEY)

def chat(messages: list[dict]):
    response = _client.chat.completions.create(
        model=settings.MODEL_NAME,
        messages=messages
    )
    return response.choices[0].message.content
