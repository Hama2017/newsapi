from enum import Enum

class ErrorCode(str, Enum):
    NOT_FOUND = "News not found"
    CATEGORY_NOT_FOUND = "Category not found for this news"
    SERVER_ERROR = "News server error"