from typing import Annotated

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..database import get_db
from ..schemas.user import LoginUser
from ..services.auth import authenticate_user, create_tokens

router = APIRouter()


@router.post("/login")
def login(user: LoginUser, db: Annotated[Session, Depends(get_db)]):
    auth_user = authenticate_user(user, db)
    access, refresh = create_tokens(auth_user)
    return {
        "access_token": access,
        "refresh_token": refresh,
        "token_type": "bearer",
    }


@router.post("/refresh-token")
def refresh_token():
    pass


@router.post("/logout")
def logout():
    pass


# @router.get("/test")
# def test(payload: Annotated[dict, Depends(check_access_token)]):
#     print(payload)
#     return payload
