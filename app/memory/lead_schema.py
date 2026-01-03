from pydantic import BaseModel

class Lead(BaseModel):
    name: str
    phone: str | None = None
    email: str | None = None
    intent: str
