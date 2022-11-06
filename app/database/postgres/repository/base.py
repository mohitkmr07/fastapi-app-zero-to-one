from datetime import datetime
from typing import Any, Generic, List, Optional, Type, TypeVar
from uuid import UUID

from sqlalchemy.orm import Session

from app.database.postgres.model.model import Base

ModelType = TypeVar("ModelType", bound=Base)


class BaseRepository(Generic[ModelType]):
    def __init__(self, model: Type[ModelType]):
        """
        CRUD object with default methods to Create, Read, Update, Delete (CRUD).
        **Parameters**
        * `model`: A SQLAlchemy model class
        * `schema`: A Pydantic model (schema) class
        """
        self.model = model

    def get_all_by_ids(self, db: Session, *, ids: Any) -> Optional[List[ModelType]]:
        if ids is None:
            ids = []
        return db.query(self.model).filter(self.model.id.in_(ids)).all()

    def get_by_id(self, id: UUID, db: Session) -> Optional[ModelType]:
        return db.query(self.model).filter(self.model.id == id).first()

    def get(self, *, offset: int = 0, limit: int = 100, db: Session) -> Optional[List[ModelType]]:
        return db.query(self.model).offset(offset).limit(limit).all()

    def create(self, *, obj_in: Optional[ModelType], db: Session) -> Optional[ModelType]:
        if not obj_in:
            return None

        obj_in.created_at = datetime.utcnow()
        obj_in.updated_at = obj_in.created_at
        db.add(obj_in)
        db.commit()
        db.refresh(obj_in)
        return obj_in

    def update(self, *, db_obj: Optional[ModelType], db: Session) -> Optional[ModelType]:
        if not db_obj:
            return None

        db_obj.updated_at = datetime.utcnow()
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def delete(self, *, db_obj: Optional[ModelType], db: Session):
        if db_obj:
            db.delete(db_obj)
            db.commit()

    def delete_by_id(self, *, id: UUID, db: Session):
        obj = db.query(self.model).get(id)
        db.delete(obj)
        db.commit()
