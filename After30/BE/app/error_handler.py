import traceback
from fastapi import Request, FastAPI, HTTPException
from fastapi.responses import ORJSONResponse
from fastapi.exceptions import RequestValidationError
from app.response import (
    bad_request, not_found, bad_jwt_token,
    unprocessable_entity
)
from jose import JWTError
from loguru import logger
from app.exception import Duplicated_User


def init_app(app: FastAPI):

    @app.exception_handler(400)
    async def bad_request_handler(
        request: Request,
        exc: HTTPException
    ):
        return bad_request(exc.detail)

    @app.exception_handler(RequestValidationError)
    async def validation_exception_handler(
        request: Request,
        exc: RequestValidationError
    ):
        """Validation Exception Handler"""
        errors: list = exc.errors()
        detail = errors[0].get('msg') if errors else None
        for e in errors:
            if e.get('ctx'):
                e['ctx'] = str(e['ctx'])

        return unprocessable_entity(detail, errors)

    @app.exception_handler(JWTError)
    async def unauthorized_handler(
        request: Request,
        exc: JWTError
    ):
        return bad_jwt_token(str(exc.args[0]))

    @app.exception_handler(404)
    async def not_found_handler(
        request: Request,
        exc: HTTPException
    ):
        return not_found

    @app.exception_handler(500)
    async def internal_server_error_handler(
        request: Request,
        exc: HTTPException
    ):
        return ORJSONResponse(
            {'msg': 'internal_server_error'},
            status_code=500,
        )

    @app.exception_handler(Duplicated_User)
    async def already_exists_user_handler(
        request: Request,
        exc: HTTPException
    ):
        return ORJSONResponse(
            {'msg': 'already_exists_user'},
            status_code=400,
        )
