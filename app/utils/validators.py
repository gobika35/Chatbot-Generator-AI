def validate_phone(phone: str) -> bool:
    return phone.isdigit() and 7 <= len(phone) <= 15

def validate_email(email: str) -> bool:
    return "@" in email and "." in email
