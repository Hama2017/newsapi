from pydantic import BaseModel
from typing import Generic, TypeVar
from enum import Enum

T = TypeVar('T')

class ApiResponse(BaseModel, Generic[T]):
    data: T

