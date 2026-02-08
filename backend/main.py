from contextlib import asynccontextmanager
from fastapi import FastAPI

from .db.database import init_db
from .core.config import config

# Init database before the app runs 
@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield 

app = FastAPI(title=config.app_name, lifespan=lifespan)
