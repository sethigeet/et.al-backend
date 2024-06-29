from typing import Optional

from pydantic import BaseModel, EmailStr
from sqlmodel import SQLModel, Field, Session, select

from . import get_engine


class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    username: str = Field(unique=True, min_length=3, max_length=50)
    password: str
    name: str
    email: EmailStr


class UserDTO(BaseModel):
    id: int
    username: str
    name: str
    email: str


def find_by_id(id: int) -> Optional[User]:
    with Session(get_engine()) as session:
        statement = select(User).where(User.id == id)
        user = session.exec(statement).first()

    return user


def find_by_username(username: str) -> Optional[User]:
    with Session(get_engine()) as session:
        statement = select(User).where(User.username == username)
        user = session.exec(statement).first()

    return user


def upsert(user: User):
    with Session(get_engine(), expire_on_commit=False) as session:
        session.add(user)
        session.commit()
