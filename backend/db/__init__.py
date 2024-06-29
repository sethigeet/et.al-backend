from typing import Optional
import os

from sqlmodel import create_engine, SQLModel
from sqlalchemy import Engine

_engine: Optional[Engine] = None


def get_engine() -> Engine:
    global _engine
    if _engine is not None:
        return _engine

    _engine = create_engine(os.environ["DATABASE_URL"])

    return _engine


def run_migrations():
    engine = get_engine()

    # TODO: Handle actual migrations
    SQLModel.metadata.create_all(engine)
