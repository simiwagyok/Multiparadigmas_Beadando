from pydantic import BaseModel, field_validator
from datetime import datetime
import re

class AutoJobCreate(BaseModel):
    rendszam: str
    tipus: str
    szolgaltatas: str
    ar: float

    @field_validator('rendszam')
    def validate_rendszam(cls, v):
        if not re.match(r"^[A-Z]{3}-[0-9]{3}$", v):
            raise ValueError('Helytelen formátum! Helyes: ABC-123')
        return v

class AutoJobResponse(BaseModel):
    id: int
    rendszam: str
    tipus: str
    szolgaltatas: str
    statusz: str
    ar: float
    letrehozva: datetime
    class Config:
        from_attributes = True

class Statisztika(BaseModel):
    bevetel: float
    ossz_auto: int
    varakozik: int
    kesz: int
