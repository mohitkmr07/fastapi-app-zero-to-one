from http import HTTPStatus
from typing import Optional

from starlette.responses import JSONResponse


class Error(Exception):
    """Base class for exceptions in this module."""
    pass


class RequestError(Error):
    def __init__(self, status_code: int, error_code: str, error_msg: Optional[str] = None):
        self.status_code = HTTPStatus(status_code)
        self.error_code = error_code
        self.error_msg = error_msg


ERROR = "error"
CODE = "code"
MESSAGE = "message"
REQUEST_ID = "request-id"


class RequestErrorHandler:
    def __init__(self, exc: RequestError):
        self.error_code = exc.error_code
        self.status_code = exc.status_code
        self.error_msg = exc.error_msg

    def process_message(self):
        return JSONResponse(
            status_code=self.status_code,
            content={
                ERROR: {
                    CODE: self.error_code,
                    MESSAGE: self.error_msg,
                }
            }
        )
