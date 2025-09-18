from pydantic import BaseModel, ConfigDict
from typing import Optional
from app.routes.category.schemas import CategoryRead

class NewsCreate(BaseModel):
    title: str
    subtitle: str
    category_id: int

class NewsUpdate(BaseModel):
    title: Optional[str] = None
    subtitle: Optional[str] = None
    category_id: Optional[int] = None

class NewsRead(BaseModel):
    model_config = ConfigDict(from_attributes=True) 
    
    id: int
    title: str
    subtitle: str
    category_id: int
    category: Optional[CategoryRead] = None