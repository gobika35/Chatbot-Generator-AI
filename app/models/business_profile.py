from pydantic import BaseModel
from typing import List

class BusinessProfile(BaseModel):
    business_name: str
    business_type: str
    services: List[str]
    language: str
    tone: str
