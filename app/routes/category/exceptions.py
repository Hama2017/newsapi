from app.enums.error_codes import ErrorCode
from app.core.exceptions import BaseApiException

class CategoryNotFoundException(BaseApiException):
    def __init__(self):
        super().__init__(status_code=404, error_code=ErrorCode.NOT_FOUND)

class CategoryAlreadyExistsException(BaseApiException):
    def __init__(self):
        super().__init__(status_code=409, error_code=ErrorCode.ALREADY_EXISTS)

class CategoryServerErrorException(BaseApiException):
    def __init__(self):
        super().__init__(status_code=500, error_code=ErrorCode.SERVER_ERROR)