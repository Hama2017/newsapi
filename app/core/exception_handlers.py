from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError

async def validation_exception_handler(request: Request, exc: RequestValidationError):
    """Handler for Pydantic validation errors"""
    """ errors = []
    for error in exc.errors():
        field = ".".join(str(loc) for loc in error["loc"])
        message = error["msg"]
        errors.append(f"{field}: {message}")
    
    error_message = "; ".join(errors) """
    
    return JSONResponse(
        status_code=422,
        content={ "detail": "ERROR_VALIDATION"}
        
    )

def register_exception_handlers(app: FastAPI):
    """Register all exception handlers"""
    app.add_exception_handler(RequestValidationError, validation_exception_handler)