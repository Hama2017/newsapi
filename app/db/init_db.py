from sqlmodel import SQLModel
from .base import engine
from app.models.news import News

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)
