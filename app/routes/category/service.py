from sqlmodel import Session
from .repository import CategoryRepository
from .schemas import CategoryCreate, CategoryRead
from .exceptions import CategoryAlreadyExistsException, CategoryServerErrorException
from sqlalchemy.exc import IntegrityError
from typing import List

class CategoryService:
    def __init__(self, db: Session):
        self.repository = CategoryRepository(db)

    def create_category(self, category_data: CategoryCreate) -> CategoryRead:
        try:
            existing = self.repository.get_by_label(category_data.label)
            if existing:
                raise CategoryAlreadyExistsException()
            
            category = self.repository.create(category_data)
            return CategoryRead.model_validate(category)  # ← Plus besoin de from_attributes=True
        except IntegrityError:
            raise CategoryAlreadyExistsException()
        except CategoryAlreadyExistsException:
            raise
        except Exception as e:
            print(f"Error in create_category: {str(e)}")
            raise CategoryServerErrorException()

    def get_all_categories(self) -> List[CategoryRead]:
        try:
            categories = self.repository.get_all()
            return [CategoryRead.model_validate(cat) for cat in categories]  # ← Plus besoin de from_attributes=True
        except Exception as e:
            print(f"Error in get_all_categories: {str(e)}")
            raise CategoryServerErrorException()