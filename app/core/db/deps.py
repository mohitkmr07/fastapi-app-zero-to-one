from typing import Generator, Optional

from app.core.db.db_session import SessionLocal


def get_db() -> Generator:
    db: Optional[SessionLocal] = None
    try:
        db = SessionLocal()
        yield db
    finally:
        if db:
            db.close()
