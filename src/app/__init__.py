from fastapi import FastAPI
from src.app.routers import routers
import src.app.models.config.connection

app = FastAPI()

app.include_router(routers.router)