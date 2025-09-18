from fastapi import APIRouter, Depends
from sqlmodel import Session
from app.db.base import get_session
from app.schemas.response import ApiResponse
from .service import NewsService
from .schemas import NewsCreate, NewsUpdate, NewsRead
from typing import List

router = APIRouter()

@router.post("/", response_model=ApiResponse[NewsRead])
def create_news(
    news_data: NewsCreate,
    db: Session = Depends(get_session)
):
    service = NewsService(db)
    result = service.create_news(news_data)
    return ApiResponse(ok=True, result=result)

@router.get("/", response_model=ApiResponse[List[NewsRead]])
def get_all_news(db: Session = Depends(get_session)):
    service = NewsService(db)
    result = service.get_all_news()
    return ApiResponse(ok=True, result=result)

@router.get("/{news_id}", response_model=ApiResponse[NewsRead])
def get_news_by_id(news_id: int, db: Session = Depends(get_session)):
    service = NewsService(db)
    result = service.get_news_by_id(news_id)
    return ApiResponse(ok=True, result=result)

@router.put("/{news_id}", response_model=ApiResponse[NewsRead])
def update_news(
    news_id: int,
    news_data: NewsUpdate,
    db: Session = Depends(get_session)
):
    service = NewsService(db)
    result = service.update_news(news_id, news_data)
    return ApiResponse(ok=True, result=result)

@router.delete("/{news_id}", response_model=ApiResponse[dict])
def delete_news(news_id: int, db: Session = Depends(get_session)):
    service = NewsService(db)
    result = service.delete_news(news_id)
    return ApiResponse(ok=True, result=result)