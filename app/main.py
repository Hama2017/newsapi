from fastapi import FastAPI
from app.routes.news.routes import router as news_router
from app.routes.category.routes import router as category_router
from app.core.config import API_TITLE, API_VERSION, API_PREFIX
from app.core.exception_handlers import register_exception_handlers
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title=API_TITLE, version=API_VERSION)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"], 
    allow_headers=["*"],
)

register_exception_handlers(app)

app.include_router(category_router, prefix=f"{API_PREFIX}/categories", tags=["Categories"])
app.include_router(news_router, prefix=f"{API_PREFIX}/news", tags=["News"])