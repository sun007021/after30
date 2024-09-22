import time
from typing import Any
from fastapi import HTTPException, Depends
from app.response import OK, CREATED
from model.schema import users_schema
from . import api
from app.api.users.service.users import sign_up
from core.db import get_db
from sqlalchemy.ext.asyncio import AsyncSession


@api.post(
    '/users',
    summary="sign_up",
    response_model=CREATED[users_schema.UserCreated],
)
async def user_create(  # 00-01 sign up
    user: users_schema.Users,
    db: AsyncSession = Depends(get_db)
):
    created_user = await sign_up(db, user)
    return CREATED(
        users_schema.UserCreated(
            email=created_user.email
        )
    )
