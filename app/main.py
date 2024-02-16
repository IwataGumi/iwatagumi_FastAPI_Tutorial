from fastapi import FastAPI

from app.routers import router
from app.db.database import setup_db

app = FastAPI()

setup_db(app)

app.include_router(router, prefix="/api")
