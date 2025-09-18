from fastapi import APIRouter, Depends
from sqlmodel import Session
from app.db.base import get_session
from app.schemas.response import ApiResponse
from .service import CategoryService
from .schemas import CategoryCreate, CategoryRead
from typing import List

router = APIRouter()

@router.post("/", response_model=ApiResponse[CategoryRead])
def create_category(
    category_data: CategoryCreate,
    db: Session = Depends(get_session)
):
    service = CategoryService(db)
    result = service.create_category(category_data)
    return ApiResponse(ok=True, result=result)

@router.get("/", response_model=ApiResponse[List[CategoryRead]])
def get_all_categories(db: Session = Depends(get_session)):
    service = CategoryService(db)
    result = service.get_all_categories()
    return ApiResponse(ok=True, result=result)

