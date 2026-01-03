import json
from datetime import datetime
from pathlib import Path

LEAD_DIR = Path("data/leads")
LEAD_DIR.mkdir(parents=True, exist_ok=True)

def save_lead(bot_id: str, lead_data: dict):
    file_path = LEAD_DIR / f"{bot_id}.json"

    lead_data["timestamp"] = datetime.utcnow().isoformat()

    if file_path.exists():
        with open(file_path, "r") as f:
            leads = json.load(f)
    else:
        leads = []

    leads.append(lead_data)

    with open(file_path, "w") as f:
        json.dump(leads, f, indent=2)

    return True
