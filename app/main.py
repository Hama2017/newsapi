from fastapi import FastAPI
from app.routes.news import index
from app.db.init_db import create_db_and_tables

app = FastAPI(title="News API")

create_db_and_tables()

app.include_router(index.router, prefix="/news", tags=["News"])
