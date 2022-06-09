from fastapi import APIRouter
from src.app.controllers.export import GetAnalisys
from src.app.controllers.set import InsertData

router = APIRouter()

@router.get("/{collection}/{document}", status_code=200)
async def Analisys(collection: str, document: str, reverse: bool):
    print("Get " + document + " to: ", collection)
    return await GetAnalisys(collection, document, reverse)

@router.post("/{collection}/{document}", status_code=200)
async def Insert(collection: str, document: str, data: dict, user: str, password: str):
    print("Insert to: ", collection)
    return await InsertData(collection, document, data, user, password)

@router.get("/", status_code=200)
async def root():
    return {"message": "API Works!"}