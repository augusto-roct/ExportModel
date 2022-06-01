from src.app.models.utils import set, get
from src.app.models.config.config import db

async def InsertData(collection, document, data): 
    return await set.Set(collection, document, data, db)

async def GetData(collection, document): 
    return await get.Get(collection, document, db)