from sqlalchemy import Column, Integer, String, Float, DateTime
from datetime import datetime
from .database import Base

class AutoJob(Base):
    __tablename__ = "munkak"
    id = Column(Integer, primary_key=True, index=True)
    rendszam = Column(String, index=True)
    tipus = Column(String)
    szolgaltatas = Column(String)
    statusz = Column(String, default="Várakozás")
    ar = Column(Float)
    letrehozva = Column(DateTime, default=datetime.utcnow)
