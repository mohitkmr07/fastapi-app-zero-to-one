from http import HTTPStatus
from typing import Optional, List
from uuid import UUID

from sqlalchemy.orm import Session
from starlette.requests import Request

from app.common.api_error import ErrorCode
from app.common.api_exceptions import RequestError
from app.database.postgres.model.model import User
from app.database.postgres.repository.user import user_repository
from app.schemas.user import UserRequest, UserResponse


def create_user(user_request: UserRequest, request: Request, db: Session):
    user: User = User()
    user.name = user_request.name
    user.age = user_request.age
    user.context = request.url.path
    user: User = user_repository.create(db=db, obj_in=user)
    return user


def get_user_by_id(id: UUID, db: Session):
    user: Optional[User] = user_repository.get_by_id(db=db, id=id)
    if not user:
        raise RequestError(status_code=HTTPStatus.NOT_FOUND, error_code=ErrorCode.INCORRECT_USER_ID,
                           error_msg="User Not Found")
    return user


def get_users(db: Session) \
        -> List[UserResponse]:
    users: Optional[List[User]] = user_repository.get(
        db=db)

    return users


def delete_user_by_id(id: UUID, db: Session):
    validate_user_id(id=id, db=db)
    user_repository.delete_by_id(db=db, id=id)


def validate_user_id(id: UUID, db: Session):
    user: Optional[User] = user_repository.get_by_id(db=db, id=id)
    if not user:
        raise RequestError(status_code=HTTPStatus.NOT_FOUND, error_code=ErrorCode.INCORRECT_USER_ID)


def update_user(id: UUID, user_request: UserRequest, request, db):
    user: Optional[User] = user_repository.get_by_id(db=db, id=id)
    user.name = user_request.name
    user.age = user_request.age
    user.age = user_request.age
    user.context = request.url.path
    user: User = user_repository.update(db=db, db_obj=user)
    return user
