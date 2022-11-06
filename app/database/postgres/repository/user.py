from typing import Optional, List
from uuid import UUID

from fastapi import Depends
from sqlalchemy.orm import Session

from app.core.db.deps import get_db
from app.database.postgres.model.model import User
from app.database.postgres.repository.base import BaseRepository


class UserRepository(BaseRepository[User]):

    # extra queries that can be over written
    def get_by_name(self, name: str, db: Session) -> Optional[List[User]]:
        return db.query(self.model).filter(self.model.name == name).all()


user_repository = UserRepository(User)
