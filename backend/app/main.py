import random

from fastapi import Depends, FastAPI

from starlette.middleware.cors import CORSMiddleware

from .config import settings
from .routes.auth import router
from .routes.test import router as test_router
from .services.auth import check_access_token

from .admin.setup import init_admin

origins = ["http://localhost:3000"]


app = FastAPI(debug=settings.DEBUG)
init_admin(app)
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(router, prefix="/auth", tags=["auth"])
app.include_router(
    test_router,
    prefix="/test",
    tags=["q"],
    dependencies=[Depends(check_access_token)],
)


@app.get("/")
def root() -> dict:
    rand_list = [str(random.randint(1, 100)) for _ in range(10)]
    return {"data": rand_list}
