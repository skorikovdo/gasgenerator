import random

from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .config import settings
from .routes.auth import router
from .routes.test import router as test_router
from .services.auth import check_access_token

origins = [
    "*",
]


app = FastAPI(debug=settings.DEBUG)
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
    return {"data": random.randint(1, 100)}
