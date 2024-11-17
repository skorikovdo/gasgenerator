from typing import Annotated
from fastapi import Response, Request, Cookie

from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from ..database import get_db
from ..schemas.user import LoginUser, User
from ..services.auth import (
    authenticate_user,
    create_tokens,
    check_access_token,
    get_current_user_by_id,
)

router = APIRouter()


@router.post("/login")
def login(user: LoginUser, db: Annotated[Session, Depends(get_db)], response: Response):
    auth_user = authenticate_user(user, db)
    access, refresh = create_tokens(auth_user)
    response = JSONResponse(
        content={
            "access_token": access,
            "token_type": "bearer",
            "user": {"name": auth_user.name, "id": auth_user.id},
        }
    )
    response.set_cookie(
        key="refresh_token",
        value=f"Bearer {refresh}",
        httponly=True,
        secure=True,
        # samesite="none",
        expires=60 * 60 * 24,
        # domain="localhost",
    )
    return response


@router.post("/refresh-token")
def refresh_token():
    pass


@router.post("/logout")
def logout():
    pass


@router.get("/current-user", dependencies=[Depends(check_access_token)])
def get_current_user(
    request: Request,
    db: Annotated[Session, Depends(get_db)],
    refresh_token: Annotated[str | None, Cookie()] = None,
) -> User | None:
    print(refresh_token)
    user = get_current_user_by_id(request.state.user_id, db)
    return user


# @router.get("/test")
# def test(payload: Annotated[dict, Depends(check_access_token)]):
#     print(payload)
#     return payload
