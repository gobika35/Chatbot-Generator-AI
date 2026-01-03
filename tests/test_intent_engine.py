from app.core.intent_engine import detect_intent

def test_appointment_intent():
    assert detect_intent("I want to book an appointment") == "appointment"

def test_purchase_intent():
    assert detect_intent("What is the price? I want to buy") == "purchase"

def test_default_intent():
    assert detect_intent("Tell me about your services") == "inquiry"
