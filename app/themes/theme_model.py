from pydantic import BaseModel

class Theme(BaseModel):
    primary_color: str
    background_color: str
    font: str
    border_radius: str = "8px"
