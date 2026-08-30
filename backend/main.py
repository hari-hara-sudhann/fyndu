from fastapi import FastAPI, Depends
from contextlib import asynccontextmanager
from config import setup_db, get_db
from model import User
from sqlalchemy.orm import Session


@asynccontextmanager
async def lifespan(app: FastAPI):
    setup_db()
    yield

app = FastAPI(lifespan=lifespan)


@app.get("/")
def root():
    return {
        "status": "healthy" 
    }


@app.get("/users")
def list_users(db: Session = Depends(get_db)):
    return db.query(User).all()