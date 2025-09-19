from sqlmodel import Session
from fastapi import HTTPException
from .repository import CategoryRepository
from .schemas import CategoryCreate, CategoryRead
from .errors_code import ErrorCode
from sqlalchemy.exc import IntegrityError
from typing import List

class CategoryService:
    def __init__(self, db: Session):
        self.repository = CategoryRepository(db)

    def create_category(self, category_data: CategoryCreate) -> CategoryRead:
        try:
            existing = self.repository.get_by_label(category_data.label)
            if existing:
                raise HTTPException(status_code=409, detail=ErrorCode.ALREADY_EXISTS.name)

            category = self.repository.create(category_data)
            return CategoryRead.model_validate(category)

        except IntegrityError:
            raise HTTPException(status_code=409, detail=ErrorCode.ALREADY_EXISTS.name)

        except HTTPException:
            raise
        except Exception as e:
            print(f"Error in create_category: {str(e)}")
            raise HTTPException(status_code=500, detail=ErrorCode.SERVER_ERROR.name)

    def get_all_categories(self) -> List[CategoryRead]:
        try:
            categories = self.repository.get_all()
            return [CategoryRead.model_validate(cat) for cat in categories]
        except Exception as e:
            print(f"Error in get_all_categories: {str(e)}")
            raise HTTPException(status_code=500, detail=ErrorCode.SERVER_ERROR.name)

    def get_category_by_id(self, category_id: int) -> CategoryRead:
        try:
            category = self.repository.get_by_id(category_id)
            if not category:
                raise HTTPException(status_code=404, detail=ErrorCode.NOT_FOUND.name)
            
            return CategoryRead.model_validate(category)
        except HTTPException:
            raise
        except Exception as e:
            print(f"Error in get_category_by_id: {str(e)}")
            raise HTTPException(status_code=500, detail=ErrorCode.SERVER_ERROR.name)