from app.enums.error_codes import ErrorCode
from app.core.exceptions import BaseApiException

class NewsNotFoundException(BaseApiException):
    def __init__(self):
        super().__init__(status_code=404, error_code=ErrorCode.NOT_FOUND)

class NewsAlreadyExistsException(BaseApiException):
    def __init__(self):
        super().__init__(status_code=409, error_code=ErrorCode.ALREADY_EXISTS)

class NewsServerErrorException(BaseApiException):
    def __init__(self):
        super().__init__(status_code=500, error_code=ErrorCode.SERVER_ERROR)

class NewsValidationErrorException(BaseApiException):
    def __init__(self):
        super().__init__(status_code=400, error_code=ErrorCode.VALIDATION_ERROR)