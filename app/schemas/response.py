from pydantic import BaseModel
from typing import Generic, TypeVar
from app.enums.error_codes import ErrorCode

T = TypeVar('T')

class ErrorResponse(BaseModel):
    detail: ErrorCode

class ApiResponse(BaseModel, Generic[T]):
    ok: bool
    result: T