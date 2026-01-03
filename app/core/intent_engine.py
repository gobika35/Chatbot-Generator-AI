def detect_intent(message: str):
    msg = message.lower()
    if "appoint" in msg or "book" in msg:
        return "appointment"
    if "price" in msg or "buy" in msg:
        return "purchase"
    return "inquiry"
