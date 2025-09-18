from sqlmodel import Session, select
from typing import List, Optional
from .model import Category
from .schemas import CategoryCreate

class CategoryRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, category_data: CategoryCreate) -> Category:
        category = Category(**category_data.model_dump())
        self.db.add(category)
        self.db.commit()
        self.db.refresh(category)
        return category

    def get_all(self) -> List[Category]:
        return self.db.exec(select(Category)).all()

    def get_by_id(self, category_id: int) -> Optional[Category]:
        return self.db.exec(select(Category).where(Category.id == category_id)).first()

    def get_by_label(self, label: str) -> Optional[Category]:
        return self.db.exec(select(Category).where(Category.label == label)).first()

    def exists_by_id(self, category_id: int) -> bool:
        return self.get_by_id(category_id) is not None