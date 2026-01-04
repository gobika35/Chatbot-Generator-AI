_states = {}

def get_state(session_id: str):
    return _states.get(session_id, {"turns": 0})

def update_state(session_id: str, intent: str, turns: int):
    _states[session_id] = {
        "intent": intent,
        "turns": turns
    }
