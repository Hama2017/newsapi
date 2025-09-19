from enum import Enum

class ErrorCode(str, Enum):
    NOT_FOUND = "Category not found"
    ALREADY_EXISTS = "Category already exists"
    SERVER_ERROR = "Category server error"