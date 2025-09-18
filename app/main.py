from fastapi import FastAPI
from app.api.v1 import news
from app.db.init_db import create_db_and_tables
from app.core.config import API_V1_PREFIX, API_VERSION, API_V1_PREFIX
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title=API_VERSION, version=API_VERSION)

create_db_and_tables()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"], 
    allow_headers=["*"], 
)
app.include_router(news.router, prefix=f"{API_V1_PREFIX}/news", tags=["News"])
