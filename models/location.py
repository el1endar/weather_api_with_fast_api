from pydantic import BaseModel
from typing import Optional


class Location(BaseModel):
    city: str = "Kraków"
    state: Optional[str] = None
    country: str = "PL"
