import datetime
from typing import Annotated

import uuid
import argon2
from fastapi import APIRouter, Cookie, HTTPException, Depends
from fastapi.responses import JSONResponse, Response

from etal import config, db
from . import helpers, input_models

router = APIRouter()
hasher = argon2.PasswordHasher()


@router.get("/register")
async def register(input: input_models.RegisterInput):
    user = db.user.find_by_username(input.username)
    if user is not None:
        return JSONResponse(
            {"detail": "A user with that username already exists!"},
            status_code=400,
        )

    user = db.user.User(
        username=input.username,
        password=hasher.hash(input.password),
        name=input.name,
        email=input.email,
    )
    db.user.upsert(user)

    return JSONResponse({"success": True}, status_code=201)


@router.get("/login", response_model=db.user.UserDTO)
async def login(input: input_models.LoginInput, response: Response) -> db.user.User:
    user = db.user.find_by_username(input.username)
    if user is None:
        raise HTTPException(
            status_code=401,
            detail="Either a user with that username does not exist or your password is incorrect!",
        )

    try:
        hasher.verify(user.password, input.password)
        if hasher.check_needs_rehash(user.password):
            user.password = hasher.hash(input.password)
            db.user.upsert(user)
    except:
        raise HTTPException(
            status_code=401,
            detail="Either a user with that username does not exist or your password is incorrect!",
        )

    session = db.session.Session(
        user_id=user.id,  # type: ignore
        expires_at=datetime.datetime.now() + datetime.timedelta(days=7),
    )
    db.session.upsert(session)

    response.set_cookie(
        config.COOKIE_NAME,
        str(session.id),
        max_age=60 * 60 * 24 * 7,
        httponly=True,
    )

    return user


@router.get("/logout")
async def logout(
    res: Response,
    session_id: Annotated[str | None, Cookie(alias=config.COOKIE_NAME)] = None,
):
    if session_id is None:
        raise HTTPException(status_code=401, detail="Unauthorized")

    db.session.delete(uuid.UUID(session_id))
    res.delete_cookie(config.COOKIE_NAME)
    return {"success": True}


@router.get("/me", response_model=db.user.UserDTO)
async def me(user: Annotated[db.user.User, Depends(helpers.get_user)]) -> db.user.User:
    return user
