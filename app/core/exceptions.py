from app.enums.error_codes import ErrorCode

class BaseApiException(Exception):
    """Base class for all API exceptions"""
    def __init__(self, status_code: int, error_code: ErrorCode):
        self.status_code = status_code
        self.error_code = error_code
        self.detail = {
            "ok": False,
            "result": {"detail": error_code.value}
        }
        super().__init__(f"{status_code}: {error_code.value}")