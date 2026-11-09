"""Database configuration for isolated development.

No implicit production credentials, no connection at import time, no automatic
schema creation. A missing database URL means DB-dependent functionality is
unavailable, not permission to use insecure development defaults.
"""
import os

from fastapi import HTTPException
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.pool import StaticPool

DATABASE_URL = os.getenv("DANREXO_DATABASE_URL") or os.getenv("DATABASE_URL")

# Engine construction does not contact the server; no create_all at import.
if DATABASE_URL:
    options = {"pool_pre_ping": True}
    if DATABASE_URL in {"sqlite://", "sqlite:///:memory:"}:
        options = {"connect_args": {"check_same_thread": False}, "poolclass": StaticPool}
    engine = create_engine(DATABASE_URL, **options)
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
else:
    engine = None
    SessionLocal = None

Base = declarative_base()


def get_db():
    if SessionLocal is None:
        raise HTTPException(status_code=503, detail="Database not configured")
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
