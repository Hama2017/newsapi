from pydantic import BaseModel, ConfigDict
from typing import Optional
from app.routes.category.schemas import CategoryRead

class Category(BaseModel):
    id: int
    label: Optional[str]

class NewsCreate(BaseModel):
    title: str
    subtitle: str
    category: Category

class NewsUpdate(BaseModel):
    title: Optional[str] = None
    subtitle: Optional[str] = None
    category: Category

class NewsRead(BaseModel):
    model_config = ConfigDict(from_attributes=True) 
    
    id: int
    title: str
    subtitle: str
    category_id: int
    category: Optional[CategoryRead] = None