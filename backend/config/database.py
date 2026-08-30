import os
from typing import Generator
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from model import Base, User, Item

DATABASE_URL = os.getenv("DATABASE_URL", None)
if (DATABASE_URL is None):
    raise ValueError("Database URL is not loading (config/database.py)")

engine = create_engine(
    DATABASE_URL,
    connect_args={},
    echo=False
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
)

def setup_db():
    Base.metadata.create_all(bind=engine)

def get_db() -> Generator[Session, None, None]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()