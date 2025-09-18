from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from app.core.exceptions import BaseApiException
from app.enums.error_codes import ErrorCode

async def api_exception_handler(request: Request, exc: BaseApiException):
    """Generic handler for all API exceptions"""
    return JSONResponse(
        status_code=exc.status_code,
        content=exc.detail
    )

async def validation_exception_handler(request: Request, exc: RequestValidationError):
    """Handler for Pydantic validation errors"""
    return JSONResponse(
        status_code=422,
        content={
            "ok": False,
            "result": {"detail": ErrorCode.VALIDATION_ERROR.value}
        }
    )

def register_exception_handlers(app: FastAPI):
    """Register all exception handlers"""
    app.add_exception_handler(BaseApiException, api_exception_handler)
    app.add_exception_handler(RequestValidationError, validation_exception_handler)