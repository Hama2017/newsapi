from fastapi import APIRouter, Depends, HTTPException
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
    return ApiResponse(data=result)

@router.get("/", response_model=ApiResponse[List[CategoryRead]])
def get_all_categories(db: Session = Depends(get_session)):
    service = CategoryService(db)
    result = service.get_all_categories()
    return ApiResponse(data=result)

@router.get("/{category_id}", response_model=ApiResponse[CategoryRead])
def get_category_by_id(
    category_id: int,
    db: Session = Depends(get_session)
):
    service = CategoryService(db)
    result = service.get_category_by_id(category_id)
    return ApiResponse(data=result)