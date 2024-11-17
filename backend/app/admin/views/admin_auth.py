from sqladmin.authentication import AuthenticationBackend
from starlette.requests import Request
from starlette.responses import Response
from fastapi.security import OAuth2PasswordBearer
from ...services.auth import get_user
from ...database import get_db

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/admin/login")


class AdminAuth(AuthenticationBackend):
    async def login(self, request: Request) -> bool:
        form = await request.form()
        db = get_db().__next__()
        username, password = form["username"], form["password"]
        user = get_user(db, str(username))
        if user:
            request.session.update({"token": "..."})
            return True
        return False

    async def logout(self, request: Request) -> bool:
        request.session.clear()
        return True

    async def authenticate(self, request: Request) -> Response | bool:
        token = request.session.get("token")

        if not token:
            return False

        # Check the token in depth
        return True
