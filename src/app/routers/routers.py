from fastapi import APIRouter
from src.app.controllers.export import GetData, InsertData
from src.app.models.interfaces import testScoresOfStudents

router = APIRouter()

@router.get("/", status_code=200)
async def root():
    return {"message": "API Works!"}

@router.post("/{collection}/{document}", status_code=200)
async def Insert(collection: str, document: str, data: testScoresOfStudents.Test):
    return await InsertData(collection, document, data)

@router.get("/{collection}/{document}", status_code=200)
async def Insert(collection: str, document: str):
    return await GetData(collection, document)