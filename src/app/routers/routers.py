from fastapi import APIRouter
from src.app.controllers.export import getModel
router = APIRouter()

@router.get("/", status_code=200)
async def root():
    return {"message": "API Works!"}

@router.get("/{filePath:path}", status_code=200)
async def model(filePath: str):
    return await getModel(filePath)