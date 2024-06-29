import datetime
from typing import Annotated
from fastapi import Cookie, HTTPException

from etal import config, db


async def get_user(
    session_id: Annotated[str | None, Cookie(alias=config.COOKIE_NAME)] = None
) -> db.user.User:
    if session_id is None:
        raise HTTPException(status_code=401, detail="Unauthorized")

    session = db.session.find_by_id(session_id)
    if session is None or session.expires_at < datetime.datetime.now():
        raise HTTPException(status_code=401, detail="Unauthorized")

    user = db.user.find_by_id(session.user_id)
    if user is None:
        raise HTTPException(status_code=401, detail="Unauthorized")

    return user
