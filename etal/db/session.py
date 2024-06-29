from typing import Optional
from datetime import datetime
import uuid

from sqlmodel import SQLModel, Field, Session as SqlSession, select
from sqlalchemy import Uuid

from .helpers import get_engine


class Session(SQLModel, table=True):
    id: uuid.UUID = Field(
        sa_type=Uuid(as_uuid=True),  # type: ignore
        default_factory=uuid.uuid4,
        primary_key=True,
        description="The id of the session",
    )
    user_id: int = Field(
        description="The ID of the user that the session belongs to",
        foreign_key="user.id",
    )
    expires_at: datetime = Field(description="The time when the session expires")


def find_by_id(id: str) -> Optional[Session]:
    with SqlSession(get_engine()) as sql_session:
        statement = select(Session).where(Session.id == id)
        session = sql_session.exec(statement).first()
        return session


def upsert(session: Session):
    with SqlSession(get_engine(), expire_on_commit=False) as sql_session:
        sql_session.add(session)
        sql_session.commit()


def delete(id: uuid.UUID):
    with SqlSession(get_engine()) as sql_session:
        statement = select(Session).where(Session.id == id)
        session = sql_session.exec(statement).first()
        if session is None:
            return

        sql_session.delete(session)
        sql_session.commit()
