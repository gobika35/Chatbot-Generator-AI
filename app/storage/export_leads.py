import json
from pathlib import Path

def export_leads(bot_id: str):
    path = Path(f"data/leads/{bot_id}.json")
    if not path.exists():
        return []

    with open(path, "r") as f:
        return json.load(f)
