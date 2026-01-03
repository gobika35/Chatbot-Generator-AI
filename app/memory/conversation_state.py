_states = {}

def get_state(session_id: str):
    return _states.get(session_id, {})

def update_state(session_id: str, intent: str):
    _states[session_id] = {"intent": intent}
