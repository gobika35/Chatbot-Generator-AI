import uuid
import json
from app.core.prompt_factory import build_system_prompt

def build_chatbot(data):
    bot_id = str(uuid.uuid4())

    system_prompt = build_system_prompt(data)

    bot_config = {
        "bot_id": bot_id,
        "business": data.dict(),
        "system_prompt": system_prompt,
        "intents": ["appointment", "inquiry", "purchase"],
        "theme": {
            "primary_color": "#000000",
            "background_color": "#ffffff",
            "font": "sans-serif"
        }
    }

    with open(f"data/bots/{bot_id}.json", "w") as f:
        json.dump(bot_config, f, indent=2)

    return {"bot_id": bot_id}
