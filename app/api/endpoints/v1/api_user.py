from http import HTTPStatus
from typing import Optional, List
from uuid import UUID

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from starlette.requests import Request

from app.core.db.deps import get_db
from app.database.postgres.model.model import User
from app.schemas.user import UserResponse, UserRequest
from app.services import user_service

api_router = APIRouter()


@api_router.post("", response_model=UserResponse, status_code=HTTPStatus.CREATED)
async def create_user(user_request: UserRequest, request: Request, db: Session = Depends(get_db)) -> UserResponse:
    user: Optional[User] = user_service.create_user(user_request=user_request,
                                                    request=request, db=db)
    return user


@api_router.get("", response_model=List[UserResponse])
async def get_users(db: Session = Depends(get_db)) -> List[UserResponse]:
    return user_service.get_users(db=db)


@api_router.get("/{id}", response_model=UserResponse)
async def get_user_by_id(id: UUID,
                         db: Session = Depends(get_db)
                         ) -> UserResponse:
    return user_service.get_user_by_id(id=id, db=db)


@api_router.put("/{id}", response_model=UserResponse, status_code=HTTPStatus.OK)
async def update_user(id: UUID, user_request: UserRequest, request: Request,
                      db: Session = Depends(get_db)) -> UserResponse:
    user: Optional[User] = user_service.update_user(id=id, user_request=user_request,
                                                    request=request, db=db)
    return user


@api_router.delete("/{id}", status_code=HTTPStatus.OK)
async def delete_user_by_id(id: UUID,
                            db: Session = Depends(get_db)
                            ):
    user_service.delete_user_by_id(id=id, db=db)
