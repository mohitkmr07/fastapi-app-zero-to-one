from __future__ import annotations

from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, constr


class UserBase(BaseModel):
    name: constr(min_length=1, strip_whitespace=True)  # type: ignore
    age: int  # type: ignore


class UserRequest(UserBase):
    pass


class UserResponse(UserBase):
    id: UUID
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
