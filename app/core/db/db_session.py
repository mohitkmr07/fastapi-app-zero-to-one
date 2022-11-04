from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.core.config import settings

engine = create_engine(settings.SQLALCHEMY_DATABASE_URI,
                       pool_pre_ping=settings.POOL_PRE_PING,
                       pool_size=settings.POOL_SIZE,
                       echo=settings.ECHO_POOL,
                       max_overflow=settings.MAX_OVERFLOW,
                       pool_recycle=settings.POOL_RECYCLE_IN_SECONDS,
                       echo_pool=settings.ECHO_POOL,
                       pool_reset_on_return=settings.POOL_RESET_ON_RETURN,
                       pool_timeout=settings.POOL_TIMEOUT_IN_SECONDS)
SessionLocal = sessionmaker(autocommit=False, autoflush=True, bind=engine)
