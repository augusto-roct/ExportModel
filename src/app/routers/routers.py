from fastapi import APIRouter
from src.app.controllers.export import GetData, InsertData, GetMetrics

router = APIRouter()

@router.get("/metrics/{collection}", status_code=200)
async def Metrics(collection: str):
    print(collection)
    return await GetMetrics(collection)

@router.post("/{collection}/{document}", status_code=200)
async def Insert(collection: str, document: str, data: dict, user: str, password: str):
    return await InsertData(collection, document, data, user, password)

@router.get("/{collection}/{document}", status_code=200)
async def Insert(collection: str, document: str):
    return await GetData(collection, document)

@router.get("/", status_code=200)
async def root():
    return {"message": "API Works!"}