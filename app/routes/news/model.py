from sqlmodel import SQLModel, Field, Relationship
from typing import Optional

class News(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str
    subtitle: str
    category_id: int = Field(foreign_key="category.id")
    
    category: Optional["Category"] = Relationship(back_populates="news")