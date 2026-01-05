from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

load_dotenv()

# Alapértelmezésben SQLite, de ha van környezeti változó (Renderen), akkor azt használja
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./autokozmetika.db")

# Kijavítjuk a PostgreSQL vs SQLite beállítási különbségeket
connect_args = {}
if "sqlite" in DATABASE_URL:
    # Csak SQLite-nál kell ez a beállítás
    connect_args = {"check_same_thread": False}

# ITT A LÉNYEG: a pool_pre_ping=True
engine = create_engine(
    DATABASE_URL, 
    connect_args=connect_args,
    pool_pre_ping=True  # <--- EZ JAVÍTJA A "MÁSODIKRA MŰKÖDIK" HIBÁT!
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()