from datetime import datetime, timedelta

# from passlib.context import CryptContext
import bcrypt
import jwt
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer

from ..config import settings
from ..database import Session
from ..models.user import UserDB
from ..schemas.user import LoginUser

# pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
# oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def create_tokens(user: UserDB) -> tuple:
    access_token = jwt.encode(
        {
            "sub": user.id,
            "exp": datetime.now()
            + timedelta(settings.ACCESS_TOKEN_LIFETIME_MINUTE),
        },
        settings.SECRET_KEY,
        algorithm=settings.ALGORITM,
    )
    refresh_token = jwt.encode(
        {
            "sub": user.id,
            "exp": datetime.now()
            + timedelta(settings.REFRESH_TOKEN_LIFETIME_MINUTE),
        },
        settings.SECRET_KEY_REFRESH,
        algorithm=settings.ALGORITM,
    )
    return access_token, refresh_token


def register(db: Session, user: LoginUser):
    user_db = UserDB(
        name=user.name, hashed_password=create_pwd_hash(user.password)
    )
    db.add(user_db)
    db.commit()


def create_pwd_hash(pwd: str) -> bytes:
    pwd_bytes = pwd.encode("utf-8")
    salt = bcrypt.gensalt()
    hash_pwd = bcrypt.hashpw(password=pwd_bytes, salt=salt)
    return hash_pwd


def verify_pwd(plain, hash_pwd):
    pwd_plain_bytes = plain.encode("utf-8")
    hash_bytes = hash_pwd.encode("utf-8")
    return bcrypt.checkpw(password=pwd_plain_bytes, hashed_password=hash_bytes)


def get_user(db: Session, user: str) -> UserDB | None:
    return db.query(UserDB).where(UserDB.name == user).first()


def authenticate_user(user: LoginUser, db: Session) -> UserDB:
    user_identificate = get_user(db, user.name)
    if not user_identificate or not verify_pwd(
        user.password, user_identificate.hashed_password
    ):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
        )
    return user_identificate


async def check_access_token(credentials=Depends(HTTPBearer())):
    token = credentials.credentials
    payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITM])
    return payload


def get_current_user_by_id():
    pass
