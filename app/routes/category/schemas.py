from pydantic import BaseModel, ConfigDict

class CategoryCreate(BaseModel):
    label: str

class CategoryRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    
    id: int
    label: str