from fastapi import FastAPI
from src.app.routers import routers

app = FastAPI()

app.include_router(routers.router)