from typing import Optional, List
from uuid import UUID

from sqlalchemy.orm import Session

from app.common.constants import ONE_HOUR_IN_SECONDS
from app.core.cache.redis_cache import GetCachedEntity
from app.database.postgres.model.model import User
from app.database.postgres.repository.base import BaseRepository


class UserRepository(BaseRepository[User]):

    # extra queries that can be over written
    def get_by_name(self, name: str, db: Session) -> Optional[List[User]]:
        return db.query(self.model).filter(self.model.name == name).all()

    @GetCachedEntity(('id', ONE_HOUR_IN_SECONDS))
    async def get_by_id(self, id: UUID, db: Session) -> Optional[User]:
        return BaseRepository.get_by_id(self, id=id, db=db)


user_repository = UserRepository(User)
