from fastapi import APIRouter
from loguru import logger
from app.route import GzipRoute


api = APIRouter(
    route_class=GzipRoute,
    tags=['users']
)

from . import users
