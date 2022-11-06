from fastapi import APIRouter

from app.api.endpoints.v1 import api_user

api_router = APIRouter(tags=["CRUD APIs"])
api_router.include_router(api_user.api_router, prefix="/users")
